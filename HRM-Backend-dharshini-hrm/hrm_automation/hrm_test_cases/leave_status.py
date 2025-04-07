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


class leave_status(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Leave Status")

    def leavestatus(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.LEAVE_STATUS_CARD)
        time.sleep(5)
        # self.dropdown_click(Locators.LT_DEPARTMENT,1)
        # time.sleep(2)
        self.dropdown_click(Locators.LT_DESIGNATION, 1)
        time.sleep(2)
        self.click(Locators.LT_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.LT_THIS_MONTH)
        time.sleep(2)
        self.click(Locators.LT_RESET)
        time.sleep(2)
        self.click(Locators.LT_LEAVESELECT)
        time.sleep(2)
        self.click(Locators.LT_REMAINING_LEAVE)
        time.sleep(2)
        self.click(Locators.LT_CLOSE_BT)
        time.sleep(2)
        self.logger.info('Leave status Page is Working Fine')
        time.sleep(2)







