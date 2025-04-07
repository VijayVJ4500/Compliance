import time
import unittest
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from hrm_automation import headers
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging

from hrm_automation.logger_file import get_logger

# Configure logger
logger = logging.getLogger('hrm_logger')
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(file_handler)


class PayrollConfiguration(BasePage, unittest.TestCase):
    """
    Payroll Configuration Automation
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Pay Components")

    def check_response(self, url, data, request_type="post"):
        """
        Helper method to check API response for given URL and data.
        """


        try:
            if request_type.lower() == "post":
                response = requests.post(url, json=data, headers=headers.get_headers())
            elif request_type.lower() == "patch":
                response = requests.patch(url, json=data, headers=headers.get_headers())
            else:
                self.logger.error("Invalid request type specified.")
                return None
            return response.status_code
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def con_tab(self):
        """
        Navigate to the Payroll Configuration Tab.
        """
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.PAY_COMP_CARD)
        time.sleep(2)

    def default_add(self):
        """
        Add a default earning in payroll configuration.
        """
        self.click(Locators.PAY_COMP_DEFAULT_TAB)
        time.sleep(1)
        self.click(Locators.DEFAULT_CANCEL)
        time.sleep(1)
        self.click(Locators.DEFAULT_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/earning/"
        data = {
    "earning_name": "Allowance 1",
    "description": "DESCRIPTION",
    "frequency": "regular_in_ctc",
    "pay_type": "fixed",
    "min_value": "10",
    "max_value": "50",
    "is_standard": False,
    "ctc_based": False,
    "calculated_by": [],
    "flexi_pay": False
}

        try:
            response = requests.post(url, json=data, headers=headers.get_headers())

            logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info("Default Earning created successfully")
            elif response.status_code == 409:
                self.logger.info(f"Default Earning already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Default Earning creation failed: Response code {response.status_code}")
            self.click(Locators.DEFAULT_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def default_edit(self):
        """
        Edit a default earning in payroll configuration.
        """
        self.click(Locators.DEFAULT_EDIT_BT)
        time.sleep(1)
        self.click(Locators.DEFAULT_CANCEL)
        time.sleep(1)
        self.click(Locators.DEFAULT_EDIT_BT)
        time.sleep(1)
        self.click(Locators.DEFAULT_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/earning/12"
        data = {
    "earning_name": "Allowance 2",
    "description": "DESCRIPTION",
    "frequency": "regular_in_ctc",
    "pay_type": "fixed",
    "min_value": "10",
    "max_value": "50",
    "is_standard": False,
    "ctc_based": False,
    "calculated_by": [],
    "flexi_pay": False
}

        status_code = self.check_response(url, data, request_type="patch")

        if status_code == 200:
            self.logger.info("Default earning edited successfully")
        elif status_code == 409:
            self.logger.warning("Default earning already exists")
        else:
            self.logger.error(f"Default earning edit failed with status code {status_code}")
            self.click(Locators.DEFAULT_CANCEL)

    def test_check_response_invalid_url(self):
        config = PayrollConfiguration(driver=None)
        url = "http://this-does-not-exist-123456.com"
        headers = {}
        method = "post"

        status_code = config.check_response(url, headers, method)
        print(f"DEBUG: URL={url}, Method={method}, Received status code={status_code}")

        self.assertIsNone(status_code, "Status code should be None for invalid URL.")

    def test_default_edit_invalid_data(self):
        """
        Test editing with invalid data.
        Ensures that an attempt to edit a payroll configuration with invalid or empty data fails.
        """
        # Navigate to the Default Earnings tab


        # Initialize the configuration object
        config = PayrollConfiguration(driver=None)

        # Define the invalid data
        invalid_data = {
            "earning_name": "",
            "description": "",
            "frequency": "",
            "pay_type": "",
            "min_value": "",
            "max_value": ""
        }
        self.logger.debug(f"Attempting to edit with invalid data: {invalid_data}")

        # Make the API call
        response_code = config.check_response(
            "https://ipssapi.techgenzi.com/payroll_config/earning/99",
            invalid_data,
            "patch"
        )

        # Log the response code and assert the result
        if response_code != 200:
            self.logger.info(f"Invalid data edit correctly rejected. Response Code: {response_code}")
        else:
            self.logger.error(f"Invalid data edit incorrectly succeeded. Response Code: {response_code}")

        self.assertNotEqual(response_code, 200, "Edit should not succeed with invalid data.")
        time.sleep(1)
        self.click(Locators.PAY_COMP_DEFAULT_TAB)
        time.sleep(1)
     #Earning

    def earning_add(self):
        """
        Add a  earning in payroll configuration.
        """

        self.click(Locators.PAY_COMP_EARNING_TAB)
        time.sleep(1)
        self.click(Locators.EARG_CANCEL)
        time.sleep(1)
        self.click(Locators.EARG_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/earning/"
        data = {
            "earning_name": "Allowance 1",
            "description": "DESCRIPTION",
            "frequency": "regular_in_ctc",
            "pay_type": "fixed",
            "min_value": "10",
            "max_value": "50",
            "is_standard": False,
            "ctc_based": False,
            "calculated_by": []

        }

        try:
            response = requests.post(url, json=data, headers=headers.get_headers())

            self.logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info(" Earning created successfully")
            elif response.status_code == 409:
                self.logger.info(f" Earning already exists: Response code {response.status_code}")
            else:
                self.logger.error(f" Earning creation failed: Response code {response.status_code}")
            self.click(Locators.EARG_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def earning_edit(self):
        """
        Edit a  earning in payroll configuration.
        """
        self.driver.execute_script("window.scrollBy(0,200)")
        time.sleep(2)
        self.click(Locators.EARG_EDIT)
        time.sleep(1)
        self.click(Locators.EARG_CANCEL)
        time.sleep(1)
        self.click(Locators.EARG_EDIT)
        time.sleep(1)
        self.click(Locators.EARG_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/earning/165"
        data = {
            "earning_name": "Allowance 2",
            "description": "DESCRIPTION",
            "frequency": "regular_in_ctc",
            "pay_type": "fixed",
            "min_value": "10",
            "max_value": "50",
            "is_standard": False,
            "ctc_based": False,
            "calculated_by": []
        }

        status_code = self.check_response(url, data, request_type="patch")

        if status_code == 200:
            self.logger.info("Earning edited successfully")
        elif status_code == 409:
            self.logger.warning("Earning already exists")
        else:
            self.logger.error(f"Earning edit failed with status code {status_code}")
            self.click(Locators.EARG_CANCEL)

    def test_check_response_invalid_url_earning(self):
        """
        Test API response for invalid URL.
        """
        config = PayrollConfiguration(driver=None)
        status_code = config.check_response("https://invalid-url.com", {}, "post")
        self.assertIsNone(status_code, "Status code should be None for invalid URL.")

    def test_default_edit_invalid_data_earning(self):
        """
        Test editing with invalid data.
        Ensures that an attempt to edit a payroll configuration with invalid or empty data fails.
        """
        # Navigate to the Default Earnings tab
        self.click(Locators.EARG_EDIT)
        time.sleep(1)
        # Initialize the configuration object
        config = PayrollConfiguration(driver=None)

        # Define the invalid data
        invalid_data = {
            "earning_name": "",
            "description": "",
            "frequency": "",
            "pay_type": "",
            "min_value": "",
            "max_value": ""
        }
        self.logger.debug(f"Attempting to edit with invalid data: {invalid_data}")

        # Make the API call
        response_code = config.check_response(
            "https://ipssapi.techgenzi.com/payroll_config/earning/99",
            invalid_data,
            "patch"
        )

        # Log the response code and assert the result
        if response_code != 200:
            self.logger.info(f"Invalid data edit correctly rejected. Response Code: {response_code}")
        else:
            self.logger.error(f"Invalid data edit incorrectly succeeded. Response Code: {response_code}")

        self.assertNotEqual(response_code, 200, "Edit should not succeed with invalid data.")
        self.click(Locators.PAY_COMP_EARNING_TAB)
        time.sleep(1)

    def deduction_tab(self):
        self.click(Locators.PAY_COMP_DEDUCTION_TAB)
        time.sleep(1)
#DEDUCTION

    def deduction_add(self):
        """
        Add a  earning in payroll configuration.
        """

        self.click(Locators.DEDC_CANCEL)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        self.click(Locators.DEDC_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/deduction/"
        data = {
    "deduction_name": "Deduction  for esi",
    "description": "DESC",
    "frequency": "regular_not_in_ctc",
    "pay_type": "percentage",
    "min_value": "10",
    "max_value": "100",
    "is_standard": False,
    "ctc_based": True,
    "calculated_by": []
}

        try:
            response = requests.post(url, json=data, headers=headers.get_headers())

            self.logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info(" Deduction created successfully")
            elif response.status_code == 409:
                self.logger.info(f" Deduction already exists: Response code {response.status_code}")
            else:
                self.logger.error(f" Deduction creation failed: Response code {response.status_code}")
            self.click(Locators.DEDC_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def deduction_edit(self):
        """
        Edit a  earning in payroll configuration.
        """

        self.driver.execute_script("window.scrollBy(0,200)")
        time.sleep(2)
        self.click(Locators.DEDC_EDIT)
        time.sleep(1)
        # self.click(Locators.DEDC_CANCEL)
        # time.sleep(1)
        # self.click(Locators.DEDC_EDIT)
        # time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-300)")
        time.sleep(2)
        self.click(Locators.DEDC_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/deduction/43"
        data = {
    "deduction_name": "Deduction limit with  100 for regular",
    "description": "DESCRIPTION",
    "frequency": "regular_not_in_ctc",
    "pay_type": "fixed",
    "min_value": 10,
    "max_value": 100,
    "is_standard": False,
    "ctc_based": False,
    "calculated_by": []
}

        status_code = self.check_response(url, data, request_type="patch")

        if status_code == 200:
            self.logger.info("Deduction edited successfully")
        elif status_code == 409:
            self.logger.warning("Deduction already exists")
        else:
            self.logger.error(f"Deduction edit failed with status code {status_code}")
            self.click(Locators.DEDC_CANCEL)

    def test_check_response_invalid_url_deduction(self):
        """
        Test API response for invalid URL.
        """
        config = PayrollConfiguration(driver=None)
        status_code = config.check_response("https://invalid-url.com", {}, "post")
        self.assertIsNone(status_code, "Status code should be None for invalid URL.")

    def test_default_edit_invalid_data_deduction(self):
        """
        Test editing with invalid data.
        Ensures that an attempt to edit a payroll configuration with invalid or empty data fails.
        """
        # Navigate to the Default Earnings tab
        self.click(Locators.DEDC_EDIT)
        time.sleep(1)
        # Initialize the configuration object
        config = PayrollConfiguration(driver=None)

        # Define the invalid data
        invalid_data = {
    "deduction_name": "",
    "description": "",
    "frequency": "",
    "pay_type": "",
    "min_value": "",
    "max_value": ""
}
        self.logger.debug(f"Attempting to edit with invalid data: {invalid_data}")

        # Make the API call
        response_code = config.check_response(
            "https://ipssapi.techgenzi.com/payroll_config/earning/43",
            invalid_data,
            "patch"
        )

        # Log the response code and assert the result
        if response_code != 200:
            self.logger.info(f"Invalid data edit correctly rejected. Response Code: {response_code}")
        else:
            self.logger.error(f"Invalid data edit incorrectly succeeded. Response Code: {response_code}")

        # self.assertNotEqual(response_code, 200, "Edit should not succeed with invalid data.")
        self.driver.execute_script("window.scrollBy(0,-400)")
        time.sleep(2)
        self.click(Locators.PAY_COMP_DEDUCTION_TAB)
        time.sleep(1)


    # STANDARD DEDUCTION
    def std_deduction_tab(self):
        self.click(Locators.PAY_COMP_STD_DEDUCTION_TAB)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(2)
    def std_deduction_add(self):
        """
        Add a  standard deduction in payroll configuration.
        """

        self.click(Locators.STD_CANCEL)
        time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,400)")
        # time.sleep(2)
        self.click(Locators.STD_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll_config/standard_deduction_config/"
        data = {
    "component_name": "PF FSUND",
    "component_value": 234,
    "percent_of": None,
    "code": "ESI",
    "salary_limit": 15000,
    "is_percent": True,
    "min_value": 2510,
    "max_value": 100000,
    "calculated_by": []
}

        try:
            response = requests.post(url, json=data, headers=headers.get_headers())

            self.logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info("Standard Deduction created successfully")
            elif response.status_code == 409:
                self.logger.info(f" Standard Deduction already exists: Response code {response.status_code}")
            else:
                self.logger.error(f" Standard Deduction creation failed: Response code {response.status_code}")
            self.click(Locators.STD_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def std_deduction_edit(self):
        """
        Add a  standard in payroll configuration.
        """

        self.click(Locators.STD_CANCEL)
        time.sleep(1)

        self.click(Locators.STD_SAVE)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,600)")
        time.sleep(2)
        # Scroll and edit operations
        table_container = self.driver.find_element(By.CSS_SELECTOR, ".ag-body-horizontal-scroll-viewport")
        actions = ActionChains(self.driver)
        actions.click_and_hold(table_container).move_by_offset(600, 0).release().perform()
        time.sleep(1)
        self.click(Locators.STD_EDIT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-300)")
        time.sleep(1)
        url = "https://ipssapi.techgenzi.com/payroll_config/standard_deduction_config/45"
        data = {
    "component_name": "Employee32",
    "component_value": 234,
    "percent_of": None,
    "code": "ESI",
    "salary_limit": 15000,
    "is_percent": True,
    "min_value": 2510,
    "max_value": 100000,
    "calculated_by": []
}

        try:
            response = requests.patch(url, json=data, headers=headers.get_headers())


            if response.status_code == 200:
                self.logger.info(" Standard Deduction Updated successfully")
            elif response.status_code == 409:
                self.logger.info(f" Standard Deduction already exists: Response code {response.status_code}")
            else:
                self.logger.error(f" Standard Updation creation failed: Response code {response.status_code}")
            self.click(Locators.STD_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")


    def configure_pay(self):
        """
        End-to-end configuration test.
        """
        self.con_tab()
        self.default_add()
        self.default_edit()
        self.test_check_response_invalid_url()
        self.test_default_edit_invalid_data()
        self.earning_add()
        self.earning_edit()
        # self.test_check_response_invalid_url_earning()
        self.test_default_edit_invalid_data_earning()
        self.deduction_tab()
        self.deduction_add()
        self.deduction_edit()
        # self.test_check_response_invalid_url_deduction()
        self.test_default_edit_invalid_data_deduction()
        self.std_deduction_tab()
        self.std_deduction_add()
        self.std_deduction_edit()
