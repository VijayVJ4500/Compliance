
import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging

from hrm_automation.logger_file import get_logger

# Configure logger
logger = logging.getLogger('hrm_logger')
logger.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(file_handler)

class User(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("User and Userole")

    def scroll_to_bottom(self):
        # Scroll to the bottom of the page using JavaScript
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def account_click(self):
        self.click(Locators.ACCONT_BT)
        time.sleep(1)

    def manage_user_tab(self):
        self.click(Locators.MANAGE_USERROLE)
        time.sleep(1)

    def delete_user(self):
        self.click(Locators.USER_1ST_ROW)
        time.sleep(1)
        self.click(Locators.USERS_DEL)
        time.sleep(1)
        self.click(Locators.ACCEPT_YES)
        time.sleep(1)
        self.click(Locators.USER_1ST_ROW)
        time.sleep(1)

    def manage_user(self):
        self.click(Locators.USERS_ADD)
        time.sleep(1)
        self.enter_text(Locators.USERS_ADD_FNAME, "sithu")
        time.sleep(1)
        self.enter_text(Locators.USERS_ADD_LNAME, "SRI")
        time.sleep(1)
        self.enter_text(Locators.USERS_ADD_EMAIL, "kenichi@gmail.com")
        time.sleep(1)
        # self.enter_text(Locators.USERS_ADD_USERNAME,"ADS4SdsdddsafsDitdtesdsQW@ESdaBN@JA2002")
        # time.sleep(1)
        # self.click(Locators.USERS_ADD_CHECKBOX)
        # time.sleep(1)
        self.click(Locators.USER_ADD_CREATEUSER)
        time.sleep(4)
        self.click(Locators.USERS_1ST_ROW)
        time.sleep(1)

        # self.click(Locators.USERS_EDIT)
        # time.sleep(1)
        self.click(Locators.ASSIGN_ROLE_COMPLETE)
        time.sleep(6)
        self.click(Locators.USER_1ST_ROW)
        time.sleep(1)
        # self.click(Locators.USER_1ST_ROW)
        # time.sleep(3)
        self.click(Locators.USERS_EDIT)
        time.sleep(1)
        self.click(Locators.ASSIGN_ROLE)
        time.sleep(1)
        # self.click(Locators.USERS_ROW)
        # time.sleep(1)
        self.click(Locators.UPDATE_USER)
        time.sleep(1)

    def manage_userrole_tab(self):
        self.click(Locators.USER_ROLL_BT)
        time.sleep(5)

    def delete_role(self):
        self.click(Locators.ASSIGN_ROLE_CHECK)
        time.sleep(1)
        self.click(Locators.ASSIGN_ROLL_DELETE)
        time.sleep(1)
        self.click(Locators.ACCEPT_YES)
        time.sleep(1)

    def manage_userrole(self):
        time.sleep(8)
        self.click(Locators.ASSIGN_ROLE_CHECK)
        time.sleep(1)
        self.click(Locators.ASSIGN_ROLE_VIEW)
        time.sleep(2)
        self.click(Locators.ASSIGN_ROLL_BACK)
        time.sleep(1)
        self.click(Locators.ASSIGN_ROLL_ADD)
        time.sleep(4)
        self.enter_text(Locators.ROLL_NAME, "test")
        time.sleep(1)
        self.enter_text(Locators.ROLL_DES, "test")
        time.sleep(1)
        self.dropdown_click(Locators.CLONE, 1)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.click(Locators.ADMIN_CHECK)
        time.sleep(1)
        self.scroll_to_bottom()
        time.sleep(1)
        self.click(Locators.ROLL_CREATE_USERROLE)
        time.sleep(1)
        self.click(Locators.USER_UPDATE_CHECK)
        time.sleep(1)
        self.click(Locators.ASSIGN_ROLL_EDIT)
        time.sleep(5)
        self.clear(Locators.ROLL_NAME_EDIT)
        time.sleep(1)
        self.enter_text(Locators.ROLL_NAME_EDIT, "test")
        time.sleep(1)
        # self.click(Locators.ADMIN_CHECK)
        # time.sleep(1)
        self.scroll_to_bottom()
        time.sleep(1)
        self.click(Locators.ROLL_NAME_UPDATE)
        time.sleep(1)

    def account(self):
        self.click(Locators.ACCONT_BT)
        time.sleep(1)
        self.click(Locators.MY_ACCOUNT)
        time.sleep(1)
        self.click(Locators.ACC_DEL)
        time.sleep(1)
        photo_path = "D:\ssl\HRM-Backend\hrm_automation\screenshot"  # Replace with the actual file path
        self.file_upload(Locators.FILE_UPLOAD, photo_path)
        time.sleep(1)
        self.click(Locators.CHANGE_PWD)
        time.sleep(1)
        self.enter_text(Locators.CURRENT_PWD, "dev@12345678")
        time.sleep(1)
        self.enter_text(Locators.NEW_PWD, "dev@123456789")
        time.sleep(1)
        self.enter_text(Locators.CONFIRM_PWD, "dev@123456789")
        time.sleep(1)

    def userrole(self):
        self.account_click()
        self.manage_user_tab()
        self.delete_user()
        self.manage_user()
        self.manage_userrole_tab()
        self.delete_role()
        self.manage_userrole()
        self.account()
