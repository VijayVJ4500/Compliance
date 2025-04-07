import logging
import random
import time
import unittest
from ..headers import AppTestCase
from faker import Faker
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging

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



class ShiftProvider:
    @staticmethod
    def generate_shift_name():
        shift_prefix = ["Early", "Mid", "Late", "Overnight", "Graveyard"]
        shift_suffix = ["Shift", "Work Period", "Rotation", "Schedule"]
        return f"{fake.random_element(shift_prefix)} {fake.random_element(shift_suffix)}"

fake = Faker()
shift_name = ShiftProvider.generate_shift_name()

class shift(BasePage,unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Shift Configure")

    def shift_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(2)
        self.click(Locators.SHIFT_CARD)
        time.sleep(2)

    def wait_and_click(self, locator):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def wait_and_enter_text(self, locator, text):
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    # def shift_tab(self):
    #         self.wait_and_click(Locators.HOME_SIDEBAR)
    #         self.driver.execute_script("window.scrollBy(0,800)")
    #         self.wait_and_click(Locators.SHIFT_CARD)

    def check_negative_value(self, locator, value, field_name):
            """
            Enter a negative value into a field and check if the form is submitted.
            Log a message if the form accepts the negative value.
            """
            self.wait_and_enter_text(locator, value)
            self.wait_and_click(Locators.SHIFT_SUBMIT)
            # Check for presence of any error message or validation
            if self.is_element_present(Locators.SHIFT_SUBMIT):
                    self.logger.info(f"Negative value '{value}' is being  not accepted in {field_name}")
            else:
                    self.logger.info(f"Negative value '{value}' is being  accepted in {field_name}")

    def shift_add_1(self):
            """
            Test the Shift Add functionality, including checking for negative value acceptance.
            """
            self.wait_and_click(Locators.SHIFT_ADD)

            # Enter valid values first
            self.wait_and_enter_text(Locators.SHIFT_NAME, "Shift with Negative Tests")
            time.sleep(1)
            self.wait_and_enter_text(Locators.SHIFT_START, "11:00")
            time.sleep(1)
            self.wait_and_enter_text(Locators.SHIFT_END, "22:00")
            time.sleep(1)
            # self.wait_and_enter_text(Locators.SHIFT_BREAK, "5")
            # time.sleep(1)
            # self.clear(Locators.SHIFT_BREAK)
            # time.sleep(1)
            # Test negative values for different fields
            self.check_negative_value(Locators.SHIFT_BREAK, "-5", "SHIFT_BREAK")
            time.sleep(1)
            self.click(Locators.SHIFT_GTIME_BEFORE)
            time.sleep(1)
            self.check_negative_value(Locators.SHIFT_START_GRACE, "-15", "SHIFT_START_GRACE")
            time.sleep(1)
            self.check_negative_value(Locators.MIN_SHIFT_MINS, "-150", "MIN_SHIFT_MINS")
            time.sleep(1)
            self.check_negative_value(Locators.HALF_SHIFT_MINS, "-250", "HALF_SHIFT_MINS")
            time.sleep(1)
            self.check_negative_value(Locators.BREAK_OT, "-15", "BREAK_OT")
            time.sleep(1)
            self.check_negative_value(Locators.ALLOW_MIN_1, "-60", "ALLOW_MIN_1")
            time.sleep(1)
            self.check_negative_value(Locators.OT_END_MIN, "-120", "OT_END_MIN")
            time.sleep(1)

            # Cancel the form after testing
            self.wait_and_click(Locators.SHIFT_CANCEL)
            time.sleep(1)

    #ADD THE SHIFT
    def shift_add(self):
#Check the cancel Button whether the data is cancelling or not
        self.click(Locators.SHIFT_ADD)
        time.sleep(1)
        self.click(Locators.SHIFT_CANCEL)
        time.sleep(1)
#check the submit button whether the empty fields are posting or not
        self.click(Locators.SHIFT_ADD)
        time.sleep(1)
        self.click(Locators.SHIFT_SUBMIT)
        time.sleep(1)
        #Add the shift
        shift_name1 = f"Shift {random.randint(5, 10000)}"

        # Enter the shift name dynamically
        self.enter_text(Locators.SHIFT_NAME, shift_name1)
        time.sleep(1)
        # self.click(Locators.SHIFT_DEFAULT)
        # time.sleep(1)
        self.enter_text(Locators.SHIFT_START,"11:00")
        time.sleep(1)
        self.enter_text(Locators.SHIFT_END,"22:00")
        time.sleep(1)
        self.enter_text(Locators.SHIFT_BREAK,"5")
        time.sleep(1)
        self.click(Locators.SHIFT_GTIME_AFTER)
        time.sleep(1)
        self.enter_text(Locators.SHIFT_START_GRACE,"15")
        time.sleep(1)
        self.enter_text(Locators.SHIFT_END_GRACE,"15")
        time.sleep(1)
        self.enter_text(Locators.MIN_SHIFT_MINS,"150")
        time.sleep(1)
        self.enter_text(Locators.HALF_SHIFT_MINS,"250")
        time.sleep(1)
        self.enter_text(Locators.BREAK_OT,"15")
        time.sleep(1)
        self.enter_text(Locators.OT_END_1,"23:50")
        time.sleep(1)
        self.enter_text(Locators.ALLOW_MIN_1,"60")
        time.sleep(1)
        self.enter_text(Locators.OT_END_MIN,"120")
        time.sleep(1)
        self.click(Locators.DEF_OT_SLAB)
        time.sleep(1)
        self.click(Locators.SHIFT_ADD_ROW)
        time.sleep(1)
        self.enter_text(Locators.OT_END_2, "23:50")
        time.sleep(1)
        self.enter_text(Locators.ALLOW_MIN_2, "60")
        time.sleep(1)
        # self.enter_text(Locators.ALLOW_MIN_1,"60")
        # time.sleep(1)
        self.click(Locators.SHIFT_SUBMIT)
        time.sleep(6)

        self.logger.info("All fields and button are working fine")

        self.click(Locators.SHIFT_ADD)
        time.sleep(1)
        shift_name = f"Shift {random.randint(5, 10000)}"
         # Add the Shift
        url = "https://ipssapi.techgenzi.com/shift_configure/shift_mast_hrm/"
        payload = {
    "shift_name": shift_name,
    "shift_start_time": "09:36",
    "shift_end_time": "18:37",
    "shift_break_mins": 5,
    "shift_duration": 541,
    "shift_work_mins": 536,
    "minimum_shift_minutes": 150,
    "halftime_shift_mins": 350,
    "shift_start_grace_time": 5,
    "shift_end_grace_time": "05",
    "break_before_ot": "5",
    "night_shift": False
}
        
        response = requests.post(url, json=payload, headers=AppTestCase.get_headers())
        if response.status_code == 200:
            self.logger.info(f"Shift Created Successfully: {response.status_code}")
        else:
            self.logger.error(f"Failed to Update Shift: {response.status_code}")
        # Scrolls within the popup window to reveal hidden elements or load more content
        # self.driver.popup_scroll()


#  # Scroll and edit operations
#         wait = WebDriverWait(self.driver, 10)
#         popup_window = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiDialogContent-root.css-1ty026z")))

#         # Perform a smaller scroll to avoid out-of-bounds issue
#         actions = ActionChains(self.driver)
#         actions.click_and_hold(popup_window).move_by_offset(0, -200).release().perform()

        # popup = self.driver.find_element(By.CSS_SELECTOR, ".MuiDialogContent-root.css-1ty026z")
        # actions = ActionChains(self.driver)

        # # Define the scroll amount and number of scrolls
        # scroll_amount = 200  # Adjust this value based on the scroll speed/requirement
        # num_scrolls = 10  # 7 is there Adjust the number of scrolls as needed

        # # Perform vertical scrolling on the popup
        # for _ in range(num_scrolls):
        #     actions.move_to_element(popup).click_and_hold().move_by_offset(0, scroll_amount).release().perform()
        #     time.sleep(1)  # Add a delay between scrolls if necessary


        self.click(Locators.SHIFT_CANCEL)

    def shift_edit(self):
        # Click Edit and Clear all the Fields, to check the Mandatory Fields

        self.click(Locators.SHIFT_EDIT)
        time.sleep(1)
        self.clear(Locators.SHIFT_NAME)
        time.sleep(1)
        # self.click(Locators.SHIFT_DEFAULT)
        # time.sleep(1)
        self.clear(Locators.SHIFT_START)
        time.sleep(1)
        self.clear(Locators.SHIFT_END)
        time.sleep(1)
        self.clear(Locators.SHIFT_BREAK)
        time.sleep(1)

        self.clear(Locators.SHIFT_START_GRACE)
        time.sleep(1)
        self.clear(Locators.SHIFT_END_GRACE)
        time.sleep(1)
        self.clear(Locators.MIN_SHIFT_MINS)
        time.sleep(1)
        self.clear(Locators.HALF_SHIFT_MINS)
        time.sleep(1)
        self.click(Locators.SHIFT_SUBMIT)
        time.sleep(6)

#Check the cancel Button

        self.click(Locators.SHIFT_CANCEL)
        time.sleep(1)
#clear the data and click the submit button
        self.click(Locators.SHIFT_EDIT)
        time.sleep(1)
        self.clear(Locators.SHIFT_NAME)
        time.sleep(1)
        self.click(Locators.SHIFT_SUBMIT)
        time.sleep(5)
# Edit the data
        fake = Faker()
        shift_name = ShiftProvider.generate_shift_name()

        # Enter the shift name dynamically
        self.enter_text(Locators.SHIFT_NAME, shift_name)
        time.sleep(1)
# self.click(Locators.SHIFT_DEFAULT)
# time.sleep(1)
        self.click(Locators.SHIFT_SUBMIT)
        time.sleep(5)
        self.logger.info("All shift Page Button are working fine")
      

        # self.click(Locators.SHIFT_EDIT)
        # time.sleep(1)
        shift_name1 = f"Shift {random.randint(5, 10000)}"
# Add the Shift
        url = "https://ipssapi.techgenzi.com/shift_configure/shift_mast_hrm/150/"
        payload = {
"shift_name": shift_name1,
"shift_start_time": "09:36",
"shift_end_time": "18:37",
"shift_break_mins": 5,
"shift_duration": 541,
"shift_work_mins": 536,
"minimum_shift_minutes": 150,
"halftime_shift_mins": 350,
"shift_start_grace_time": 5,
"shift_end_grace_time": "05",
"break_before_ot": "5",
"night_shift": False
}

        response = requests.patch(url, json=payload, headers=AppTestCase.get_headers())
        if response.status_code == 200:
                self.logger.info(f"Shift Updated Successfully: {response.status_code}")
        else:
                self.logger.error(f"Failed to Update Sequence: {response.status_code}")

        # self.click(Locators.SEQUENCE_SUBMIT)


    def rotation(self, form_data=None):
#check the cancel button

        self.click(Locators.ROTATION_TAB)
        time.sleep(1)
        self.click(Locators.ROTATION_ADD)
        time.sleep(1)
        self.click(Locators.ROTATION_CANCEL)
        time.sleep(1)
#check the rotation is submitting or not
        self.click(Locators.ROTATION_ADD)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(1)
#Adding the Rotation for daily
        self.dropdown_click(Locators.ROTATION_SHIFT,1)
        self.dropdown_click(Locators.ROTATION_SHIFT, 3)
        self.dropdown_click(Locators.ROTATION_SHIFT, 5)
        time.sleep(1)
        self.click(Locators.ROTATION_SHIFT)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_NAME,"SWING")
        time.sleep(1)
        self.click(Locators.ROTAION_FREQ)
        time.sleep(1)
        self.click(Locators.ROTATION_DAILY)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_START,12-12-2023)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(1)

