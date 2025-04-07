import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ..base import BasePage
from ..locators import Locators
from hrm_automation.logger_file import get_logger
class WFHManagement(BasePage):
    """
    WFH management test mWFHule to handle WFH applications and approvals.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("WFHManagement")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/WFH_management"
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

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

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("WFHManagement")
        self.wait = WebDriverWait(driver, 10)
        self.screenshot_dir = "screenshots/WFH_management"
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

    def navigate_to_WFH(self):
        """Navigate to WFH section"""
        try:
            self.click(Locators.HOME_SIDEBAR)
            time.sleep(1)
            self.click(Locators.EMP_PORTAL_CARD)
            time.sleep(2)
            self.click(Locators.EP_WFH_TAB)
            time.sleep(1)
            self.logger.info("Navigated to WFH section")
        except Exception as e:
            self.logger.error(f"Navigation to WFH section failed: {str(e)}")
            raise

    def apply_single_day_WFH(self, date, reason):
        """Apply single day WFH"""
        try:
            self.click(Locators.EP_WFH_SELF)
            time.sleep(1)
            self.click(Locators.EP_WFH_SINGLE_DAY_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_WFH_DATE, date)
            time.sleep(1)
            self.enter_text(Locators.EP_WFH_REASON, reason)
            time.sleep(1)
            
            self.click(Locators.EP_WFH_APPLY_BT)
            self.take_action_screenshot("single_day_WFH")
            self.logger.info(f"Applied single day WFH for {date}")
        except Exception as e:
            self.logger.error(f"Failed to apply single day WFH: {str(e)}")
            raise

    def apply_half_day_WFH(self, date, reason, first_half=True):
        """Apply half day WFH"""
        try:
            self.click(Locators.EP_WFH_SELF)
            time.sleep(1)
            self.click(Locators.EP_WFH_HALFDAY_RADIO)
            time.sleep(1)
            
            if first_half:
                self.click(Locators.EP_WFH_FIRSTHALF_RADIO)
            else:
                self.click(Locators.EP_WFH_SECONDHALF_RADIO)
            time.sleep(1)
            
            self.enter_text(Locators.EP_WFH_DATE, date)
            time.sleep(1)
            self.enter_text(Locators.EP_WFH_REASON, reason)
            time.sleep(1)
            
            self.click(Locators.EP_WFH_APPLY_BT)
            self.take_action_screenshot("half_day_WFH")
            self.logger.info(f"Applied half day WFH for {date}")
        except Exception as e:
            self.logger.error(f"Failed to apply half day WFH: {str(e)}")
            raise

    def handle_WFH_Rejection(self):
        """Handle WFH Rejection"""
        try:
            self.click(Locators.EP_WFH_REJECT_BT)
            time.sleep(1)
            # Enter rejection remarks
            self.enter_text(Locators.EP_WFH_REJECT_REMARKS, "Work priority")
            time.sleep(1)
            # Click submit
            self.click(Locators.EP_WFH_REJECT_SUBMIT)
            time.sleep(2)  # Wait for snackbar/response
            try:
                submit_button = self.get_element(Locators.EP_WFH_FROMDATE_HEADER)
                if submit_button.is_displayed():
                    self.logger.info("Rejection is Posted so cases passed")
                    self.take_action_screenshot("WFH_rejection")
                return True
                    
            except:
                self.logger.error("Rejection remarks not posted")
                self.click(Locators.EP_WFH_REJECT_CANCEL)
                return False
           
        except Exception as e:
            self.logger.error(f"Failed to handle WFH rejection: {str(e)}")
            return False

    def handle_WFH_approval(self):
            """Handle WFH approval"""
            try:
                # First click Reportee radio button
                self.click(Locators.EP_WFH_REPORTEE)
                time.sleep(2)
                
                # Click approve button
                self.click(Locators.EP_WFH_APPROVE_BT)
                time.sleep(2)
                self.driver.switch_to.alert.accept()
                time.sleep(2)
                # Check for success message
                if self.check_snackbar_message("WFH approved successfully!"):
                    self.logger.info("WFH approved successfully!")
                    self.take_action_screenshot("WFH_approval_success")
                    return True
                else:
                    self.logger.error("WFH approval failed - Success message not shown")
                    self.take_action_screenshot("WFH_approval_failed")
                    return False
                    
            except Exception as e:
                self.logger.error(f"Failed to handle WFH request: {str(e)}")
                raise


    def WFH_management_flow(self):
        """Complete WFH management flow"""
        try:
            # Employee login and apply WFHs
            self.do_login("TGZ00029", "1234567890")
            self.navigate_to_WFH()
            
            # Apply first WFH (single day)
            self.apply_single_day_WFH("10-03-2025", "Client meeting")
            
            # Apply second WFH (half day)
            self.apply_half_day_WFH("11-03-2025", "Site visit", first_half=True)
            
            # Logout as employee
            self.do_logout()

            # Manager login and handle WFHs
            self.do_login("TGZ00028", "1234567890")
            self.navigate_to_WFH()
            
            # Handle first WFH (approve)
            self.handle_WFH_approval()
            
            # Handle second WFH (reject)
            self.handle_WFH_Rejection()
            
            # Logout as manager
            self.do_logout()
            
            self.logger.info("WFH management flow completed successfully")
        except Exception as e:
            self.logger.error(f"WFH management flow failed: {str(e)}")
            raise