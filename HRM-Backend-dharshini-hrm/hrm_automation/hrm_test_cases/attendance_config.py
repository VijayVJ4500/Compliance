import time
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from logger import logger
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import logging

from hrm_automation.logger_file import get_logger

# # Configure self.logger
logger.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.
# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)  # or INFO, WARNING, ERROR, etc.
# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add handler to the self.logger
logger.addHandler(file_handler)
class att_confg(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Attendance Configuration")
    def att_confg_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        self.click(Locators.ATT_CONFG_CARD)
        time.sleep(4)
    def overtime_tab(self):
        self.click(Locators.OVERTIME_RADIO)
        time.sleep(4)

    # ADD THE OVERTIME
    def overtime_add(self):
# Check the cancel Button whether the data is cancelling or not
        self.click(Locators.OVERTIME_ADD)
        time.sleep(1)
        self.click(Locators.OVERTIME_CANCEL)
        time.sleep(1)
# check the submit button whether the empty fields are posting or not
        self.click(Locators.OVERTIME_ADD)
        time.sleep(1)
        self.click(Locators.OVERTIME_SUBMIT)
        time.sleep(1)
# Add the overtime
        self.enter_text(Locators.OVERTIME_NAME, "Overtime 5")
        time.sleep(1)
        self.enter_text(Locators.OVERTIME_TIMESS, "2")
        time.sleep(1)
        self.click(Locators.OVERTIME_SUBMIT)
        time.sleep(5)
        self.logger.info("overtime  Added successfully")

    def overtime_edit(self):
# Check the cancel Button whether the data is cancelling or not
#         self.click(Locators.OVERTIME_EDIT)
#         time.sleep(1)
#         self.click(Locators.OVERTIME_CANCEL)
#         time.sleep(3)
# check the submit button whether the empty fields are posting or not
        self.click(Locators.OVERTIME_EDIT)
        time.sleep(1)
        self.clear(Locators.OVERTIME_NAME)
        time.sleep(1)
        self.clear(Locators.OVERTIME_TIMESS)
        time.sleep(1)
        self.click(Locators.OVERTIME_SUBMIT)
        time.sleep(1)
# Edit the OVERTIME
        self.enter_text(Locators.OVERTIME_NAME, "Overtime")
        time.sleep(1)
        self.enter_text(Locators.OVERTIME_TIMESS, "2")
        time.sleep(1)
        self.click(Locators.OVERTIME_SUBMIT)
        time.sleep(6)
        self.logger.info("overtime  Updated successfully")
    def permission_tab(self):
        time.sleep(5)
        self.click(Locators.PERMIS_RADIO)
        time.sleep(2)
    # ADD THE SHIFT

    def permission_add(self):
# Check the cancel Button whether the data is cancelling or not
        self.click(Locators.PERMISSION_ADD)
        time.sleep(1)
        self.click(Locators.PERMISSION_CANCEL)
        time.sleep(1)
# check the submit button whether the empty fields are posting or not
        self.click(Locators.PERMISSION_ADD)
        time.sleep(1)
        self.click(Locators.PERMISSION_SUBMIT)
        time.sleep(1)
# Add the PERMISSION
        self.enter_text(Locators.PERMISSION_NAME, "Permission labors")
        time.sleep(1)
        self.dropdown_click(Locators.PERMISSION_CAT, 2)
        time.sleep(1)
        self.enter_text(Locators.PERMISSION_HOURS, "120")
        time.sleep(1)
        self.click(Locators.PERMISSION_SUBMIT)
        time.sleep(6)
        self.logger.info("Permission Added successfully")

    def permission_edit(self):
    # Check the cancel Button whether the data is cancelling or not
        self.click(Locators.PERMISSION_EDIT)
        time.sleep(1)
        self.click(Locators.PERMISSION_CANCEL)
        time.sleep(1)
    # check the submit button whether the empty fields are posting or not
        self.click(Locators.PERMISSION_EDIT)
        time.sleep(1)
        self.clear(Locators.PERMISSION_NAME)
        time.sleep(1)
        self.click(Locators.PERMISSION_SUBMIT)
        time.sleep(1)
# Edit the PERMISSION
        self.enter_text(Locators.PERMISSION_NAME, "Permission for estaff")
        time.sleep(1)
        self.dropdown_click(Locators.PERMISSION_CAT, 5)
        time.sleep(1)
        self.click(Locators.PERMISSION_SUBMIT)
        time.sleep(5)
        self.logger.info("Permission Updated successfully")

#
    def week_off_add(self):
# Check the cancel Button whether the data is cancelling or not
        self.click(Locators.WEEK_ADD)
        time.sleep(1)
        self.click(Locators.WEEK_CANCEL)
        time.sleep(1)
# check the submit button whether the empty fields are posting or not
        self.click(Locators.WEEKOFF_RADIO)
        time.sleep(2)
        self.click(Locators.WEEK_ADD)
        time.sleep(1)
        self.click(Locators.WEEK_SUBMIT)
        time.sleep(1)
# Add the WEEK for day
        self.enter_text(Locators.WEEK_NAME, "weekoff tues")
        time.sleep(1)
        # self.click(Locators.WEEK_OFF)
        # time.sleep(3)
        self.click(Locators.WEEK_SUBMIT)
        time.sleep(5)
        # self.logger.info("Weekoff created successfully")

        try:
            time.sleep(2)
            # Check for specific snackbar messages using XPath with exact text
            if self.is_element_present("//div[text()='Saved successfully!']"):
                time.sleep(2)
                self.logger.info("Weekoff added successfully!")
                time.sleep(2)
            elif self.is_element_present("//div[text()='WeekOff title already exists']"):
                self.logger.warning("Weekoff already exists!")
                self.click(Locators.WEEK_CANCEL)
                time.sleep(1)
            else:
                self.logger.error("Weekoff not added!")
                self.click(Locators.WEEK_CANCEL)
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"An error occurred while verifying the snackbar message: {e}")
            self.click(Locators.WEEK_CANCEL)
            time.sleep(1)

    def week_edit(self):
