import time
import os
from datetime import datetime, timedelta
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from ..base import BasePage
from ..locators import Locators
from hrm_automation.logger_file import get_logger

class OnDutyManagementNegative(BasePage):
    """
    On Duty management negative test cases.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("OnDutyManagementNegative")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/onduty_management_negative"
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
            snackbar = self.driver.find_element(By.XPATH, "(//div[@class='MuiAlert-message css-1xsto0d'])[1]")
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

    def navigate_to_od(self):
        """Navigate to OD section"""
        try:
            self.click(Locators.HOME_SIDEBAR)
            time.sleep(1)
            self.click(Locators.EMP_PORTAL_CARD)
            time.sleep(2)
            self.click(Locators.EP_OD_TAB)
            time.sleep(1)
            self.logger.info("Navigated to OD section")
        except Exception as e:
            self.logger.error(f"Navigation to OD section failed: {str(e)}")
            raise

    def test_invalid_date(self):
        """Test applying OD with invalid date format"""
        try:
            self.click(Locators.EP_OD_SELF)
            time.sleep(1)
            self.click(Locators.EP_OD_SINGLE_DAY_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_OD_DATE,f"01-02-{Faker().random_int(min=10000, max=99999)}")
            time.sleep(1)
            self.enter_text(Locators.EP_OD_REASON, "Test invalid date")
            time.sleep(1)
            self.click(Locators.EP_OD_APPLY_BT)
            time.sleep(3)
            # Check for success message
            if self.check_snackbar_message("On duty Applied Successfully!"):
                self.logger.error("On duty applied  with invalid date, So Case Failed")
                self.take_action_screenshot("od_approval_success")
                return False
            else:
                self.logger.info("OD is not Applied  - Success message not shown")
                self.take_action_screenshot("od_Apply_failed")
                return True
        except Exception as e:
            self.logger.error(f"Invalid date test failed: {str(e)}")
            raise

    def test_empty_reason(self):
        """Test applying OD without reason"""
        try:
            self.click(Locators.EP_OD_SELF)
            time.sleep(1)
            self.click(Locators.EP_OD_SINGLE_DAY_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_OD_DATE, Faker().future_date().strftime("%d-%m-%Y"))
            time.sleep(1)
            # Don't enter reason
            
            self.click(Locators.EP_OD_APPLY_BT)
             # Check for success message
            if self.check_snackbar_message("On duty Applied successfully!"):
                self.logger.error("On duty applied with empty reason field")
                self.take_action_screenshot("od_approval_failed")
                return False
            else:
                self.logger.info("Empty reason is not Posting - Success message not shown")
                self.take_action_screenshot("od_approval_success")
                return False
        except Exception as e:
            self.logger.error(f"Empty reason test failed: {str(e)}")
            raise

    
    def test_past_date(self):
        """Test applying OD for past date month"""
        try:
            self.click(Locators.EP_OD_SELF)
            time.sleep(1)
            self.click(Locators.EP_OD_SINGLE_DAY_RADIO)
            time.sleep(1)
            
          
            self.enter_text(Locators.EP_OD_DATE, Faker().date_between(start_date="-1y", end_date="today").strftime("%d-%m-2024"))
            time.sleep(1)
            self.enter_text(Locators.EP_OD_REASON, "Test past date")
            time.sleep(1)
            
            self.click(Locators.EP_OD_APPLY_BT)
# Check for success message
            if self.check_snackbar_message("On duty Applied successfully!"):
                self.logger.error("On duty applied with past month field")
                self.take_action_screenshot("od_approval_case_failed")
                return False
            else:
                self.logger.info("Onduty with Past Month not applied - Success message not shown")
                self.take_action_screenshot("od_approvalcase_success")
                return False
        except Exception as e:
            self.logger.error(f"Onduty with Past Month test failed: {str(e)}")
            raise

            
        except Exception as e:
            self.logger.error(f"Past date test failed: {str(e)}")
            raise

    def test_reject_without_remarks(self):
        """Test rejecting OD without providing remarks"""
        try:
            self.click(Locators.EP_OD_REPORTEE)
            time.sleep(2)
            self.click(Locators.EP_OD_REJECT_BT)
            time.sleep(1)
            # Don't enter rejection remarks
            self.click(Locators.EP_OD_REJECT_SUBMIT)
            time.sleep(2)

            try:
                submit_button = self.get_element(Locators.EP_OD_FROMDATE_HEADER)
                if submit_button.is_displayed():
                    self.logger.error("Rejection remarks not posted, So Test Failed")
                    self.take_action_screenshot("od_rejection")
                return True
                    
            except:
                self.logger.info("Rejection remarks not posted, So Test Passed")
                self.click(Locators.EP_OD_REJECT_CANCEL)
                return False
           
        except Exception as e:
            self.logger.error(f"Failed to handle OD rejection: {str(e)}")
            return False

    def run_all_negative_tests(self):
        """Run all negative test cases"""
        try:
            # Employee negative tests
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_od()            
            self.test_invalid_date()
            # self.test_empty_reason()
            # self.test_past_date()
            self.do_logout()
            
            # # Manager negative tests
            # self.do_login("TGZ00028", "1234567890")
            # self.navigate_to_od()
            # self.test_reject_without_remarks()
            # self.do_logout()
            
            self.logger.info("All negative test cases completed")
        except Exception as e:
            self.logger.error(f"Negative test cases failed: {str(e)}")
            raise
