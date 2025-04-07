import time
import unittest
import requests
from faker import Faker

from hrm_automation import headers
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging

from logger import logger

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
class template_page(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Pay Template")


    def check_response(self, url, data, request_type="post"):

        if request_type == "post":
            response = requests.post(url, json=data, headers=headers.get_headers())
        else:
            response = requests.patch(url, json=data, headers=headers.get_headers())

        return response.status_code



    def template_tab(self):
        """
        Navigates to the template tab by clicking on appropriate elements.
        """
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.PAY_TEMP_CARD)
        time.sleep(1)

    def daily_emp(self):
        """
        Performs actions to create a CTC wage template and logs success or error messages.
        """
        # try:
        self.click(Locators.TEMPL_CREATE_BT)
        time.sleep(1)
        self.scroll_down(200)
        self.click(Locators.TEMPL_CANCEL)
        time.sleep(1)
        self.click(Locators.TEMPL_CREATE_BT)
        time.sleep(1)
        self.scroll_down(200)
        self.click(Locators.TEMPL_SAVE)
        time.sleep(3)
        # self.click(Locators.TEMPL_NAME)
        # time.sleep(1)
        # self.enter_text(Locators.TEMPL_NAME, "managers TEMPLATE")
        # time.sleep(3)
        # self.dropdown_click(Locators.TEMPL_TYPE, 1)
        # time.sleep(1)
        # self.enter_text(Locators.TEMPL_DESC, "CTCs WAGE TEMPLATE DESCRIPTION")
        # time.sleep(1)
        # self.click(Locators.TEMPL_REG_EAR_BT)
        # time.sleep(1)
        # self.click(Locators.TEMPL_REGULAR_1)
        # time.sleep(1)
        # self.click(Locators.TEMPL_REG_EAR_BT)
        # time.sleep(1)
        # self.click(Locators.TEMPL_REG_NOT_CTC_BT)
        # time.sleep(1)
        # self.click(Locators.TEMPL_REG_NOT_CTC_BT)
        # time.sleep(1)
        # self.click(Locators.TEMPL_ADD_EARN)
        # time.sleep(1)
        # self.click(Locators.TEMPL_ADD_EARN)
        # time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,300)")
        # time.sleep(2)
        # self.click(Locators.TEMPL_REG_DED)
        # time.sleep(1)
        # self.click(Locators.TEMPL_REG_DED)
        # time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,300)")
        # time.sleep(2)
        # self.click(Locators.TEMPL_OCC_DED)
        # time.sleep(1)
        # self.click(Locators.TEMPL_OCC_DED)
        # time.sleep(1)
        # self.dropdown_click(Locators.TEMPL_TYPE1, 2)
        # time.sleep(1)
        # self.click(Locators.TEMPL_CALC_BY_DW)
        # time.sleep(1)

            # self.click(Locators.TEMP_SAVE)
            # time.sleep(1)

            # # Mock API response to capture status code
            # response = requests.post(
            #     "https://ipssapi.techgenzi.com/payroll/org_template/",
            #     headers={
            #         "Content-Type": "application/json",
            #         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTczNTUzMDI1NSwianRpIjoiNTk0NDBmMzEtZTQ5OC00OGJjLWI4NmItYjIyNjVkNWFlMDQ2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VybmFtZSI6Iml0aG9kQHBnYy5jb20iLCJjb250cm9saWQiOjEsInByb2plY3RpZCI6IlRJUExQR0MiLCJmaW55ciI6IjIzLTI0IiwiZmlueXJfaWQiOjE2NDk2ODIyMDQ3NzgsImNvbXBjb2RlIjoiR0pJIiwiZGlzcGxheSI6IkdKIElOTk9WQVRJT05TIEFORCBURVhUSUxFIE5FVFdPUksgUFJJVkFURSBMSU1JVEVEIiwiY29tcG5hbWUiOiJHSiBJTk5PVkFUSU9OUyBBTkQgVEVYVElMRSBORVRXT1JLIFBSSVZBVEUgTElNSVRFRCIsImJicmFuY2giOiJTSVZBS0FTSSIsImFkZHJlc3MiOiIxLzQwNyxEUCAtMiwzJjQgU0lEQ08gSU5EVVNUUklBTCBFU1RBVEUsIFNVTEFLS0FSQUkiLCJnc3RubyI6IjMzQUFDQ0c2MTM2QzFaNCIsImNvbXBhbnlfaWQiOjE1MzkxNDc2NDk3MDUsInVzZXJpZCI6MTU3MTY1NjQ5NDM3MSwiZW1wX2lkIjpudWxsLCJ1c2VyX3JvbGUiOiJBZG1pbiJ9LCJuYmYiOjE3MzU1MzAyNTUsImV4cCI6MTczNTYxNjY1NX0.iteAsJ2n594_hCMfnqt-HDTMPSQt4kbVhRmoKC_eOvU"
            #     })
            #
            # logger.debug(f"Response Status Code: {response.status_code}")
            #
            # if response.status_code == 200:
            #     logger.info("Template created successfully")
            # elif response.status_code == 409:
            #     logger.info(f"Template already exists: Response code is {response.status_code}")
            #     self.click(Locators.TEMPL_CANCEL)
            # else:
            #     logger.error(f"Template creation failed: Response code is {response.status_code}")
            #     self.click(Locators.TEMPL_CANCEL)

        # except Exception as e:
        #     logger.error(f"An error occurred during template creation: {e}")
        # finally:
        #     # self.click(Locators.TEMPL_CANCEL)
        #     time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll/org_template/"
        data = {
    "template_name": "TAILORS TEMPLATE",
    "template_type": "daily_wages",
    "description": "CTCs WAGE TEMPLATE DESCRIPTION"
}

        try:
            response = requests.post(url, json=data, headers=headers.get_headers())

            self.logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info("Template created successfully")
            elif response.status_code == 409:
                self.logger.info(f"Template already exists: Response code {response.status_code}")
                self.driver.execute_script("window.scrollBy(0,400)")
                time.sleep(1)
                self.scroll_down(200)
                self.click(Locators.TEMPL_CANCEL)
            else:
                self.logger.error(f"Template creation failed: Response code {response.status_code}")
                self.driver.execute_script("window.scrollBy(0,400)")
                time.sleep(1)
                self.scroll_down(200)
                self.click(Locators.TEMPL_CANCEL)

        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def edit_temp(self):
        """
        Creates a CTC wage template and handles API interaction with proper logging.
        """

    # Open and Cancel View (to reset state)
        time.sleep(4)
        self.click(Locators.TEMPL_VIEW_BT)
        time.sleep(1)
        self.scroll_down(200)
        self.click(Locators.TEMPL_CANCEL)
        time.sleep(1)

        # Reopen and start editing template
        self.click(Locators.TEMPL_VIEW_BT)
        time.sleep(1)
        self.scroll_down(200)
        # self.click(Locators.TEMPL_SAVE)
        # time.sleep(7)
        # self.click(Locators.TEMPL_VIEW_BT)
        # time.sleep(1)
        # Update Template Name and Description
        self.click(Locators.TEMPL_NAME)
        time.sleep(1)
        # self.clear(Locators.TEMPL_NAME)
        # time.sleep(1)
        # self.enter_text(Locators.TEMPL_NAME, "staffs TEMPLATE")
        # time.sleep(1)
        # self.dropdown_click(Locators.TEMPL_TYPE, 1)
        # time.sleep(1)
        # self.enter_text(Locators.TEMPL_DESC, "CTCs WAGE TEMPLATE DESCRIPTION")
        self.click(Locators.TEMPL_REG_EAR_BT)
        time.sleep(1)
        self.click(Locators.TEMPL_REGULAR_1)
        time.sleep(1)
        self.click(Locators.TEMPL_REG_EAR_BT)
        time.sleep(1)



        # Save Template
        self.scroll_down(200)
        self.click(Locators.TEMPL_SAVE)
        time.sleep(1)

        url = "https://ipssapi.techgenzi.com/payroll/org_template/49"
        data = {
            "template_name": "HELPERS TEMPLATE",
            "template_type": "daily_wages",
            "description": "CTCs WAGE TEMPLATE DESCRIPTION"
        }

        try:
            response = requests.patch(url, json=data, headers=headers.get_headers())

            self.logger.debug(f"Response Status Code: {response.status_code}")
            if response.status_code == 200:
                self.logger.info("Template Updated successfully")
            elif response.status_code == 409:
                self.logger.info(f"Template already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Template updation failed: Response code {response.status_code}")
                self.scroll_down(200)
                self.click(Locators.TEMPL_CANCEL)
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")

    def template(self):

        self.template_tab()
        self.daily_emp()
        self.edit_temp()
