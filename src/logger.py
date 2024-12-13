import logging
import os
from datetime import datetime

# Generate the log file name with the current datetime
LOG_FILE = f"log_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s %(name)s - %(message)s",
    level=logging.INFO,
)

