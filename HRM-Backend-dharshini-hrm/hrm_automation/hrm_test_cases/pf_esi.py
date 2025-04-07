import time
import unittest

from selenium.webdriver.chrome.options import Options
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger
import logging
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


class PF_ESI(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("PF ESI Report")

    def pfesi(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.PFESI_REPORT_CARD)
        time.sleep(5)
        self.dropdown_click(Locators.PFESI_BAND,1)
        time.sleep(2)
        self.dropdown_click(Locators.PFESI_DEPT, 1)
        time.sleep(2)
        # self.click(Locators.ESI_TOGGLE)
        # time.sleep(2)
        self.click(Locators.PFESI_RESET)
        time.sleep(2)
        self.click(Locators.LT_RESET)
        time.sleep(2)
        self.logger.info('PF ESI Report Page is Working Fine')
        time.sleep(2)







