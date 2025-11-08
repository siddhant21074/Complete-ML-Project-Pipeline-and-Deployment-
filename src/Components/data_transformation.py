import sys 
import numpy as np
import pandas as pd 
import os 
from pathlib import Path
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer ## to create pipeline of encoding
from sklearn.impute import SimpleImputer ## deals with missing values 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

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

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object_to_pkl

@dataclass
class DataTransformationConfig:
    ## this line creates a pkl model file at this path 
    preprocessor_obj_file_path = os.path.join('artifacts',"preprocessor.pkl")  

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation_object(self):
        try:
            numerical_columns=['reading score', 'writing score']
            catergorical_columns=['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']
            
            ## Creating pipeline to process the numnerical columns data
            numerical_columns_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")), # replace the missing value with median of column
                    ("scaler",StandardScaler())
                ]
            )
            Catergorical_columns_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoding",OneHotEncoder())
                ]
            )
            logging.info("Numerical columns standard scaling completed")
            logging.info("Categorical columns encoding completed")
            
            ## this is the execuation of pipeline step by step 
            preprocessor=ColumnTransformer(
                [
                    ("numerical_pipeline",numerical_columns_pipeline,numerical_columns),
                    ("categorical_pipeline",Catergorical_columns_pipeline,catergorical_columns)
                ]
            )
            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Train and Test data completed")
            logging.info("Obtaining preprocessor object")
            
            preprocessing_obj=self.get_data_transformation_object()
            target_column_name="math score"
            numerical_columns=['reading score', 'writing score']
            
            input_feature_train_df=train_df.drop(columns=[target_column_name])
            target_feature_train_df=train_df[target_column_name]
            
            input_feature_test_df=test_df.drop(columns=[target_column_name])
            target_feature_test_df=test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training and testing dataframe")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]
            
            save_object_to_pkl(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)