import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from ..base import BasePage
from ..locators import Locators
from hrm_automation.logger_file import get_logger

class PermissionManagement(BasePage):
    """
    Permission management test module to handle permission requests and approvals.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("PermissionManagement")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/permission_management"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def take_action_screenshot(self, action_type):
        """Take screenshot after action"""
        time.sleep(2)  # Wait for snackbar
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

    def apply_permission(self, date, hours, start_time, reason):
        """Apply permission"""
        try:
            self.click(Locators.EP_PERMISSION_SELF)
            time.sleep(1)
            
            # Enter date
            self.enter_text(Locators.EP_PERMISSION_DATE, date)
            time.sleep(1)
            
            self.dropdown_click(Locators.EP_PERMISSION_HOURS,1)
            time.sleep(1)
            
            # Enter start time
            self.enter_text(Locators.EP_START_TIME, start_time)
            time.sleep(1)
            
            # Enter reason
            self.enter_text(Locators.EP_PERMISSION_REASON, reason)
            time.sleep(1)
            
            # Submit
            self.click(Locators.EP_PERMISSION_APPLY_BT)
            # Check for success message
            if self.check_snackbar_message("Permission Applied successfully!"):
                self.logger.info("Permission Applied successfully!")
                self.take_action_screenshot("Permission_Applied_success")
                return True
            else:
                self.logger.error("Permission Applied failed - Success message not shown")
                self.take_action_screenshot("Applied_Applied_failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to handle Permission request: {str(e)}")
            raise

    def handle_permission_approval(self):
        """Handle permission approval"""
        try:
            self.click(Locators.EP_PERMISSION_REPORTEE)
            time.sleep(2)
            
            self.click(Locators.EP_PERMISSION_APPROVE_BT)
            time.sleep(2)
        # Check for success message
            if self.check_snackbar_message("Permission approved successfully!"):
                self.logger.info("Permission approved successfully!")
                self.take_action_screenshot("Permission_approval_success")
                return True
            else:
                self.logger.error("Permission approval failed - Success message not shown")
                self.take_action_screenshot("permission_approval_failed")
                return False
                
        except Exception as e:
            self.logger.error(f"Failed to handle Permission request: {str(e)}")
            raise
    def handle_permission_rejection(self):
        """Handle permission rejection"""
        try:
            self.click(Locators.EP_PERMISSION_REPORTEE)
            time.sleep(2)
            
            self.click(Locators.EP_PERMISSION_REJECT_BT)
            time.sleep(1)
            
            self.enter_text(Locators.EP_PERMISSION_REJECT_REMARKS, "Work priority")
            time.sleep(1)
            
            self.click(Locators.EP_PERMISSION_REJECT_SUBMIT)
            time.sleep(2)
            try:
                submit_button = self.get_element(Locators.EP_OD_FROMTIME_HEADER)
                if submit_button.is_displayed():
                    self.logger.info("Rejection is Posted so cases passed")
                    self.take_action_screenshot("od_rejection")
                return True
                    
            except:
                self.logger.error("Rejection remarks not posted")
                self.click(Locators.EP_OD_REJECT_CANCEL)
                return False
           
        except Exception as e:
            self.logger.error(f"Failed to handle OD rejection: {str(e)}")
            return False

    def permission_management_flow(self):
        """Complete permission management flow"""
        try:
            # Employee login and apply permissions
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_permission()
            
            # Apply first permission
            self.apply_permission("13-03-2025", 2, "10:00", "Doctor appointment")
            
            # Apply second permission
            self.apply_permission("14-03-2025", 1, "14:00", "Personal work")
            
            # Logout as employee
            self.do_logout()

            # # Manager login and handle permissions
            # self.do_login("TGZ00028", "1234567890")
            # self.navigate_to_permission()
            
            # # Handle first permission (approve)
            # self.handle_permission_approval()
            
            # # Handle second permission (reject)
            # self.handle_permission_rejection()
            
            # # Logout as manager
            # self.do_logout()
            
            self.logger.info("Permission management flow completed successfully")
        except Exception as e:
            self.logger.error(f"Permission management flow failed: {str(e)}")
            raise
