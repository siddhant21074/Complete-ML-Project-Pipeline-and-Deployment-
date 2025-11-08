import os 
import sys
import pandas as pd
import numpy as np
import dill
from pathlib import Path

# Add project root to Python path - handle both direct execution and module import
if __file__:
    project_root = Path(__file__).resolve().parent.parent
else:
    # Fallback if __file__ is not available
    project_root = Path.cwd()

# Ensure project root is in Python path
project_root_str = str(project_root)
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)

from src.exception import CustomException

def save_object_to_pkl(file_path,obj):  
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
            
    except Exception as e:
        raise CustomException(e,sys)