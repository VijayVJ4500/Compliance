import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Datatable(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def datatable_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.DATA_TABLE)
        time.sleep(2)
        self.click(Locators.DATATABLE_ADD)
        time.sleep(2)
        # First Data
        self.enter_text(Locators.DATATABLE_CATEGORY, "Externals Data")
        time.sleep(2)
        self.send_keys(Locators.DATATABLE_CATEGORY_DESC, "Data")
        time.sleep(2)
        self.enter_text(Locators.DATATABLE_LABEL1, "Policy")
        time.sleep(2)
        self.click(Locators.DATATABLE_QUESTION_TYPE)
        time.sleep(2)
        self.dropdown_click(Locators.DATATABLE_QUES_TYPE_LIST, 1, "Text")
        time.sleep(2)
        self.click(Locators.DATABLE_VALID_QUES_TYPE)
        time.sleep(2)
        self.static_dropdown(Locators.DATABLE_VALID_QUES_TYPE_LIST, "Special Text")
        time.sleep(2)
        self.click(Locators.SPECIAL_TEXT_TYPE)
        time.sleep(2)
        self.static_dropdown(Locators.SPECIAL_TEXT_TYPE_LIST,  "PAN No")

        # Second document
        self.click(Locators.DATABLE_DUPLICATE)
        time.sleep(2)
        self.scroll_down(500)
        time.sleep(2)
        self.clear(Locators.DATATABLE_LABEL2)
        time.sleep(2)
        self.enter_text(Locators.DATATABLE_LABEL2, "Rule Name")
        time.sleep(2)
        self.click(Locators.DATA_VALID_TYPE)
        time.sleep(2)
        self.static_dropdown(Locators. DATABLE_VALID_QUES_TYPE_LIST, "Regex")
        time.sleep(2)
        self.enter_text(Locators.DATATABLE_REGEX_PATTERN, "^[a-zA-Z ]*$")
        time.sleep(2)
        self.click(Locators.DATATABLE_SUBMIT)
        time.sleep(2)

        ##Thrid doc
        self.click(Locators.DATATABLE_CLICK)
        time.sleep(2)
        self.click(Locators.DATATABLE_EDIT)
        time.sleep(2)
        self.scroll_down(500)
        time.sleep(2)
        self.click(Locators.DATATABLE_ADDLABEL)
        time.sleep(2)
        self.scroll_down(500)
        time.sleep(2)
        self.enter_text(Locators.DATATABLE_LABEL3,"Law Name")
        time.sleep(2)
        self.click(Locators. DATATABLE_QUESTION_TYPE2)
        time.sleep(2)
        self.static_dropdown(Locators. DATATABLE_QUES_TYPE_LIST,"Dropdown")
        time.sleep(2)
        self.click(Locators.DATABLE_OPTION)
        time.sleep(2)
        self.clear(Locators. DATABLE_OPTION_TEXT)
        time.sleep(2)
        self.enter_text(Locators.DATABLE_OPTION_TEXT,"N/A")
        time.sleep(2)
        self.scroll_down(500)
        time.sleep(2)
        self.click(Locators.DATATABLE_SUBMIT)
        time.sleep(2)
