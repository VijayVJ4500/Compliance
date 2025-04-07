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
class pay_slip_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def pay_slip(self):

        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAY_SLIP_CARD)
        time.sleep(1)

#CHECKING THE RESET FUNCTION
        self.enter_text(Locators.PAYSLIP_MONTH,"SEPTEMBER")
        time.sleep(1)
        self.dropdown_click(Locators.PAYSLIP_IDCARD,1)
        time.sleep(1)
        self.click(Locators.PAYSLIP_RESET)
        time.sleep(1)
# CHECKING THE GENERATE FUNCTION
        self.enter_text(Locators.PAYSLIP_MONTH, "SEPTEMBER")
        time.sleep(1)
        self.click(Locators.PAYSLIP_GENERATE)
        time.sleep(1)
        logger.info(" Payslip Generated successfully")

        #CHECKING THE DOWNLOAD FUNCITON

        self.click(Locators.PAYSLIP_DOWNLOAD1)
        time.sleep(1)
        self.click(Locators.PAYSLIP_DOWNLOAD2)
        time.sleep(1)
        logger.info(" Payslip 1&2 is  downloaded successfully")

#CHECKING THE ALERT MESSAGE FOR NOT SELECTING THE EMPLOYEE BUT CLICKING THE DOWNLOAD SELECTED BUTTON

        self.click(Locators.PAYSLIP_DOWNLOAD_SEL)
        time.sleep(1)
        self.click(Locators.PAYSLIP_CLOSE)
        time.sleep(1)
        logger.info("Alert message for not selecting the checkbox but selecting download selected is sucessfull")

#CHECKING THE SELECTED PAYSLIP IS GETTING DOWNLOADING OR NOT
        self.click(Locators.PAYSLIP_CHECK1)
        time.sleep(1)
        self.click(Locators.PAYSLIP_CHECK2)
        time.sleep(1)
        self.click(Locators.PAYSLIP_CHECK3)
        time.sleep(1)
        self.click(Locators.PAYSLIP_DOWNLOAD_SEL)
        time.sleep(1)
        logger.info("The selected payslip downloaded successfully")

#CHECK WHETHER ALL PAYSLIP IS GETTING DOWNLOADING OR NOT

        self.click(Locators.PAYSLIP_DOWNLOAD_ALL)
        time.sleep(1)
        logger.info("All Payslip downloaded successfully")



