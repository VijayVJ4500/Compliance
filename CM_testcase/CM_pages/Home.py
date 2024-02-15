import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Homepage(Basepage):
    def __init__(self, driver):
        super().__init__(driver)
    def home_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.HOME)
        time.sleep(1)
        self.click(Locators.DATA)
        time.sleep(2)
        self.click(Locators.BACK)
        time.sleep(2)

