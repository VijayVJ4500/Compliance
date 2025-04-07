import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging
from logger import logger


# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(file_handler)



class resign(BasePage, unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)

    def resign_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,700)")
        # time.sleep(1)
        self.click(Locators.RESIGNATION_CARD)
        time.sleep(10)

    def termination(self):
        self.click(Locators.RESIG_DEPT_FIL)
        time.sleep(1)
        self.click(Locators.RESIG_DES_FIL)
        time.sleep(8)
        self.dropdown_click(Locators.RESIGN_ID_FIL, 3)
        time.sleep(1)
        self.click(Locators.RESIG_APPLY_FIL)
        time.sleep(1)
        self.enter_text(Locators.RESIG_DOL, "15-03-2024")
        time.sleep(1)
        self.click(Locators.RESIG_1CHECK)
        time.sleep(2)
        self.click(Locators.RESIG_TER_BT)
        time.sleep(2)
        self.dropdown_click(Locators.RESIG_TERM_REASON, 1)
        time.sleep(1)
        self.click(Locators.RESIGN_TERM_SUBMIT)
        time.sleep(1)
        logger.info("Employee has been Terminated Sucessfully")



    def resignation(self):
        self.click(Locators.RESIG_DEPT_FIL)
        time.sleep(1)
        self.click(Locators.RESIG_DES_FIL)
        time.sleep(1)
        self.dropdown_click(Locators.RESIGN_ID_FIL, 14)
        time.sleep(1)
        self.click(Locators.RESIG_APPLY_FIL)
        time.sleep(1)
        self.enter_text(Locators.RESIG_DOL, "15-03-2024")
        time.sleep(4)
        self.click(Locators.RESIG_1CHECK)
        time.sleep(4)
        self.click(Locators.RESIG_RESIG_BT)
        time.sleep(4)
        self.dropdown_click(Locators.RESIGN_RESIGN_REASON,1)
        time.sleep(1)
        self.click(Locators.RESIGN_RESIGN_SUBMIT)
        time.sleep(3)
        logger.info("Employee has been Resigned Sucessfully")

    def resign_page(self):
        self.resign_tab()
        self.termination()
        self.resignation()