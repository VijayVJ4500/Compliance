import time
import os
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from ..base import BasePage
from ..locators import Locators
from hrm_automation.logger_file import get_logger
from faker import Faker
def get_element_text(self, locator):
    element = self.driver.find_element(*locator)
    return element.text

class LeaveManagementNegative(BasePage):
    """Leave management negative test cases"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("LeaveManagementNegative")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/leave_management_negative"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

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

    def check_snackbar_message(self, action_type, expected_message):
        """Capture screenshot and check snackbar message"""
        time.sleep(2)  # Wait for snackbar
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(self.screenshot_dir, f"{action_type}_{timestamp}.png")
        
        try:
            self.driver.save_screenshot(screenshot_path)
            snackbar = self.driver.find_element(By.CLASS_NAME, "MuiSnackbarContent-message")
            actual_message = snackbar.text
            
            if expected_message in actual_message:
                self.logger.info(f"{action_type} validation successful - Found message: {expected_message}")
                return True
            else:
                self.logger.error(f"{action_type} validation failed - Expected '{expected_message}' but got '{actual_message}'")
                return False
        except Exception as e:
            self.logger.error(f"{action_type} validation failed - Message not found")
            return False
        
    def test_empty_reason(self):
        """Test applying leave without reason"""
        self.click(Locators.EP_LEAVE_SELF_RADIO)
        time.sleep(1)
        self.click(Locators.EP_LEAVE_APPLY_BT)
        time.sleep(1)
        self.click(Locators.EP_SINGLE_DAY_RADIO)
        time.sleep(1)
        fake = Faker()

# Generate a random future date
        random_leave_date = fake.future_date()
        self.enter_text(Locators.EP_DATE, random_leave_date.strftime("%d-%m-%Y"))
        time.sleep(1)
        self.click(Locators.EP_LEAVE_SUBMIT_BT)
        error_message = self.driver.find_element(*Locators.EP_REASON_REQUIRED).text
        time.sleep(10)
        if error_message.strip() == "Reason is required":
            self.logger.warning("Reason is not entered so not submitted. So, Test passed")  # Pass the logger name
            time.sleep(1)
            self.click(Locators.EP_LEAVE_CANCEL_BT)
            time.sleep(1)
        else:
            self.logger.error("Reason is Not Entered But may be submitted or not shown the Error, Test Failed")
                

    def test_invalid_date(self):
        """Test applying leave with invalid date format"""
        try:
            self.click(Locators.EP_LEAVE_SELF_RADIO)
            time.sleep(1)
            self.click(Locators.EP_LEAVE_APPLY_BT)
            time.sleep(1)
            self.click(Locators.EP_SINGLE_DAY_RADIO)
            time.sleep(1)
           
           

            self.enter_text(Locators.EP_DATE, f"01-02-{Faker().random_int(min=10000, max=99999)}")
            time.sleep(1)
            self.enter_text(Locators.EP_LEAVE_REASON, "Test invalid date")
            time.sleep(1)
            self.click(Locators.EP_LEAVE_SUBMIT_BT)
            time.sleep(2)

            try:
                self.driver.find_element(*Locators.EP_LEAVE_SUBMIT_BT)
                self.logger.info("Invalid date format was rejected as expected. Test passed")
                raise Exception("Invalid date was accepted")
                self.click(Locators.EP_LEAVE_CANCEL_BT)
                time.sleep(1)
            except:
                self.logger.error("Invalid date format was accepted unexpectedly. Test failed")
                time.sleep(1)
                
                
        except Exception as e:
            self.logger.error(f"Test invalid date failed: {str(e)}")
            raise
    def test_reject_without_reason(self):
        """Test rejecting leave without providing reason"""
        try:
            self.click(Locators.EP_LEAVE_REPORTEE_RADIO_BT)
            time.sleep(2)
            self.click(Locators.EP_LEAVE_REJECT_BT)
            time.sleep(2)
            # Don't enter rejection reason
            self.click(Locators.EP_LEAVE_REJECT_REJECT)
            time.sleep(2)

            try:
                close_button = self.driver.find_element(*Locators.EP_LEAVE_REJECT_CLOSE)
                if close_button.is_displayed():
                    self.logger.info("Leave Rejected reason was not Submitted without giving reason, So Test Passed")
                    self.click(Locators.EP_LEAVE_REJECT_CLOSE)
                    time.sleep(1)
                else:
                    self.logger.error("Leave was Rejected without Reason unexpectedly. Test failed")
            except:
                self.logger.error("Leave was Rejected without Reason unexpectedly")

        except Exception as e:
            self.logger.error(f"Test reject without reason failed: {str(e)}")
            raise



       
    

    def test_past_date(self):
        """Test applying leave for past date"""
        try:
            self.click(Locators.EP_LEAVE_SELF_RADIO)
            time.sleep(1)
            self.click(Locators.EP_LEAVE_APPLY_BT)
            time.sleep(1)
            self.click(Locators.EP_SINGLE_DAY_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_DATE, Faker().date_between(start_date="-1y", end_date="today").strftime("%d-%m-2024"))
            time.sleep(1)

            self.enter_text(Locators.EP_LEAVE_REASON, "Test past date")
            
            self.click(Locators.EP_LEAVE_SUBMIT_BT)

            time.sleep(3)
            if self.check_snackbar_message("Past Date", "Cannot apply leave for past Month"):
                self.logger.info("Past date validation passed")
                time.sleep(10)
                self.click(Locators.EP_LEAVE_CANCEL_BT)
                time.sleep(1)
            else:
                self.logger.error("Past date validation failed")
        except Exception as e:
            self.logger.error(f"Past date test failed: {str(e)}")
            raise

    def run_all_negative_tests(self):
        
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_leave() 
            self.test_empty_reason()          
            self.test_invalid_date()
            self.test_past_date()
            self.do_logout()
            
            # Test manager rejection without reason
            self.do_login("TGZ00028", "1234567890")
            self.navigate_to_leave()
            self.test_reject_without_reason()
            self.do_logout()
