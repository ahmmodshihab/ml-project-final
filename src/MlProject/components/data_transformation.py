import os
import sys
from dataclasses import dataclass

from src.MlProject.logger import logger
from src.MlProject.exception import CustomException
from src.MlProject.utils import save_obj

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path:str=os.path.join('artifacts','preprosesor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    try:
        def get_data_transformation_obj(self):

         cata_features=["gender","race_ethnicity","parental-level_of_education","lunch","test_preparation_score"]
         num_feature=["writing_score",'reading_score']

         cata_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy="most_frequent")),
                                       ("encoder",OneHotEncoder()),
                                       ("scalling",StandardScaler(with_mean=False))])

         num_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy="median")),
                                      ("scalling",StandardScaler())])   

        # transforming Column
         preprocessor=ColumnTransformer(transformers=[("cata_pipeline",cata_pipeline,cata_features),
                                                       ("num_pipeline",num_pipeline,num_feature)])


         return preprocessor
    except Exception as e:
        raise CustomException(e,sys)

    
    try:
      def initiate_data_transformation(self,train_path,test_path):
        
        train_df=pd.read_csv(train_path)
        test_df= pd.read_csv(test_path)
        
        logger.info(f"train & test data reading completed")

        target_column='math_score'

         # dividing independent and dependent features of train
        input_train_df=train_df.drop(columns=[target_column],axis=1)
        target_train_df=train_df[target_column]
 
         # dividing independent and dependent features of test
        input_test_df=test_df.drop(columns=[target_column],axis=1)
        target_test_df=test_df[target_column]


        logger.info("Applying preprocessor on training and test data")

        # applying preprocessor
        preprocessor_obj=self.get_data_transformation_obj()
        
        input_feature_train_transformed=preprocessor_obj.fit_transform(input_train_df)
        input_feature_test_transformed=preprocessor_obj.transform(input_test_df)

       # concatination
        logger.info("concatination of input features and target feature")

        train_arr=np.c_[input_feature_train_transformed,np.array(target_train_df)] 
        test_arr=np.c_[input_feature_test_transformed,np.array(target_test_df)]    

      # saving prepeosser
        save_obj(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessor_obj) 
        logger.info("saved preprocessor object")

        return(train_arr,
               test_arr,
               self.data_transformation_config.preprocessor_obj_file_path)                        
    except Exception as e:
       raise CustomException(e,sys)
       
