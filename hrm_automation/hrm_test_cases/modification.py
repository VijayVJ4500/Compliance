import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

from hrm_automation.logger_file import get_logger


class modify(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Approval Modification")

    def approve_tab(self):
        time.sleep(1)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        self.click(Locators.APPROVAL_MODIFY_CARD)
        time.sleep(6)

    def leave_app(self):
        # self.click(Locators.AP_LEAVE_RADIO)
        # time.sleep(1)
        # self.click(Locators.AP_LEAVE_REJECT)
        # time.sleep(3)
        self.click(Locators.AP_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.AP_THIS_MONTH)
        time.sleep(3)
        # self.click(Locators.AP_SEARCH)
        # time.sleep(3)
        self.click(Locators.AM_CHECK1)
        time.sleep(1)
        self.click(Locators.AP_LEAVE_REJECT)
        time.sleep(3)
        self.logger.info("Leave Rejected successfully")

    def od_app(self):
        self.click(Locators.AP_OD_RADIO)
        time.sleep(2)
        # self.click(Locators.AP_OD_REJECT)
        # time.sleep(2)
        self.click(Locators.AP_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.AP_THIS_MONTH)
        time.sleep(1)
        # self.click(Locators.AP_SEARCH)
        # time.sleep(3)
        self.click(Locators.AM_OD_CHECK1)
        time.sleep(1)
        self.click(Locators.AP_OD_REJECT)
        time.sleep(1)
        self.logger.info("Onduty Rejected successfully")

    def modify_page(self):
        self.approve_tab()
        self.leave_app()
        self.od_app()
