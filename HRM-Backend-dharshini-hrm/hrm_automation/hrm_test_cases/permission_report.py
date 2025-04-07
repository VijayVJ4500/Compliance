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


class Permission_Report(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Permission Report")

    def permission(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.PERMISSION_CARD)
        time.sleep(5)
        self.click(Locators.PERMISSION_FREQ)
        time.sleep(2)
        self.click(Locators.PERMISSION_HOUR)
        time.sleep(2)
        self.enter_text(Locators.PERMISSION_START, '01-12-2024')
        time.sleep(2)
        self.enter_text(Locators.PERMISSION_END, '30-12-2024')
        time.sleep(2)
        self.dropdown_click(Locators.PERMISSION_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PERMISSION_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PERMISSION_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PERMISSION_IDCARD, 1)
        time.sleep(2)

        self.click(Locators.PERMISSION_RESET)
        time.sleep(2)
        self.click(Locators.PERMISSION_EXCEL)
        time.sleep(2)
        self.logger.info('Permission Report Page is Working Fine')
        time.sleep(2)






