import inspect
import logging


class GetLogger:

    def get_logger(self):
        logging.basicConfig(filename="compliance_loger.log",
                            format='Date and Time:%(asctime)s - %(levelname)s - %(name)s -Line number:%(lineno)d : %('
                                   'message)s',
                            datefmt='%d-%b-%y %I:%M:%S %p',
                            filemode='a'
                            )

        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        logger.setLevel(logging.DEBUG)
        return logger
