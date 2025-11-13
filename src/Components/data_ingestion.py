# writing a code in this file to read the data from various sources 
import os 
import pandas as pd
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Add project root to Python path - handle both direct execution and module import
if __file__:
    project_root = Path(__file__).resolve().parent.parent.parent
else:
    # Fallback if __file__ is not available
    project_root = Path.cwd()

# Ensure project root is in Python path
project_root_str = str(project_root)
if project_root_str not in sys.path:
    sys.path.insert(0, project_root_str)

# Import src modules after adding project root to path
from src.exception import CustomException
from src.logger import logging
from src.Components.data_transformation import DataTransformation 
from src.Components.data_transformation import DataTransformationConfig
from src.Components.model_trainer import ModelTrainerConfig,ModelTrainer

@dataclass
class DataIngestionClass:
    train_data_class : str = os.path.join('artifacts','train.csv')
    test_data_class : str = os.path.join('artifacts','test.csv')
    raw_data_class : str = os.path.join('artifacts','raw.csv')
    
    
class DataIngestion:
    def __init__(self):
        self.ingestion = DataIngestionClass()
    
    def initiate_data_ingestion(self):
        
        logging.info("Entered the data ingestion method or component")
        try:
            csv_path = os.path.join(str(project_root), 'src', 'Notebook', 'StudentsPerformance.csv')
            df = pd.read_csv(csv_path)
            logging.info("Read the dataset from source ")
            
            os.makedirs(os.path.dirname(self.ingestion.train_data_class), exist_ok=True)
            
            df.to_csv(self.ingestion.raw_data_class,index=False,header=True)
            logging.info("Train Test Split")
            train,test = train_test_split(df,test_size=0.2,random_state=42)
            train.to_csv(self.ingestion.train_data_class,index=False,header=True)
            test.to_csv(self.ingestion.test_data_class,index=False,header=True)
            
            logging.info("Ingestion of data completed")
            
            return(self.ingestion.train_data_class,
                   self.ingestion.test_data_class)
        
        except Exception as e:
            raise CustomException(e,sys)
            
            
if __name__ == "__main__": 
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))