import time
import unittest
import logging

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Contleave(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger('Continuous Leave')

    def continouse_leave(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.CONT_LEAVE_CARD)
        time.sleep(2)
        self.click(Locators.CONT_DATE)
        time.sleep(2)
        self.click(Locators.CONT_7DAYS)
        time.sleep(2)
        self.click(Locators.CONT_TERMINATE)
        time.sleep(2)
        self.dropdown_click(Locators.CONT_REASON, 1)
        time.sleep(2)
        self.click(Locators.CONT_SUBMIT)
        time.sleep(2)
        self.logger.info('Employee has been terminated successfully in Continuous leave')
        time.sleep(1)
