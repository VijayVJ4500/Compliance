import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger
from logger import logger
class approve(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Approval Process")

    def approve_tab(self):
        time.sleep(1)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        self.click(Locators.APPROVAL_PROCESS_CARD)
        time.sleep(6)

    def leave_app(self):
        self.click(Locators.AP_LEAVE_RADIO)
        time.sleep(1)
        # self.click(Locators.AP_DECLARE)
        # time.sleep(1)
        # self.driver.switch_to.alert.accept()  # for the alert messages actions there is method called "switched to.alert". for the ok-> "accept" for cancel -> "dismiss"
        # time.sleep(2)

    #leave approve without declare leave
        self.click(Locators.AP_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.AP_THIS_MONTH)
        time.sleep(3)
        # self.click(Locators.AP_SEARCH)
        # time.sleep(3)
        self.click(Locators.AP_CHECK1)
        time.sleep(1)
        self.click(Locators.AP_DECLARE)
        time.sleep(1)
        self.dropdown_click(Locators.AP_LEAVE_NAME,1)
        time.sleep(1)
        self.click(Locators.AP_LEAVE_SUBMIT)
        time.sleep(3)
        self.logger.info("Leave Approved successfully")
    def od_app(self):
        self.click(Locators.AP_OD_RADIO)
        time.sleep(2)
        # od approve
        self.click(Locators.AP_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.AP_THIS_MONTH)
        time.sleep(2)
        # self.click(Locators.AP_SEARCH)
        # time.sleep(3)
        self.click(Locators.AP_OD_CHECK1)
        time.sleep(1)
        self.click(Locators.AP_APPROVE_OD)
        time.sleep(1)
        self.logger.info("Onduty Approved successfully")

    def approve_page(self):
        self.approve_tab()
        self.leave_app()
        self.od_app()
