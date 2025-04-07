import time
import unittest
import logging
from selenium.webdriver.chrome.options import Options
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


class Late_entry(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Late Entry Report")

    def lateentry(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.LATEENTRY_CARD)
        time.sleep(3)
        self.click(Locators.LE_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.LE_THIS_MONTH)
        time.sleep(2)
        self.dropdown_click(Locators.LE_DEPARTMENT,1)
        time.sleep(2)
        self.dropdown_click(Locators.LE_DESIGNATION, 1)
        time.sleep(2)
        # self.click(Locators.LE_EARLY_OUT)
        # time.sleep(2)
        self.click(Locators.LE_RESET)
        time.sleep(2)
        self.logger.info('Late Entry Page is Working Fine')
        time.sleep(2)