# Check the cancel Button whether the data is cancelling or not
        self.click(Locators.WEEK_EDIT)
        time.sleep(1)
        self.click(Locators.WEEK_CANCEL)
        time.sleep(1)
# check the submit button whether the empty fields are posting or not
        self.click(Locators.WEEK_EDIT)
        time.sleep(1)
        self.clear(Locators.WEEK_NAME)
        time.sleep(1)
        self.click(Locators.WEEK_SUBMIT)
        time.sleep(1)
# Edit the WEEK for day
        self.enter_text(Locators.WEEK_NAME, "week wedn")
        time.sleep(1)
        self.click(Locators.WEEK_SUBMIT)
        time.sleep(5)
        # self.logger.info("Weekoff Updated successfully")


        try:
            time.sleep(1)
            # Check for specific snackbar messages using XPath with exact text
            if self.is_element_present("//div[text()='Updated Successfully!']"):
                time.sleep(1)
                self.logger.info("Weekoff Updated successfully!")
            elif self.is_element_present("//div[text()='WeekOff title already exists']"):
                self.logger.warning("Weekoff already exists!")
                self.click(Locators.WEEK_CANCEL)
                time.sleep(1)
            else:
                self.logger.error("Weekoff not added!")
                self.click(Locators.WEEK_CANCEL)
                time.sleep(1)
        except Exception as e:
            self.logger.error(f"An error occurred while verifying the snackbar message: {e}")
            #
            # self.click(Locators.WEEK_CANCEL)
            # time.sleep(1)


    def working_day_tab(self):
        self.click(Locators.WORKING_RADIO)
        time.sleep(5)


