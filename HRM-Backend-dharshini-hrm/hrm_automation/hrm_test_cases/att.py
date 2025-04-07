import time
import unittest

from driver import driver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger


class attendance(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def attendance_tab(self):
        time.sleep(2)
        self.click(Locators.ATTENDANCE_SIDEBAR)
        time.sleep(10)

    def att_excel(self):
        self.dropdown_click(Locators.ATT_FIL_EMP, 1)
        time.sleep(10)
        self.click(Locators.ATT_DATE_FILTER)
        time.sleep(2)
        self.click(Locators.ATT_MONTH)
        time.sleep(5)
        self.click(Locators.ATT_APPLY_FIL)
        time.sleep(2)
        self.click(Locators.ATT_EXPORT)
        time.sleep(2)
        # self.driver.execute_script("window.scrollBy(0,500)")
        # time.sleep(1)
        self.click(Locators.ATT_RESET)
        time.sleep(15)
    def att_edit(self):
        self.click(Locators.ATT_EDIT)
        time.sleep(16)
        self.enter_text(Locators.ATT_PUNCH,"09:00")
        time.sleep(2)
        self.click(Locators.ATT_NEW_PUNCH_BT)
        time.sleep(2)
        self.enter_text(Locators.ATT_NEW_PUNCH,"17:00")
        time.sleep(2)
        self.click(Locators.ATT_SAVE)
        time.sleep(2)
    def irr_edit(self):
        self.click(Locators.IRREGULAR)
        time.sleep(2)
        self.click(Locators.IRREGULAR_EDIT)
        time.sleep(2)
        self.click(Locators.ATT_CLOSE)
        time.sleep(2)
        self.click(Locators.IRREGULAR_EDIT)
        time.sleep(2)
        self.click(Locators.ATT_SAVE)
        time.sleep(2)
        self.click(Locators.ATT_NEW_PUNCH_BT)
        time.sleep(2)
        self.enter_text(Locators.IRR_ATT_NEW_PUNCH,"17:50")
        time.sleep(2)
        self.click(Locators.ATT_SAVE)
        time.sleep(2)
    def bulk_add(self):
        self.click(Locators.BULK_ATT)
        time.sleep(2)
        self.click(Locators.BULK_EMP)
        time.sleep(6)
        self.click(Locators.ATT_EMP_1)
        time.sleep(6)
        self.click(Locators.BULK_EMP)
        time.sleep(6)
        # self.dropdown_click(Locators.BULK_EMP, 3)
        # time.sleep(2)
        # self.dropdown_click(Locators.BULK_EMP, 4)
        # time.sleep(2)
        # self.dropdown_click(Locators.BULK_EMP, 5)
        # time.sleep(2)
        self.enter_text(Locators.BULK_TIME,"09.00")
        time.sleep(2)
        self.enter_text(Locators.BULK_DATE,"12-04-2024")
        time.sleep(2)
        self.click(Locators.BULK_SAVE)
        time.sleep(2)
        self.click(Locators.BULK_ATT)
        time.sleep(2)
        self.enter_text(Locators.BULK_TIME_2, "17.00")
        time.sleep(2)
        self.click(Locators.BULK_SAVE)
        time.sleep(2)
    def manual(self):
        self.click(Locators.MANUAL_BT)
        time.sleep(25)
        self.dropdown_click(Locators.MANUAL_EMPLOYEE, 1)
        time.sleep(9)
        self.enter_text(Locators.MANUAL_RANGE, "13-03-2024")
        time.sleep(3)
        self.enter_text(Locators.MANUAL_SELECT_TIME, "900")
        time.sleep(1)
        self.click(Locators.MANUAL_SAVE)
        time.sleep(8)
        self.click(Locators.MANUAL_VIEW)
        time.sleep(2)
        self.click(Locators.MANUAL_EDIT)
        time.sleep(1)
        self.enter_text(Locators.MANUAL_EDIT_TIME, "1212")
        time.sleep(5)

        headers = {
            'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDMyMjc2MywianRpIjoiZTQzYzkxM2YtZjg1ZS00ODAwLWE5YWYtYTdiMzQ4ZWY4YmRhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VybmFtZSI6Iml0aG9kQHBnYy5jb20iLCJjb250cm9saWQiOjEsInByb2plY3RpZCI6IlRJUExQR0MiLCJmaW55ciI6IjIzLTI0IiwiZmlueXJfaWQiOjE2NDk2ODIyMDQ3NzgsImNvbXBjb2RlIjoiR0pJIiwiZGlzcGxheSI6IkdKIElOTk9WQVRJT05TIEFORCBURVhUSUxFIE5FVFdPUksgUFJJVkFURSBMSU1JVEVEIiwiY29tcG5hbWUiOiJHSiBJTk5PVkFUSU9OUyBBTkQgVEVYVElMRSBORVRXT1JLIFBSSVZBVEUgTElNSVRFRCIsImJicmFuY2giOiJTSVZBS0FTSSIsImFkZHJlc3MiOiIxLzQwNyxEUCAtMiwzJjQgU0lEQ08gSU5EVVNUUklBTCBFU1RBVEUsIFNVTEFLS0FSQUkiLCJnc3RubyI6IjMzQUFDQ0c2MTM2QzFaNCIsImNvbXBhbnlfaWQiOjE1MzkxNDc2NDk3MDUsInVzZXJpZCI6MTU3MTY1NjQ5NDM3MSwiZW1wX2lkIjpudWxsLCJ1c2VyX3JvbGUiOiJBZG1pbiJ9LCJuYmYiOjE3MTAzMjI3NjMsImV4cCI6MTcxMDQwOTE2M30.PnUA6RPRzqL0VEpAuxmVIEX_RdtQNRGLRqc09FkUo6Y',  # Replace YOUR_ACCESS_TOKEN with your actual access token
            'Content-Type': 'application/json'
        }
        url = 'https://ipssapi.techgenzi.com/att/att_gen/attendance_edit'


        response = requests.put(url, headers=headers, json={})
        try:
            response.raise_for_status()
            if response.status_code == 200:
                get_logger().info("Punch was Updated successfully!")
                time.sleep(10)
                self.enter_text(Locators.MANUAL_SELECT_TIME, "1745")
                time.sleep(1)
                self.click(Locators.MANUAL_SAVE)
                time.sleep(5)
                self.click(Locators.MANUAL_VIEW)
                time.sleep(2)
                self.click(Locators.MANUAL_DELETE)
                time.sleep(2)
                self.click(Locators.MANUAL_GO_BACK)
                time.sleep(2)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
            print(response.text)
            time.sleep(4)
            self.click(Locators.MANUAL_GO_BACK)
            get_logger().warning("Punch is not Updated!", response.status_code)
            time.sleep(5)
        except requests.exceptions.RequestException as err:
            print(f"Request Error: {err}")
            self.click(Locators.MANUAL_GO_BACK)
            get_logger().warning("Punch is Not Updated!")
            time.sleep(5)





    def att_page(self):
        self.attendance_tab()
        self.att_excel()
        self.att_edit()
        self.irr_edit()
        self.bulk_add()
        self.manual()