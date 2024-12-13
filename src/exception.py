import sys
import os

# Add the root directory of the project to the module search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.logger import logging








# Function to capture the error details
def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Extract traceback information
    file_name = exc_tb.tb_frame.f_code.co_filename  # Get the filename of the script
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class (Exception) constructor
        self.error_message = error_message_details(error_message, error_detail)
        
    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0

    except Exception as e:
        logging.info('Divide by zero')
        raise CustomException(e,sys)


    
















