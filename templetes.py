import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

project_name="MlProject"

list_of_files=[
               f"src/{project_name}/__init__.py",
               f"src/{project_name}/components/data_ingestion.py",
               f"src/{project_name}/components/data_transformation.py",
               f"src/{project_name}/components/model_trainer.py",
               f"src/{project_name}/components/model_monitoring.py",
               f"src/{project_name}/pipelines/__init__.py",
               f"src/{project_name}/pipelines/training_pipeline",
               f"src/{project_name}/pipelines/prediction_pipeline",
               f"src/{project_name}/exception",
               f"src/{project_name}/logger",
               f"src/{project_name}/utils.py",
               "app.py",
               "requirements.txt",
               "setup.py",
               "Dockerfile"]
               

for files in list_of_files :
    filepath=Path(files)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
      os.makedirs(filedir,exist_ok=True)
      logger.info(f"file directory {filedir} created.")


    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
       with open(filepath,'w' ) as f:
          pass
       logger.info(f" creating emty file {filename}")  

    else:
       logger.info(f"{filename} file is already exists")   

        






