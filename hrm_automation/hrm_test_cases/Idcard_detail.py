import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging
from logger_file import logger
import hrm_automation.logger_file

# # Configure logger

logger.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(file_handler)


class Idcard(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = hrm_automation.logger_file.get_logger("Idcard Detail")

    def idcard_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.IDCARD_DETAIL_CARD)
        time.sleep(5)

    def download_idcard(self):
        # self.click(Locators.IDCARD_CURRENT_BUTTON)
        # time.sleep(2)
        self.dropdown_click(Locators.IDCARD_BAND, 1)
        time.sleep(2)
        self.dropdown_click(Locators.IDCARD_DEPT, 1)
        time.sleep(2)
        self.click(Locators.IDCARD_RESET)
        time.sleep(2)
        self.logger.info('Idcard page fiters are working fine')
        time.sleep(2)

        self.click(Locators.IDCARD_VIEW)
        time.sleep(2)
        self.click(Locators.IDCARD_FLIP)
        time.sleep(2)
        self.click(Locators.IDCARD_VIEW_VIEW)
        time.sleep(2)
        self.click(Locators.IDCARD_FLIPVIEW)
        time.sleep(2)
        self.click(Locators.IDCARD_CLOSE)
        time.sleep(2)
        self.logger.info('Idcard Preview is Shown')
        time.sleep(7)

        # self.click(Locators.IDCARD_CHECK1)
        # time.sleep(2)
        self.click(Locators.IDCARD_DOWNLOAD)
        time.sleep(2)
        self.logger.info('1st Idcard downloaded successfully')
        time.sleep(2)

        self.click(Locators.IDCARD_ALLCHECK)
        time.sleep(2)
        self.click(Locators.ICARD_BULKDOWN)
        time.sleep(2)
        self.logger.info('All idcards are downloaded successfully')
        time.sleep(2)

    def idcard_page(self):
        self.idcard_tab()
        self.download_idcard()
