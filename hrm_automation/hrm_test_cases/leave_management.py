import time
import unittest
import os
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..base import BasePage
from ..locators import Locators
from faker import Faker
from hrm_automation.logger_file import get_logger

class LeaveManagement(BasePage, unittest.TestCase):
    """
    Leave management test module to handle leave applications and approvals.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("LeaveManagement")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/leave_management"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def check_snackbar_message(self, action_type, expected_message):
        """Capture screenshot and check snackbar message"""
        time.sleep(2)  # Wait for snackbar
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action_type}_{timestamp}.png")
        
        try:
            # Take screenshot first since snackbar only shows for 2 seconds
            self.driver.save_screenshot(screenshot_path)
            
            # Check if snackbar contains expected message
            snackbar = self.driver.find_element(By.CLASS_NAME, "MuiSnackbarContent-message")
            actual_message = snackbar.text
            
            if expected_message in actual_message:
                self.logger.info(f"{action_type} successful - Message verified: {expected_message}")
                return True
            else:
                self.logger.error(f"{action_type} failed - Expected '{expected_message}' but got '{actual_message}'")
                return False
                
        except Exception as e:
            self.logger.error(f"{action_type} failed - Message not found in snackbar")
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

    def navigate_to_leave(self):
        """Navigate to leave section"""
        try:
            self.click(Locators.HOME_SIDEBAR)
            time.sleep(1)
            self.click(Locators.EMP_PORTAL_CARD)
            time.sleep(2)
            self.click(Locators.EP_LEAVE_TAB)
            time.sleep(1)
        except Exception as e:
            self.logger.error(f"Navigation to leave section failed: {str(e)}")
            raise

    def apply_single_day_leave(self, date, reason):
        """Apply single day leave"""
        try:
            self.click(Locators.EP_LEAVE_SELF_RADIO)
            time.sleep(1)
            self.click(Locators.EP_LEAVE_APPLY_BT)
            time.sleep(1)

            self.click(Locators.EP_SINGLE_DAY_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_DATE, date)
            time.sleep(1)
            
            self.enter_text(Locators.EP_LEAVE_REASON, reason)
            time.sleep(1)
            
            self.click(Locators.EP_LEAVE_SUBMIT_BT)
            if self.check_snackbar_message("Single Day Leave", "Leave applied successfully"):
                self.logger.info(f"Successfully applied single day leave for {date}")
            else:
                self.logger.error(f"Failed to apply single day leave - Success message not shown")
        except Exception as e:
            self.logger.error(f"Failed to apply single day leave")
            raise

    def apply_half_day_leave(self, date, reason):
        """Apply half day leave"""
        try:
            self.click(Locators.EP_LEAVE_SELF_RADIO)
            time.sleep(1)
            self.click(Locators.EP_LEAVE_APPLY_BT)
            time.sleep(1)

            self.click(Locators.EP_HALFDAY_RADIO) 
            self.click(Locators.EP_FIRSTHALF_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_DATE, date)
            time.sleep(1)
            
            self.enter_text(Locators.EP_LEAVE_REASON, reason)
            time.sleep(1)
            
            self.click(Locators.EP_LEAVE_SUBMIT_BT)
            if self.check_snackbar_message("Half Day Leave", "Leave applied successfully"):
                self.logger.info(f"Successfully applied half day leave for {date}")
            else:
                self.logger.error(f"Failed to apply half day leave - Success message not shown")
        except Exception as e:
            self.logger.error(f"Failed to apply half day leave")
            raise

    def handle_leave_requests(self, approve=True):
        """Handle leave approval/rejection"""
        try:
            self.click(Locators.EP_LEAVE_REPORTEE_RADIO_BT)
            time.sleep(2)
            
            if approve:
                self.click(Locators.EP_LEAVE_APPROVE_BT)
                if self.check_snackbar_message("Leave Approval", "Leave Approved Successfully!"):
                    self.logger.info("Leave approved successfully")
                else:
                    self.logger.error("Leave approval failed - Success message not shown")
            else:
                self.click(Locators.EP_LEAVE_REJECT_BT)
                time.sleep(1)
                self.enter_text(Locators.EP_LEAVE_REJECT_REASON, "Critical work day")
                time.sleep(1)
                self.click(Locators.EP_LEAVE_REJECT_REJECT)
                time.sleep(1)
                if self.check_snackbar_message("Leave Rejection", "Leave Rejected Successfully!"):
                    self.logger.info("Leave rejected successfully")
                else:
                    self.logger.error("Leave rejection failed - Success message not shown")
                
        except Exception as e:
            self.logger.error(f"Failed to handle leave request")
            raise

    def leave_management_page(self):
        """Test all leave management flows"""
        try:
            # Employee login and apply leaves
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_leave()

            fake = Faker()  
            # Generate a random date in the future (e.g., within the next year)
            random_leave_date =fake.future_date()
            # Apply leave using the generated date
            self.apply_single_day_leave(random_leave_date.strftime("%d-%m-%Y"), "Personal work")        
            random_leave_date1 =fake.future_date()
            # Apply second leave (half day)
            self.apply_half_day_leave(random_leave_date1.strftime("%d-%m-%Y"), "Doctor appointment")
            
            # Logout as employee
            self.do_logout()

            # Manager login and handle leaves
            self.do_login("TGZ00028", "1234567890")
            self.navigate_to_leave()
            
            # Handle first leave (approve)
            self.handle_leave_requests(approve=True)
            
            # Handle second leave (reject)
            self.handle_leave_requests(approve=False)
            
            # Logout as manager
            self.do_logout()
            
        except Exception as e:
            self.logger.error(f"Leave management test failed")
            raise

