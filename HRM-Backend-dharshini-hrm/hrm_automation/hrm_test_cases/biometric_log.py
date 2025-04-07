import time
import unittest
import logging

from selenium.webdriver import ActionChains, Keys

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

# Simplified Logger Configuration
logger = logging.getLogger("Biometric log")
if not logger.handlers:
    logging.basicConfig(
        filename='hrm_log.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger.propagate = False


class BiometricHistory_report(BasePage, unittest.TestCase):
    """Biometric Module for HRM Automation."""
    _log_once = False  # Class-level flag to prevent duplicate logs

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logger

    def biodata(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.BIOMETRIC_HISTORY_CARD)
        time.sleep(10)

        self.click(Locators.BIOHIS_FILTER)
        self.click(Locators.BIOHIS_THISMONTH)
        time.sleep(1)
        self.dropdown_click(Locators.BIOHIS_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.BIOHIS_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.BIOHIS_DESIGNATION, 1)
        time.sleep(2)
        self.dropdown_click(Locators.BIOHIS_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.BIOHIS_EXCEL)
        time.sleep(1)
        self.click(Locators.BIOHIS_RESET)
        time.sleep(2)

        # Log only once
        if not BiometricHistory_report._log_once:
            self.logger.info('Biometric log Page is Working Fine')
            BiometricHistory_report._log_once = True
