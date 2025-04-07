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


class Employee_report(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Employee Report")

    def employee_report_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.EMPLOYEE_REPORT_CARD)
        time.sleep(5)

    def download_rep(self):

        self.dropdown_click(Locators.EMP_REP_CAT,1)
        time.sleep(2)
        self.dropdown_click(Locators.EMP_REP_DEPT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.EMP_REP_DESG, 1)
        time.sleep(2)
        self.click(Locators.EMP_REP_RESET)
        time.sleep(2)
        self.click(Locators.EMP_REP_EXCEL)
        time.sleep(1)
        self.logger.info('Employee Report Downloaded Successfully')
        time.sleep(1)
        self.click(Locators.EMP_REP_PERSONAL)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(5)
        self.click(Locators.EMP_REP_JOB)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.click(Locators.EMP_REP_SOCAIL)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(1)
        self.click(Locators.EMP_REP_EXCEL)
        time.sleep(1)
        self.logger.info('Employee Report with all details Downloaded Successfully')
        time.sleep(1)


    def employee_report_page(self):
        self.employee_report_tab()
        self.download_rep()
