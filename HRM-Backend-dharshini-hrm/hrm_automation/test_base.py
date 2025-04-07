import configparser
import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from .logger_file import get_logger

config = configparser.ConfigParser()
config.read("hrm_automation/settings.conf")


class TestBase(unittest.TestCase):
    """
    Base test class to initiate web driver in one place and reuse it everywhere.
    """
    
    def setUp(self) -> None:
        # Initialize logger for the test class
        self.logger = get_logger(self.__class__.__name__)
        self.logger.info(f"Starting test setup for {self._testMethodName}")
        """
        Setup google driver
        :return:
        """
        if 'hrm' not in config:
            raise ValueError("Missing 'hrm' section in config.ini!")

        if 'CHROME_DRIVER_LOCATION' not in config['hrm']:
            raise ValueError("Missing 'CHROME_DRIVER_LOCATION' in hrm section!")

        chrome_service = Service(config['hrm']['CHROME_DRIVER_LOCATION'])

        
        chrome_options = webdriver.ChromeOptions()
        chrome_service = Service(config['hrm']['CHROME_DRIVER_LOCATION'])
        self.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.driver.get(config['hrm']['TEST_URL'])
        self.driver.maximize_window()
        self.logger.info(f"Browser initialized and navigated to {config['hrm']['TEST_URL']}")


    #Edge driver
        # self.driver = webdriver.Edge(executable_path=config['hrm']['EDGE_DRIVER_LOCATION'])
        # self.driver.get(config['hrm']['TEST_URL'])
        # self.driver.maximize_window()
   #Firefox driver
        # firefox_options = webdriver.FirefoxOptions()
        # self.driver = webdriver.Firefox(executable_path=config['hrm']['GECKO_DRIVER_LOCATION'],
        #                                 firefox_options=firefox_options)
        # self.driver.get(config['hrm']['TEST_URL'])`
        # self.driver.maximize_window()

    def tearDown(self):
        self.logger.info(f"Tearing down test {self._testMethodName}")
        # Cleanup driver to solve memory issues
        self.driver.close()
        self.driver.quit()
        self.logger.info("Browser closed and driver quit successfully")
class TestBaseFireFox(unittest.TestCase):

    def setUp(self) -> None:  # Fixed method name from Setup to setUp
        # Initialize logger for the test class
        self.logger = get_logger(f"{self.__class__.__name__}")
        self.logger.info(f"Starting Firefox test setup for {self._testMethodName}")
        """
               Setup google driver
               :return:
               """
        firefox_options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(executable_path=config['hrm']['GECKO_DRIVER_LOCATION'],
                                        firefox_options=firefox_options)
        self.driver.get(config['hrm']['TEST_URL'])
        self.driver.maximize_window()
        self.logger.info(f"Firefox browser initialized and navigated to {config['hrm']['TEST_URL']}")

    def tearDown(self):
        self.logger.info(f"Tearing down Firefox test {self._testMethodName}")
        # Cleanup driver to solve memory issues
        self.driver.close()
        self.driver.quit()
        self.logger.info("Firefox browser closed and driver quit successfully")