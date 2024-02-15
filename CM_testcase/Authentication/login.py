import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Login(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.enter_text(Locators.USER_NAME, "11200276")
        time.sleep(3)
        self.enter_text(Locators.PASSWORD, "98765432")
        time.sleep(3)
        self.click(Locators.VISIBLE_EYE)
        time.sleep(3)
        self.click(Locators.SIGNIN)
        self.click(Locators.SIGNIN)
        time.sleep(3)

        # Negative case
        # When i click the login button without  enter any data
        # self.click(Locators.SIGNIN)
        # time.sleep(2)
        # self.required_error_msg(Locators.USERNAME_PASSWORD_REQ_MSG)
        # time.sleep(2)


