import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators

from hrm_automation.logger_file import get_logger


class Rawdata(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Raw data")

    def rawdata_tab(self):
        time.sleep(1)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.ATT_RAWDATA_CARD)
        time.sleep(6)

    def filters(self):
        self.dropdown_click(Locators.RAWDATA_IDCARD, 1)
        time.sleep(2)
        self.click(Locators.RAWDATA_FILTER)
        time.sleep(2)
        self.click(Locators.RAWDATA_THISMONTH)
        time.sleep(2)
        self.dropdown_click(Locators.RAWDATA_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.RAWDATA_DEPARTMENT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.RAWDATA_DESIGNATION, 1)
        time.sleep(2)
        self.logger.info("Rawdata page filter is working")
        time.sleep(3)
        self.click(Locators.RAWDATA_RESET)
        time.sleep(2)
        self.click(Locators.RAWDATA_EXCEL)
        time.sleep(1)
        self.logger.info("Rawdata Has been Downloaded successfully for the filtered date")

    def rawdata_page(self):
        self.rawdata_tab()
        self.filters()
