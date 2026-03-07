import os
import pickle
import sys

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
from src.MlProject.exception import CustomException
from src.MlProject.logger import logger


#data_transformation
def save_obj(file_path,obj):

  try:
      file_dir=os.path.dirname(file_path)
      os.makedirs(file_dir,exist_ok=True)

      with open(file_path ,"wb") as file_obj:
       pickle.dump(obj,file_obj)
  except Exception as e:
    raise CustomException(e,sys)



# model evaluation
def model_evaluation(X_train,y_train,X_test,y_test,models,params) :
   report={}

   for i in range(len(list(models.values()))):
      model= list(models.values())[i]
      param=params[list(models.keys())[i]]

      gs=GridSearchCV(model,param,cv=3)
      gs.fit(X_train,y_train)

      model.set_params(**gs.best_params_)     
      model.fit(X_train,y_train)

      y_train_pred=model.predict(X_train)
      y_test_pred=model.predict(X_test)

      #r2 score
      train_score=r2_score(y_train,y_train_pred)
      test_score=r2_score(y_test,y_test_pred)

      report[list(models.keys())[i]]=test_score

      return report
   
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
