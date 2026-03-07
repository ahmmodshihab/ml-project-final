if __name__=="__main__":
   

   # checking data_ingestion.py
   from src.MlProject.components.data_ingestion import DataIngestion
   data_ingestion_obj=DataIngestion()
   train_path, test_path = data_ingestion_obj.initiate_data_ingestion()


   #checking data_transformation.py
   from src.MlProject.components.data_transformation import DataTransformation
   data_transformation_obj=DataTransformation()
   train_arr,test_arr,_=data_transformation_obj.initiate_data_transformation(train_path, test_path)
   
   # checking model_trainer.py
   from src.MlProject.components.model_trainer import ModelTrainer
   model_trainer_obj=ModelTrainer()
   r2_score = model_trainer_obj.initiate_model_trainer(train_arr,test_arr)
   print(r2_score)

   # checking prediction_pipeline.py
   from src.MlProject.pipelines.prediction_pipeline import CustomData,PredictPipeline
   