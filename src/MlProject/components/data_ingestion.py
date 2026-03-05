import os
import sys
from pathlib import Path
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import pandas as pd
from src.MlProject.exception import CustomException
from src.MlProject.logger import logger

@dataclass
class DataIngestionConfig:
   # where to save the data
   raw_data_path: str=os.path.join('artifacts','raw.csv')
   train_data_path:str=os.path.join('artifacts','train.csv')
   test_data_path:str=os.path.join('artifacts','test.csv')

class DataIngestion:
   def __init__(self): 
      self.ingesion_config =DataIngestionConfig()  

   def initiate_data_ingestion(self):   
      try:
     
         df=pd.read_csv("notebook/data/stud.csv")
         logger.info(f"reading data successfully.")

         os.makedirs(os.path.dirname(self.ingesion_config.raw_data_path),exist_ok=True)
         df.to_csv(self.ingesion_config.raw_data_path)

         train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

         train_set.to_csv(self.ingesion_config.train_data_path)
         test_set.to_csv(self.ingesion_config.test_data_path)

         logger.info("Data Ingestion completed")

         return (self.ingesion_config.train_data_path,
                 self.ingesion_config.test_data_path)


      except Exception as e:
         raise CustomException(e,sys)