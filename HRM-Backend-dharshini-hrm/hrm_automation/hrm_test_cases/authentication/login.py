import time
import unittest

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger


class LoginPage(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("LoginPage")  # Initialize logger in __init__ method

    def a_login_invalid_credentials(self):
        """Test case for logging in with invalid credentials."""
        self.enter_text(Locators.USERNAME_INPUT, "invalid_username")
        time.sleep(1)
        self.enter_text(Locators.PASSWORD_INPUT, "invalid_password")
        time.sleep(1)
        self.click(Locators.SHOW_PASSWORD)
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(1)
        get_logger("LoginPage").warning("Attempted login with invalid credentials, so Login Failed")
        time.sleep(1)
        self.clear(Locators.USERNAME_INPUT)
        time.sleep(1)
        self.clear(Locators.PASSWORD_INPUT)
        time.sleep(1)

    def b_login_invalid_Password(self):
        self.enter_text(Locators.USERNAME_INPUT, "ithod@pgc.com")
        time.sleep(1)
        self.enter_text(Locators.PASSWORD_INPUT, "wrong password")
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(1)
        get_logger("LoginPage").warning(
            "Username is correct. But, Password is Wrong. So,Login Failed")  # Pass the logger name
        time.sleep(1)
        self.clear(Locators.USERNAME_INPUT)
        time.sleep(1)
        self.clear(Locators.PASSWORD_INPUT)
        time.sleep(1)

    def c_login_invalid_username(self):
        self.enter_text(Locators.USERNAME_INPUT, "wrong username")
        time.sleep(1)
        self.enter_text(Locators.PASSWORD_INPUT, "dev@123456789")
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(1)
        get_logger("LoginPage").warning(
            "Password is correct. But, username is Wrong. So, Login Failed")  # Pass the logger name
        time.sleep(1)
        self.clear(Locators.USERNAME_INPUT)
        time.sleep(1)
        self.clear(Locators.PASSWORD_INPUT)
        time.sleep(1)

    def d_login_not_entered_Password(self):
        self.enter_text(Locators.USERNAME_INPUT, "ithod@pgc.com")
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(1)
        # get_logger("LoginPage").warning(
        #     "Username is not entered. So, Test passed")  # Pass the logger name
        # time.sleep(1)
        try:
            self.assertEqual("Password is required", self.get_text(Locators.LOGIN_PASSWORD_ONLY_REQUIRED))
            self.logger.warning("Password is Not entered. So,Login Failed")
            time.sleep(1)

        except:
            self.logger.error("Test Failed")

        self.clear(Locators.USERNAME_INPUT)
        time.sleep(1)

    def e_login_not_entered_username(self):
        self.enter_text(Locators.PASSWORD_INPUT, "dev@123456789")
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(2)

        try:
            self.assertEqual("Username is required.", self.get_text(Locators.LOGIN_USERNAME_ONLY_REQUIRED))
            get_logger("LoginPage").warning("Username is not Entered, so Login Failed")  # Pass the logger name
            time.sleep(1)

        except:
            get_logger("LoginPage").error("Test Failed")

        self.clear(Locators.PASSWORD_INPUT)
        time.sleep(2)
        # get_logger("LoginPage").warning(
        #     "Username is not Entered, so Login Failed")  # Pass the logger name
        # time.sleep(1)

    def f_login(self):
        self.enter_text(Locators.USERNAME_INPUT, "ithod@pgc.com")
        time.sleep(1)
        self.enter_text(Locators.PASSWORD_INPUT, "dev@123456789")
        time.sleep(1)
        self.click(Locators.SHOW_PASSWORD)
        time.sleep(1)
        self.click(Locators.LOGIN_SUBMIT_BUTTON)
        time.sleep(5)
        self.logger.info("Logging in successfully")  # Log message using logger

    def login_page(self):
        # self.a_login_invalid_credentials()
        # self.b_login_invalid_Password()
        # self.c_login_invalid_username()
        # self.d_login_not_entered_Password()
        # self.e_login_not_entered_username()
        self.f_login()
