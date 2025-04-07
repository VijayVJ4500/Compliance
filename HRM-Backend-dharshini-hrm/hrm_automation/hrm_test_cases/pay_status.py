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
class pay_status_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def pay_status(self):

        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAY_STATUS_CARD)
        time.sleep(1)
        #CHECKING THE CANCEL BUTTON FUNCTIONALITY
        self.click(Locators.PAY_STS_SENT_APP)
        time.sleep(1)
        self.click(Locators.PAY_STS_CANCEL_BT)
        time.sleep(1)
        #CHECKING THE SENT TO APPROVE FUNCTIONALITY
        self.click(Locators.PAY_STS_SENT_APP)
        time.sleep(1)
        self.click(Locators.PAY_STS_PROCEED_BT)
        time.sleep(1)
        #CHECKING THE APPROVE FUNCTIONALITY
        self.click(Locators.PAY_STS_APP)
        time.sleep(1)
        self.click(Locators.PAY_STS_PROCEED_BT)
        time.sleep(1)
        # CHECKING THE REJECT FUNCTIONALITY
        self.click(Locators.PAY_STS_REJECT)
        time.sleep(1)
        self.click(Locators.PAY_STS_PROCEED_BT)
        time.sleep(1)
        # CHECKING THE RECALL FUNCTIONALITY
        self.click(Locators.PAY_STS_RECALL)
        time.sleep(1)
        self.click(Locators.PAY_STS_PROCEED_BT)
        time.sleep(1)
        # CHECKING THE LOCK FUNCTIONALITY
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAY_STS_LOCK)
        time.sleep(2)
        self.click(Locators.PAY_STS_PROCEED_BT)
        time.sleep(1)
        # CHECKING THE VIEW FUNCTIONALITY
        self.click(Locators.PAY_STS_VIEW)
        time.sleep(1)
        #CHECKING THE EXCEL DOWNLOADING OR NOT
        self.click(Locators.PAY_STS_EXCEL)
        time.sleep(1)
        logger.info("Excel downloaded successfully in pay status page")
        time.sleep(1)






