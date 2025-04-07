import time
from hrm_automation.base import BasePage
from hrm_automation.logger_file import get_logger
from hrm_automation.locators import Locators


class Logout(BasePage):
    """
    Logout common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Logout")

    def do_logout(self):
        """
        Click the account icon and then click logout link
        :return:
        """
        self.click(Locators.ACCONT_BT)
        time.sleep(1)
        self.click(Locators.SIGN_OUT)
        time.sleep(1)
        self.logger.info("Logging out successfully")
