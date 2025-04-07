import time
import os
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ..base import BasePage
from ..locators import Locators
from hrm_automation.logger_file import get_logger

class PermissionManagementNegative(BasePage):
    """
    Permission management negative test cases.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("PermissionManagementNegative")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/permission_management_negative"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_action_screenshot(self, action_type):
        """Take screenshot after action"""
        time.sleep(2)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action_type}_{timestamp}.png")
        try:
            self.driver.save_screenshot(screenshot_path)
            self.logger.info(f"Screenshot saved for {action_type}")
        except Exception as e:
            self.logger.error(f"Failed to save screenshot: {str(e)}")

    def check_snackbar_message(self, expected_message):
        """Check for specific message in snackbar"""
        time.sleep(2)  # Wait for snackbar
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"snackbar_{timestamp}.png")
        
        try:
            # Take screenshot first since snackbar only shows for 2 seconds
            self.driver.save_screenshot(screenshot_path)
            
            # Check if snackbar contains expected message
            snackbar = self.driver.find_element(By.CLASS_NAME, "MuiSnackbarContent-message")
            actual_message = snackbar.text
            
            return expected_message in actual_message
                
        except Exception as e:
            self.logger.error(f"Failed to verify snackbar message: {str(e)}")
            return False

    def do_login(self, username, password):
        """Login with given credentials"""
        try:
            self.enter_text(Locators.USERNAME_INPUT, username)
            time.sleep(1)
            self.enter_text(Locators.PASSWORD_INPUT, password)
            time.sleep(1)
            self.click(Locators.LOGIN_SUBMIT_BUTTON)
            time.sleep(2)
            self.logger.info(f"Logged in with username: {username}")
        except Exception as e:
            self.logger.error(f"Login failed for {username}: {str(e)}")
            raise

    def do_logout(self):
        """Logout from the system"""
        try:
            self.click(Locators.ACCONT_BT)
            time.sleep(1)
            self.click(Locators.SIGN_OUT)
            time.sleep(1)
            self.logger.info("Logged out successfully")
        except Exception as e:
            self.logger.error(f"Logout failed: {str(e)}")
            raise

    def navigate_to_permission(self):
        """Navigate to permission section"""
        try:
            self.click(Locators.HOME_SIDEBAR)
            time.sleep(1)
            self.click(Locators.EMP_PORTAL_CARD)
            time.sleep(2)
            self.click(Locators.EP_PERMISSION_TAB)
            time.sleep(1)
            self.logger.info("Navigated to permission section")
        except Exception as e:
            self.logger.error(f"Navigation to permission section failed: {str(e)}")
            raise

    def test_empty_reason(self):
        """Test applying permission without reason"""
        try:
            self.click(Locators.EP_PERMISSION_SELF)
            time.sleep(1)
            
            self.enter_text(Locators.EP_PERMISSION_DATE, "10-03-2025")
            time.sleep(1)
            self.dropdown_click(Locators.EP_PERMISSION_HOURS,1)
            time.sleep(1)
            self.enter_text(Locators.EP_START_TIME, "10:00")
            time.sleep(1)
            
            # Don't enter reason
            self.click(Locators.EP_PERMISSION_APPLY_BT)
            time.sleep(1)
            
            # Verify error message
            error = self.get_element(Locators.EP_PERMISSION_REASON_ERROR)
            if error.is_displayed():
                self.logger.info("Empty reason validation passed")
                self.take_action_screenshot("empty_reason_error")
            else:
                self.logger.error("Empty reason validation failed")
        except Exception as e:
            self.logger.error(f"Empty reason test failed: {str(e)}")
            raise

    def test_past_date(self):
        """Test applying permission for past date"""
        try:
            self.click(Locators.EP_PERMISSION_SELF)
            time.sleep(1)
            
            # Use yesterday's date
            yesterday = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%Y")
            self.enter_text(Locators.EP_PERMISSION_DATE, yesterday)
            time.sleep(1)
            self.dropdown_click(Locators.EP_PERMISSION_HOURS,1)
            time.sleep(1)
            
            self.enter_text(Locators.EP_START_TIME, "10:00")
            self.enter_text(Locators.EP_PERMISSION_REASON, "Test past date")
            time.sleep(1)
            
            self.click(Locators.EP_PERMISSION_APPLY_BT)
            self.take_action_screenshot("past_date_error")
            self.logger.info("Past date validation tested")
        except Exception as e:
            self.logger.error(f"Past date test failed: {str(e)}")
            raise

    def test_invalid_time(self):
        """Test applying permission with invalid time"""
        try:
            self.click(Locators.EP_PERMISSION_SELF)
            time.sleep(1)
            
            self.enter_text(Locators.EP_PERMISSION_DATE, "10-03-2025")
            time.sleep(1)
            
            self.dropdown_click(Locators.EP_PERMISSION_HOURS,1)
            time.sleep(1)
            
            # Enter invalid time
            self.enter_text(Locators.EP_START_TIME, "25:00")
            self.enter_text(Locators.EP_PERMISSION_REASON, "Test invalid time")
            time.sleep(1)
            
            self.click(Locators.EP_PERMISSION_APPLY_BT)
            self.take_action_screenshot("invalid_time_error")
            self.logger.info("Invalid time validation tested")
        except Exception as e:
            self.logger.error(f"Invalid time test failed: {str(e)}")
            raise

    def test_reject_without_remarks(self):
        """Test rejecting permission without remarks"""
        try:
            self.click(Locators.EP_PERMISSION_REPORTEE)
            time.sleep(2)
            
            self.click(Locators.EP_PERMISSION_REJECT_BT)
            time.sleep(1)
            
            # Don't enter rejection remarks
            self.click(Locators.EP_PERMISSION_REJECT_SUBMIT)
            self.take_action_screenshot("reject_no_remarks")
            self.logger.info("Rejection without remarks tested")
        except Exception as e:
            self.logger.error(f"Rejection without remarks test failed: {str(e)}")
            raise

    def run_negative_tests(self):
        """Run all negative test cases"""
        try:
            # Employee negative tests
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_permission()
            
            self.test_empty_reason()
            self.test_past_date()
            self.test_invalid_time()
            self.do_logout()
            
            # Manager negative tests
            self.do_login("TGZ00028", "1234567890")
            self.navigate_to_permission()
            self.test_reject_without_remarks()
            self.do_logout()
            
            self.logger.info("All negative test cases completed")
        except Exception as e:
            self.logger.error(f"Negative test cases failed: {str(e)}")
            raise
