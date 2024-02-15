import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Compcode(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def compcode_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.COMPANY_CODE)
        time.sleep(2)
        # self.click(Locators.COMPCODE_ADD)
        # time.sleep(2)
        # self.send_keys(Locators.COMPCODE_COMP_NAME, "CMS")
        # time.sleep(2)
        # self.send_keys(Locators.COMPCODE_COMP_CODE, "Test")
        # time.sleep(2)
        # self.click(Locators.COMPCODE_SUBMIT)
        # time.sleep(2)

        # ASSIGN page
        self.click(Locators.COMPCODE_ASSIGN)
        time.sleep(2)

        self.click(Locators.COMPCODE_ASSIGN_SELECTE1)
        time.sleep(2)
        self.static_dropdown(Locators.COMPCODE_ASSIGN_SELECTE1_LIST, "Company Code")
        time.sleep(2)
        self.dropdown_click(Locators.COMPCODE_ASSIGN_SELECTE2, 1, "AAA")
        time.sleep(2)
        self.click(Locators.COMPCODE_ASSIGN_SELECTE3)
        time.sleep(2)
        self.static_dropdown(Locators.COMPCODE_ASSIGN_SELECTE3_LIST, "User")
        time.sleep(2)
        self.send_keys(Locators.COMPCODE_ASSIGN_SEARCH, "test123")
        time.sleep(2)
        self.click(Locators.COMPCODE_ASSIGN_CHECKBOX)
        time.sleep(2)
        self.click(Locators.COMPCODE_ASSIGN_BUTTON)
        time.sleep(2)
