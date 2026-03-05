import os
from src.MlProject.exception import CustomException
from src.MlProject.logger import logger
import pickle
import sys


#data_transformation
def save_obj(file_path,obj):

  try:
      file_dir=os.path.dirname(file_path)
      os.makedirs(file_dir,exist_ok=True)

      with open(file_path ,"wb") as file_obj:
       pickle.dump(obj,file_obj)
  except Exception as e:
    raise CustomException(e,sys)



