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


class dashboard(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Dashboard Report")

    def scroll_to_bottom(self):
        # Scroll to the bottom of the page using JavaScript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        # Scroll to the top of the page using JavaScript
        self.driver.execute_script("window.scrollTo(0, 0);")
    def dash(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.DASHBOARD_CARD)
        time.sleep(2)
        self.enter_text(Locators.DASHBOARD_DATE,'20-11-2024')
        time.sleep(2)
        self.scroll_to_bottom()
        time.sleep(1)
        self.scroll_to_top()
        time.sleep(1)
        self.click(Locators.DASHBOARD_RESET)
        time.sleep(2)
        self.logger.info('Dashboard is Working Fine')
        time.sleep(1)






