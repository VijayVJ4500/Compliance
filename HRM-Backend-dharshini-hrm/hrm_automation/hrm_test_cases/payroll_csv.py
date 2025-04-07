import time
import unittest
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver import driver
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
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
class pay_csv_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def pay_csv(self):

        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAYROLL_CSV_CARD)
        time.sleep(1)

        #checking the cancel button
        self.click(Locators.PAYCSV_DOWNLOAD)
        time.sleep(1)
        self.click(Locators.PAYCSV_CANCEL)
        time.sleep(1)
        self.click(Locators.PAYCSV_DOWNLOAD)
        time.sleep(1)
        #download the sample excel
        self.dropdown_click(Locators.PAYCSV_COMP_TYPE,1)
        time.sleep(1)
        self.click(Locators.PAYCSV_COMP)
        time.sleep(1)
        self.click(Locators.PAYCSV_COMP)
        time.sleep(1)
        self.click(Locators.PAYCSV_DOWNLOAD_EXCEL)
        time.sleep(1)

        self.click(Locators.PAYCSV_UPLOAD)
        time.sleep(1)
        self.click(Locators.PAYCSVUPLOAD_EARNING_RADIO)
        time.sleep(1)

        earning_path = "D:\ssl\HRM-Backend\hrm_automation\earning_csv.csv"
        self.file_upload(Locators.PAYCSV_EARNING_FILE_UPLOAD, earning_path)
        time.sleep(1)

        self.click(Locators.PAYCSVUPLOAD_UPLOAD_BT)
        time.sleep(1)
        logger.info("Earning Uploaded successfully")
        time.sleep(1)

        self.click(Locators.PAYCSV_UPLOAD)
        time.sleep(1)
        self.click(Locators.PAYCSVUPLOAD_DEDUCTION_RADIO)
        time.sleep(1)

        self.click(Locators.PAYCSVUPLOAD_DEDUCTION_RADIO)
        time.sleep(1)

        deduction_path = "D:\\ssl\\HRM-Backend\\hrm_automation\\deduction.csv"
        self.file_upload(Locators.PAYCSV_EARNING_FILE_UPLOAD, deduction_path)
        time.sleep(1)
        self.click(Locators.PAYCSVUPLOAD_UPLOAD_BT)
        time.sleep(1)
        logger.info("Deduction Uploaded successfully")
        time.sleep(1)

        try:
            # Wait for the Generate button to be clickable
            generate_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(Locators.PAYCSV_GENERATE)
            )
            generate_button.click()
            logger.info("Earning and Deduction both CSV upload Generated successfully")

        except (TimeoutException, ElementClickInterceptedException):
            # If Generate button is not clickable, click Cancel button
            logger.warning("Earning and Deduction both not Get Uploaded")
            self.click(Locators.PAYCSVUPLOAD_CANCEL)
            print("Earning and Deduction both not Get Uploaded")







