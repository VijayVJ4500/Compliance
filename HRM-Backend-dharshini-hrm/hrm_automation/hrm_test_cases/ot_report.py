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


class OT_Report(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("OT Report")

    def ot(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.OT_REPORT_CARD)
        time.sleep(5)
        self.click(Locators.OT_FREQ)
        time.sleep(2)
        self.click(Locators.OT_HOUR)
        time.sleep(2)
        self.enter_text(Locators.OT_START, '01-11-2024')
        time.sleep(2)
        self.enter_text(Locators.OT_END, '30-12-2024')
        time.sleep(2)
        self.dropdown_click(Locators.OT_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.OT_DEPARTMENT,1)
        time.sleep(2)
        self.dropdown_click(Locators.OT_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.OT_IDCARD, 1)
        time.sleep(2)

        self.click(Locators.OT_RESET)
        time.sleep(2)
        self.click(Locators.OT_EXCEL)
        time.sleep(2)
        self.logger.info('Ot Report Page is Working Fine')
        time.sleep(2)







