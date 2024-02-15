import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Managedata(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def manage_data_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.MANAGE_DATA)
        time.sleep(2)
        # self.click(Locators.MANAGE_DATA_CLICK)
        # time.sleep(2)
        # self.click(Locators.MANAGE_DATA_ADD)
        # time.sleep(2)
        # self.enter_text(Locators.MANAGE_DATA_FIRST_INPUT,"YTREF8976K")
        # time.sleep(2)
        # self.enter_text(Locators.MANAGE_DATA_SEC_INPUT, "uyYBl")
        # time.sleep(2)
        # self.click(Locators.MANAGE_DATA_THRID_INPUT)
        # time.sleep(2)
        # self.static_dropdown(Locators.MANAGE_DATA_OPTION,"Yes")
        # time.sleep(2)
        # self.click(Locators.MANAGE_DATA_SUBMIT)
        # time.sleep(2)

        self.click(Locators.MANAGE_DATA_CLICK)
        time.sleep(2)
        self.click(Locators.MANAGE_DATA_CHECKBOX)
        time.sleep(2)
        self.click(Locators.MANAGE_DATA_EDIT)
        time.sleep(2)
        self.click(Locators.MANAGE_DATA_THRID_INPUT)
        time.sleep(2)
        self.static_dropdown(Locators.MANAGE_DATA_OPTION, "No")
        time.sleep(2)
        self.click(Locators.MANAGE_DATA_SUBMIT)
        time.sleep(2)



