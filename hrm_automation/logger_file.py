import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(logger_name):
    """
    Configures and returns a logger instance with a specified name.
    Ensures no duplicate handlers are added and properly closes previous handlers.

    :param logger_name: The name of the logger to configure.
    :return: Configured logger instance.
    """
    logger = logging.getLogger(logger_name)

    # Close and remove existing handlers before adding a new one
    if logger.hasHandlers():
        for handler in logger.handlers[:]:
            handler.close()  # Explicitly close file handlers
            logger.removeHandler(handler)  # Remove handler safely

    # Define log directory and file path
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(log_dir, "hrm_log.log")

    # Create log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)

    # Define formatter
    formatter = logging.Formatter(
        fmt='Date and Time: %(asctime)s - %(levelname)s - %(name)s - Line number: %(lineno)d : %(message)s',
        datefmt='%d-%b-%y %I:%M:%S %p'
    )

    # Create rotating file handler (10MB per file, keep 5 backup files)
    file_handler = RotatingFileHandler(
        log_file,
        mode='a',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # Add the new handler
    logger.addHandler(file_handler)

    # Set logger level
    logger.setLevel(logging.DEBUG)

    # Propagate to root logger
    logger.propagate = False

    return logger

# Suppress third-party library logs globally
logging.getLogger("faker").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("selenium").setLevel(logging.WARNING)