# ADD THE OVERTIME
    def working_day_add(self):
        # Check the Cancel Button whether the data is canceling or not
        self.click(Locators.WORK_ADD)
        time.sleep(3)
        # Locate the popup element
        popup = self.driver.find_element(By.CSS_SELECTOR, ".MuiDialogContent-root.css-1ty026z")
        actions = ActionChains(self.driver)

        # Define the scroll amount and number of scrolls
        scroll_amount = 200  # Adjust this value based on the scroll speed/requirement
        num_scrolls = 10  # 7 is there Adjust the number of scrolls as needed

        # Perform vertical scrolling on the popup
        for _ in range(num_scrolls):
            actions.move_to_element(popup).click_and_hold().move_by_offset(0, scroll_amount).release().perform()
            time.sleep(1)  # Add a delay between scrolls if necessary

        self.click(Locators.WORK_CANCEL)
        time.sleep(1)
        # check the submit button whether the empty fields are posting or not
        self.click(Locators.WORK_ADD)
        time.sleep(1)
        self.click(Locators.WORK_SUBMIT)
        time.sleep(1)
        # Add the working days
        self.enter_text(Locators.WORK_YEAR, "2026")
        time.sleep(1)
        self.enter_text(Locators.WORK_JAN, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_FEB, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_MAR, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_APR, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_MAY, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_JUN, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_JUL, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_AUG, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_SEP, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_OCT, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_NOV, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_DEC, "27")
        time.sleep(1)
        self.click(Locators.WORK_SUBMIT)
        time.sleep(5)
        self.logger.info("Working days  Added successfully")


    def working_day_edit(self):
        # # Check the cancel Button whether the data is cancelling or not
        # self.click(Locators.WORK_EDIT)
        # time.sleep(1)
        # self.click(Locators.WORK_CANCEL)
        # time.sleep(3)
        # check the submit button whether the empty fields are posting or not
        self.click(Locators.WORK_EDIT)
        time.sleep(1)
        self.clear(Locators.WORK_YEAR)
        time.sleep(1)
        self.clear(Locators.WORK_JAN)
        time.sleep(1)
        self.clear(Locators.WORK_FEB)
        time.sleep(1)
        self.clear(Locators.WORK_MAR)
        time.sleep(1)
        self.clear(Locators.WORK_APR)
        time.sleep(1)
        self.clear(Locators.WORK_MAY)
        time.sleep(1)
        self.clear(Locators.WORK_JUN)
        time.sleep(1)
        self.clear(Locators.WORK_JUL)
        time.sleep(1)
        self.clear(Locators.WORK_AUG)
        time.sleep(1)
        self.clear(Locators.WORK_SEP)
        time.sleep(1)
        self.clear(Locators.WORK_OCT)
        time.sleep(1)
        self.clear(Locators.WORK_NOV)
        time.sleep(1)
        self.clear(Locators.WORK_DEC)
        time.sleep(1)
        self.click(Locators.WORK_SUBMIT)
        time.sleep(1)
        # Edit the working days

        self.enter_text(Locators.WORK_YEAR, "2027")
        time.sleep(1)
        self.enter_text(Locators.WORK_JAN, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_FEB, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_MAR, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_APR, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_MAY, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_JUN, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_JUL, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_AUG, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_SEP, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_OCT, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_NOV, "27")
        time.sleep(1)
        self.enter_text(Locators.WORK_DEC, "27")
        time.sleep(1)
        self.click(Locators.WORK_SUBMIT)
        time.sleep(6)
        time.sleep(5)
        self.logger.info("Working days Updated successfully")

    def attconfg_page(self):
        self.att_confg_tab()
        self.week_off_add()
        self.week_edit()
        self.overtime_tab()
        # self.overtime_add()
        self.overtime_edit()
        self.permission_tab()
        self.permission_add()
        self.permission_edit()
        self.working_day_tab()
        self.working_day_add()
        self.working_day_edit()


