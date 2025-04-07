import random
import string
import time
from ..headers import AppTestCase
import unittest
from faker import Faker
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation import headers
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from hrm_automation.logger_file import get_logger
import logging
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


class sequence(BasePage, unittest.TestCase):
    """
    Sequence operations for the HRM system.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Sequence")

    def is_alert_present(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return True
        except TimeoutException:
            return False

    def sequence_tab(self):
        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.SEQ_CARD)
        time.sleep(2)

        # Scroll and edit operations
        table_container = self.driver.find_element(By.CSS_SELECTOR, ".ag-body-horizontal-scroll-viewport")
        actions = ActionChains(self.driver)
        actions.click_and_hold(table_container).move_by_offset(600, 0).release().perform()
        time.sleep(1)

        # Test cancel operation
        self.click(Locators.SEQUENCE_EDIT)
        time.sleep(1)
        self.click(Locators.SEQUENCE_CANCEL)
        time.sleep(2)
        self.logger.info("Cancel button clicked successfully")

        # Edit the  sequence
        self.click(Locators.SEQUENCE_EDIT)
        time.sleep(1)
         # API call to update Sequence reason
        url = "https://ipssapi.techgenzi.com/autogenerate_hrm/5279/"
        payload = {
    "tx_view_id": "GRN",
    "zeropadding": "5",
    "prefix": "GR n-",
    "description": "DESC",
    "lastno": "0"
}

        response = requests.patch(url, json=payload,headers=AppTestCase.get_headers())
        if response.status_code == 200:
            self.logger.info(f"Sequence Updated Successfully")
        else:
            self.logger.error(f"Failed to Update Sequence: {response.status_code}")

        self.click(Locators.SEQUENCE_CANCEL)

        # Test clearing fields and submitting
        self.click(Locators.SEQUENCE_EDIT)
        time.sleep(1)

        self.clear(Locators.SEQUENCE_PREFIX)
        time.sleep(1)
        self.clear(Locators.SEQUENCE_DESCRIPTION)
        time.sleep(1)
        self.clear(Locators.SEQUENE_NO_DIGIT)
        time.sleep(1)
        self.clear(Locators.SEQUENCE_LAST_DIGIT)
        time.sleep(1)       
        self.enter_text(Locators.SEQUENCE_PREFIX, "WORKER")
        time.sleep(1)
        self.enter_text(Locators.SEQUENCE_DESCRIPTION, "DESCRIPTION")
        time.sleep(1)
        self.enter_text(Locators.SEQUENE_NO_DIGIT, "4")
        time.sleep(1)
        self.enter_text(Locators.SEQUENCE_LAST_DIGIT, "3")
        time.sleep(1)
        self.click(Locators.SEQUENCE_SUBMIT)

        if self.is_alert_present():
            alert = Alert(self.driver)
            logger.info(f"Handling alert: {alert.text}")
            alert.accept()
            self.click(Locators.SEQUENCE_CANCEL)
            self.click(Locators.SEQUENCE_ADD)
            time.sleep(1)
        else:
            self.click(Locators.SEQUENCE_ADD)

        # Checking cancel button

        self.click(Locators.SEQUENCE_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")

        # Check submission of empty fields
        self.click(Locators.SEQUENCE_ADD)
        time.sleep(1)
        self.click(Locators.SEQUENCE_SUBMIT)
        time.sleep(1)
        if self.is_element_present(("xpath", "(//button[normalize-space()='Submit'])[1]")):
            self.logger.warning("Prefix is not entered, so not submitted. Test passed.")  
            
        else:
            self.logger.warning("Prefix is not entered, so not submitted. Test passed.")

        time.sleep(1)



        # Checking allready existed prefix is adding again or not 
        self.dropdown_click(Locators.SEQUENCE_BAND, 1)
        time.sleep(1)
        self.enter_text(Locators.SEQUENCE_PREFIX, "WORKERS")
        time.sleep(1)
        self.enter_text(Locators.SEQUENCE_DESCRIPTION, "DESCRIPTION")
        time.sleep(1)
        self.enter_text(Locators.SEQUENE_NO_DIGIT, "4")
        time.sleep(1)
        self.enter_text(Locators.SEQUENCE_LAST_DIGIT, "3")
        time.sleep(1)
        self.click(Locators.SEQUENCE_SUBMIT)

        if self.is_alert_present():
            alert = Alert(self.driver)
            logger.info(f"Handling alert: {alert.text}")
            alert.accept()
            self.click(Locators.SEQUENCE_CANCEL)
        else:
            logger.error("Allready existed Prefix is Adding Again")

        self.click(Locators.SEQUENCE_ADD)
        time.sleep(1)
        fake = Faker()

        # Generate a random three-letter sequence
        sequence_prefix = ''.join(random.choices(string.ascii_uppercase, k=3))

        print(sequence_prefix)
         # API call to update Sequence reason
        url = "https://ipssapi.techgenzi.com/autogenerate_hrm/"
        payload = {
    "tx_view_id": "GRN",
    "zeropadding": "5",
    "prefix": sequence_prefix,
    "description": "DESC",
    "lastno": "0"
}

        response = requests.post(url, json=payload, headers=AppTestCase.get_headers())
        if response.status_code == 200:
            self.logger.info(f"Sequence Created Successfully")
        else:
            self.logger.error(f"Failed to Create Sequence: {response.status_code}")

        self.click(Locators.SEQUENCE_CANCEL)