# Adding the Rotation for week
        self.dropdown_click(Locators.ROTATION_SHIFT, 2)
        self.dropdown_click(Locators.ROTATION_SHIFT, 3)
        self.dropdown_click(Locators.ROTATION_SHIFT, 4)
        time.sleep(1)
        self.click(Locators.ROTATION_SHIFT)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_NAME, "SWING 1")
        time.sleep(1)
        self.click(Locators.ROTAION_FREQ)
        time.sleep(1)
        self.click(Locators.ROTATION_WEEK)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_START, 22-12-2023)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(1)
#Adding the Rotation for daily
        self.dropdown_click(Locators.ROTATION_SHIFT,1)
        self.dropdown_click(Locators.ROTATION_SHIFT, 2)
        self.dropdown_click(Locators.ROTATION_SHIFT, 3)
        time.sleep(1)
        self.click(Locators.ROTATION_SHIFT)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_NAME,"SWING 2")
        time.sleep(1)
        self.click(Locators.ROTAION_FREQ)
        time.sleep(1)
        self.click(Locators.ROTATION_MONTH)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_START,22-2-2024)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(5)
        self.click(Locators.ROTATION_CANCEL)
        time.sleep(1)
    def rotation_edit(self):
#check the cancel Button
        self.click(Locators.ROTATION_EDIT)
        time.sleep(1)
        self.click(Locators.ROTATION_CANCEL)
        time.sleep(1)
        # check the rotation is submitting or not when i clear the data and click the submit button
        self.click(Locators.ROTATION_EDIT)
        time.sleep(1)
        self.clear(Locators.ROTATION_NAME)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(1)
        # Edit the Rotation
        self.dropdown_click(Locators.ROTATION_SHIFT, 1)
        self.dropdown_click(Locators.ROTATION_SHIFT, 2)
        self.dropdown_click(Locators.ROTATION_SHIFT, 3)
        time.sleep(1)
        self.click(Locators.ROTATION_SHIFT)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_NAME, "SWING")
        time.sleep(1)
        self.click(Locators.ROTAION_FREQ)
        time.sleep(1)
        self.click(Locators.ROTATION_DAILY)
        time.sleep(1)
        self.enter_text(Locators.ROTATION_START, 12-12-2024)
        time.sleep(1)
        self.click(Locators.ROTATION_SUBMIT)
        time.sleep(1)
    def shift_page(self):
        self.shift_tab()
        self.shift_add_1()


        self.shift_add()
        self.shift_edit()
        # self.rotation()
        #self.rotation_edit()
