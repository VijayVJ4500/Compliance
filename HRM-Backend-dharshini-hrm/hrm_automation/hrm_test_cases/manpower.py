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


class Manpower_Report(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Manpower Report")

    def manpower(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.click(Locators.MANPOWER_CARD)
        time.sleep(3)
        self.enter_text(Locators.MAN_DATE,'12-12-2024')
        time.sleep(2)
        self.dropdown_click(Locators.MAN_DEPT, 1)
        time.sleep(2)
        self.click(Locators.MAN_RESET)
        time.sleep(2)
        self.click(Locators.MAN_PICTORIAL_VIEW)
        time.sleep(2)
        self.click(Locators.MAN_PIC_BAND)
        time.sleep(2)
        self.click(Locators.MAN_PIC_DEPT)
        time.sleep(2)
        self.click(Locators.MAN_PIC_DESG)
        time.sleep(2)
        self.click(Locators.MAN_PIC_CLOSE)
        time.sleep(2)
        self.logger.info('Man Power Report Page is Working Fine')
        time.sleep(2)







