import logging
import os
from datetime import datetime

#log file
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# log path
log_dir_path=os.path.join(os.getcwd(),"logs")

# log dir creating
os.makedirs(log_dir_path,exist_ok=True)

log_file_path=os.path.join(log_dir_path,log_file)



logging.basicConfig(
  filename=log_file_path,
  format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
  level=logging.INFO
)

logger = logging.getLogger(__name__)