import time
import unittest
import requests

from hrm_automation import headers
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging
from logger import logger

from hrm_automation.logger_file import get_logger

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


class Leaveconfig(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Leave Configuration")

    def check_response(self, url, data, request_type="post"):
        headers_data = headers.get_headers()
        if request_type == "post":
            response = requests.post(url, json=data, headers=headers_data)
        else:
            response = requests.patch(url, json=data, headers=headers_data)

        return response.status_code

    def leave_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(2)
        self.click(Locators.LEAVE_CONFG_CARD)
        time.sleep(8)

    def leave_add(self):

        self.click(Locators.LEAVE_ADD_BT)
        time.sleep(3)
        self.click(Locators.LEAVE_CANCEL)
        time.sleep(1)
        self.click(Locators.LEAVE_ADD_BT)
        time.sleep(3)
        self.click(Locators.LEAVE_SUBMIT)
        time.sleep(1)
        self.click(Locators.LEAVE_LOP)
        time.sleep(1)
        self.click(Locators.LEAVE_SUBMIT)
        time.sleep(3)

        url = "https://ipssapi.techgenzi.com/leave_configuration_hrm/"
        try:
            response = requests.post(url, json={
    "leavetype_name": "Maternity leaves",
    "description": None,
    "loss_of_pay": False,
    "abbreviation": "AB",
    "types": "Leave",
    "default": False
}, headers=headers.get_headers())

            if response.status_code == 200:
                self.logger.info("Leave created successfully")
                time.sleep(1)
            elif response.status_code == 409:
                self.logger.info(f"Leave already exists: Response code is {response.status_code}")
                time.sleep(1)
            else:
                logger.error(f"Leave creation failed: Response code is  {response.status_code}")
            self.click(Locators.LEAVE_CANCEL)
            time.sleep(1)
        except requests.RequestException as e:
            logger.error(f"An error occurred: {e}")

    def leave_edit(self):
        self.click(Locators.LEAVE_EDIT_BT)
        time.sleep(3)
        self.click(Locators.LEAVE_CANCEL)
        time.sleep(1)
        self.click(Locators.LEAVE_EDIT_BT)
        time.sleep(3)
        self.clear(Locators.LEAVE_EDIT_NAME)
        time.sleep(1)
        self.click(Locators.LEAVE_SUBMIT)
        time.sleep(1)
        self.enter_text(Locators.LEAVE_NAME, "maternitys leave")
        time.sleep(1)
        self.click(Locators.LEAVE_LOP)
        time.sleep(1)
        self.click(Locators.LEAVE_SUBMIT)
        time.sleep(3)

        url = "https://ipssapi.techgenzi.com/leave_configuration_hrm/840"
        try:
            response = requests.patch(url, json={
                "leavetype_name": "Compensation leave",
                "description": None,
                "loss_of_pay": False,
                "abbreviation": "AB",
                "types": "Leave",
                "default": False
            }, headers=headers.get_headers())

            if response.status_code == 200:
                self.logger.info("Leave Patched successfully")
            elif response.status_code == 409:
                self.logger.info(f"Leave already exists: Response code is {response.status_code}")
            else:
                logger.error(f"Leave updation failed: Response code is  {response.status_code}")
            self.click(Locators.LEAVE_CANCEL)
        except requests.RequestException as e:
            logger.error(f"An error occurred: {e}")
    def holi_radio(self):
        self.click(Locators.LEAVE_HOLIDAY_RADIO)
        time.sleep(1)

    def holi_add(self):


        # Simulate actions for adding a holiday in the UI
        self.click(Locators.ADD_HOLIDAY_BT)
        time.sleep(1)

        self.click(Locators.ADD_HOLIDAY_SUBMIT)
        time.sleep(4)

        # API URL for post request
        url = 'https://ipssapi.techgenzi.com/leave_configuration_hrm/'

        # Prepare request data
        payload = {

  "leavetype_name": "Govert holidays",

  "abbreviation": "string",
  "description": "string",
  "types": "Holiday",
  "leave_days": ["2024-05-05"],
  "default": False,
  "show_in_payslip": False
}

        # Perform the patch request and handle exceptions
        try:
            response = requests.post(url, json=payload, headers=headers.get_headers())

            # Check the response status
            if response.status_code == 200:
                self.logger.info("Holiday created successfully")
            elif response.status_code == 409:
                self.logger.info(f"Holiday already exists. Response code is {response.status_code}")
                self.click(Locators.ADD_HOLIDAY_CANCEL)
            else:
                logger.error(f"Holiday creation failed. Response code is {response.status_code}")
                self.click(Locators.ADD_HOLIDAY_CANCEL)
        except requests.RequestException as e:
            # Log any request exceptions and cancel the operation
            logger.error(f"An error occurred: {e}")
            self.click(Locators.ADD_HOLIDAY_CANCEL)
            time.sleep(3)
    def holi_edit(self):
        self.click(Locators.EDIT_HOLIDAY_BT)
        time.sleep(1)
        self.click(Locators.ADD_HOLIDAY_CANCEL)
        time.sleep(1)
        self.click(Locators.EDIT_HOLIDAY_BT)
        time.sleep(1)
        self.clear(Locators.ADD_HOLIDAY_NAME)
        time.sleep(1)
        self.click(Locators.ADD_HOLIDAY_SUBMIT)
        time.sleep(1)

        # API URL for patch request
        url = 'https://ipssapi.techgenzi.com/leave_configuration_hrm/845'

        # Prepare request data
        payload = {

            "leavetype_name": "Pongal Hoolidys",
            "description": "string",
            "types": "Holiday",
            "leave_days": ["2024-05-05"],
            "default": False,
            "show_in_payslip": False
        }

        # Perform the patch request and handle exceptions
        try:
            response = requests.patch(url, json=payload, headers=headers.get_headers())
            time.sleep(4)
            # Check the response status
            if response.status_code == 200:
                self.logger.info("Holiday Updated successfully")
            elif response.status_code == 409:
                self.logger.info(f"Holiday already exists. Response code is {response.status_code}")
                self.click(Locators.ADD_HOLIDAY_CANCEL)
            else:
                logger.error(f"Holiday Updation failed. Response code is {response.status_code}")
                self.click(Locators.ADD_HOLIDAY_CANCEL)
        except requests.RequestException as e:
            # Log any request exceptions and cancel the operation
            logger.error(f"An error occurred: {e}")
            self.click(Locators.ADD_HOLIDAY_CANCEL)
    def leave_page(self):
        self.leave_tab()
        self.leave_add()
        self.leave_edit()
        self.holi_radio()
        self.holi_add()
        self.holi_edit()
