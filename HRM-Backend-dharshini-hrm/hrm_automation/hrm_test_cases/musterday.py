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


class muster(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Musterday Report")

    def musterday(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.MUSTER_DAY_CARD)
        time.sleep(5)
        self.dropdown_click(Locators.MUSTERDAY_IDCARD,1)
        time.sleep(1)
        # self.enter_text(Locators.MUSTERDAY_START,'11-11-2024')
        # time.sleep(1)
        # self.enter_text(Locators.MUSTERDAY_END, '30-01-2025')
        # time.sleep(1)
        # self.click(Locators.MUSTERDAY_GENERATE)
        # time.sleep(2)
        self.click(Locators.MUSTERDAY_COLLAPSE)
        time.sleep(2)
        self.click(Locators.MUSTERDAY_EXPAND)
        time.sleep(2)
        self.click(Locators.MUSTERDAY_RESET)
        time.sleep(2)
        self.click(Locators.MUSTERDAY_EXCEL)
        time.sleep(2)
        self.logger.info('Muster Report with all details Downloaded Successfully')
        time.sleep(1)







