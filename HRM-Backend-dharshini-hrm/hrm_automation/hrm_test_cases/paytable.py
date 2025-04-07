import time
import unittest
import logging
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

# Simplified Logger Configuration
logger = logging.getLogger("Pay table Report")
if not logger.handlers:
    logging.basicConfig(
        filename='hrm_log.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger.propagate = False


class paytable_report(BasePage, unittest.TestCase):
    """Pay table Report Module for HRM Automation."""
    _log_once = False  # Class-level flag to prevent duplicate logs

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logger

    def paytable(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,700)")
        time.sleep(1)
        self.click(Locators.PAY_TABLE_CARD)
        time.sleep(5)

        self.dropdown_click(Locators.PAYTABLE_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYTABLE_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYTABLE_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYTABLE_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.PAYTABLE_RESET)
        time.sleep(2)

        # Log only once
        if not paytable_report._log_once:
            self.logger.info('Pay table Report Page is Working Fine')
            paytable_report._log_once = True
