import time
import unittest
import logging
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

# Simplified Logger Configuration
logger = logging.getLogger("Payrol log")
if not logger.handlers:
    logging.basicConfig(
        filename='hrm_log.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger.propagate = False


class Payrollog_report(BasePage, unittest.TestCase):
    """Payrol log Page for HRM Automation."""
    _log_once = False  # Class-level flag to prevent duplicate logs

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logger

    def payroll_data(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAYROLL_LOG_CARD)
        time.sleep(5)
        self.click(Locators.PAYLOG_EXCEL)
        time.sleep(1)
        self.click(Locators.PAYLOG_FILTER)
        time.sleep(1)
        self.click(Locators.PAYLOG_THISMONTH)
        time.sleep(1)
        self.dropdown_click(Locators.PAYLOG_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYLOG_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYLOG_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.PAYLOG_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.PAYLOG_RESET)
        time.sleep(2)

        # Log only once
        if not Payrollog_report._log_once:
            self.logger.info('Payroll log Page is Working Fine')
            Payrollog_report._log_once = True
