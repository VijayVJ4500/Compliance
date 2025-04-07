import time
import unittest

from driver import driver

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging

from hrm_automation.logger_file import get_logger

# Configure logger
logger = logging.getLogger('hrm_logger')
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(file_handler)
class pay_generation_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Pay Generation")

    def pay_generation(self):

        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.PAY_GENERATION_CARD)
        time.sleep(1)
        self.click(Locators.PG_GENERATE_PAY_BT)
        time.sleep(1)
        self.dropdown_click(Locators.PG_MONTH,10)
        time.sleep(1)
        self.enter_text(Locators.PG_YEAR,2024)
        time.sleep(1)
        self.click(Locators.PG_GENERATE_PAY_BT)
        time.sleep(3)
        self.click(Locators.PG_CHECK)
        time.sleep(1)
        self.click(Locators.PG_GENERATE_BT)
        time.sleep(1)
        self.click(Locators.PG_EXCEL)
        time.sleep(1)
        self.click(Locators.PG_EXCEL)
        time.sleep(1)
        self.logger.info("Excel downloaded successfully in Pay generation page")


