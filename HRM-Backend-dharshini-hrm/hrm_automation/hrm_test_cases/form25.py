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


class form25(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("form25")

    def form25(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.FORM25_CARD)
        time.sleep(5)
        self.enter_text(Locators.FORM25_MONTH, "jan")
        time.sleep(2)
        self.dropdown_click(Locators.FORM25_CATEGORY, 1)
        time.sleep(2)
        self.dropdown_click(Locators.FORM25_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.FORM25_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.FORM25_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.FORM25_PDF)
        time.sleep(2)
        self.click(Locators.FORM25_RESET)
        time.sleep(2)
        self.logger.info('form25  Page is Working Fine')
        time.sleep(2)
