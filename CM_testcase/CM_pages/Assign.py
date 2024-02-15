import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Assign(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def assign_page(self):
        self.click(Locators.MENU)

        print("Clickable")
        time.sleep(2)
        self.click(Locators.ASSIGN)

        time.sleep(20)
        self.dropdown_click(Locators.FIRST_BOX, 3, "Form")

        time.sleep(20)
        self.dropdown_click(Locators.SECOND_BOX, 1, "User")

        time.sleep(20)
        self.dropdown_click(Locators.THIRD_BOX, 1, "Building Safety")

        time.sleep(20)
        self.send_keys(Locators.ASSIGN_SEARCH, "11200276")
        time.sleep(10)
        self.click(Locators.ASSIGN_CHECKBOX)
        time.sleep(2)
        self.click(Locators.ASSIGN_BUTTON)
        time.sleep(2)
        self.click(Locators.ASSIGN_SUBMIT)
        time.sleep(2)
