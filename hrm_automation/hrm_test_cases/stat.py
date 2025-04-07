import time
import unittest
import logging
from selenium.webdriver.chrome.options import Options
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Stat(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Statuatory Forms")

    def scroll_to_bottom(self):
        # Scroll to the bottom of the page using JavaScript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def stat_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.STATUATORY_FORMS_CARD)
        time.sleep(2)

    def download_stat(self):
        # Select checkboxes
        self.click(Locators.STAT_CHECKALL)
        time.sleep(2)
        self.click(Locators.STAT_CHECK1)
        time.sleep(2)
        self.click(Locators.STAT_PRM_TAMIL)
        time.sleep(2)
        self.click(Locators.STAT_SEC_HIN)
        time.sleep(2)

        # Scroll and generate forms
        self.driver.execute_script("window.scrollBy(0,350)")
        time.sleep(1)
        self.scroll_to_bottom()
        time.sleep(1)
        self.click(Locators.STAT_GEN)
        time.sleep(2)
        self.logger.info('Statuatory Forms Downloaded Successfully')

        # Ensure the browser is configured to save PDFs automatically
        # This configuration should ideally be set when initializing the driver
        prefs = {
            "plugins.always_open_pdf_externally": True,
            "download.default_directory": r"C:\Users\pjeya\Downloads",  # Set your desired download directory
            "download.prompt_for_download": False
        }
        if hasattr(self.driver, 'options') and isinstance(self.driver.options, Options):
            self.driver.options.add_experimental_option("prefs", prefs)
        else:
            self.logger.warning("Browser options not configured to save PDFs automatically.")

        # Wait for the PDF to download
        time.sleep(5)  # Adjust as necessary

    def stat_page(self):
        self.stat_tab()
        self.download_stat()
