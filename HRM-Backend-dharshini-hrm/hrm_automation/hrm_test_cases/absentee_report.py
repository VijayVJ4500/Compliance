import time
import unittest
import logging
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

# Simplified Logger Configuration
logger = logging.getLogger("Absentee Report")
if not logger.handlers:
    logging.basicConfig(
        filename='hrm_log.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger.propagate = False


class Absentees_report(BasePage, unittest.TestCase):
    """Absentee Report Module for HRM Automation."""
    _log_once = False  # Class-level flag to prevent duplicate logs

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logger

    def absentees(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.ABSENTEE_REPORT_CARD)
        time.sleep(5)
        self.click(Locators.ABSREP_EXCEL)
        time.sleep(5)
        self.enter_text(Locators.ABSREP_DATE1, "19-12-2024")
        time.sleep(2)
        self.dropdown_click(Locators.ABSREP_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.ABSREP_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.ABSREP_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.ABSREP_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.ABSREP_RESET)
        time.sleep(2)

        # Log only once
        if not Absentees_report._log_once:
            self.logger.info('Absentee Report Page is Working Fine')
            Absentees_report._log_once = True
