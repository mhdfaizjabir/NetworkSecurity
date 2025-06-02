import sys


from Network_Security.logging import logger 

class NetworkSecurityException(Exception):
    """Base class for all network security exceptions."""
    def __init__(self,error_message,error_details : sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"{self.error_message} occurred in file {self.file_name} at line number {self.line_number}"
if __name__ == "__main__":
    try:
        logger.logging.info("ENTER THE TRY BLOCK")
        
        a=1/0
        print("this wont be preinted because of the exception")
    except Exception as e:
        raise NetworkSecurityException(e,sys) 