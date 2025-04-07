import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import logging
from hrm_automation.logger_file import get_logger
# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)
# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)


class define_bulk_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Define Pay in Bulk")

    def define_pay_bulk(self):

        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.DEFINE_PAY_BULK_CARD)
        time.sleep(1)
        self.click(Locators.DEFINE_BULK_CTC)
        time.sleep(5)
        self.dropdown_click(Locators.DEFINE_BULK_DESIGNATION, 1)
        time.sleep(3)
        self.dropdown_click(Locators.DEFINE_BULK_DEPARTMENT, 1)
        time.sleep(1)
        self.enter_text(Locators.DEFINE_BULK_IDCARD, "KEERTHI")
        time.sleep(1)
        self.click(Locators.DEFINE_BULK_RESET)
        time.sleep(1)
        self.dropdown_click(Locators.DEFINE_BULK_TEMPLATE, 1)
        time.sleep(1)
        self.click(Locators.DEFINE_BULK_ASSIGN)
        time.sleep(1)
        self.driver.switch_to.alert.accept()  # for the alert messages actions there is method called "switched to.alert". for the ok-> "accept" for cancel -> "dismiss"
        time.sleep(2)
        self.click(Locators.DEFINE_CHECK1)
        time.sleep(3)

        self.dropdown_click(Locators.DEFINE_BULK_TEMPLATE, 1)
        time.sleep(1)
        self.click(Locators.DEFINE_BULK_ASSIGN)
        time.sleep(1)
        # driver = self.driver  # Ensure driver is correctly assigned
        # time.sleep(2)
        # EARNING_1 = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[5]/div[1]/div[1]/input[1]')
        # EARNING_1.click()
        # # Simulate pressing the "up" arrow key
        # EARNING_1.send_keys(Keys.ARROW_UP)
        #
        # # Wait for the page to reflect changes (if necessary)
        # time.sleep(2)
        #
        # # Fetch the updated value of the number input field
        # updated_value = EARNING_1.get_attribute('value')
        # time.sleep(2)
        #
        # print(f"Updated value: {updated_value}")
        # self.click(Locators.DEFINE_ASSIGN_BT)
        self.logger.info("Template Assigned successfully for all Employees")
