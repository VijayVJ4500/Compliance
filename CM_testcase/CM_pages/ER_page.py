import time

from Utilities.base import Basepage
from Utilities.locators import Locators
from Utilities.logger_file import GetLogger


class Establish_realation(Basepage, GetLogger):

    def __init__(self, driver):
        super().__init__(driver)

    def er_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.ESTABLISH_RELATION)
        time.sleep(2)
        self.click(Locators.ER_ADD)
        time.sleep(2)
        self.dropdown_click(Locators.FIRST_ASSET_TYPE, 1, "Calendar")
        time.sleep(2)
        self.dropdown_click(Locators.SEC_ASSET_TYPE, 1, "Form Data")
        time.sleep(2)
        self.static_dropdown(Locators.ASSET_MAPPING, "One To Many")
        time.sleep(2)
        self.click(Locators.ER_SUBMIT)
        time.sleep(2)
        # self.click(Locators.ER_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.ER_EDIT)
        # time.sleep(2)
        # self.click(Locators.ASS_MAP_CLICK)
        # time.sleep(2)
        # self.static_dropdown(Locators.ASS_MAP_ER_EDIT, "One To Many")
        # time.sleep(2)
        #
        # self.click(Locators.ER_UPDATE)
        # time.sleep(2)
        # self.click(Locators.ER_DELETE)
        # time.sleep(2)
        # self.click(Locators.ER_DELETE_YES)
        # time.sleep(2)
        # self.click(Locators.ER_SUBMIT)
        # time.sleep(2)
        # self.required_error_msg(Locators.ER_ASSET_REQ_MSG)
        # time.sleep(2)

        # Negative Case ***
        # Clicking the Add button when checkbox is selected

        # self.click(Locators.ER_CHECKBOX)
        # time.sleep(1)
        #
        # self.click(Locators.ER_ADD)
        # time.sleep(2)
        #
        # try:
        #     self.get_logger().info(self.driver.switch_to.alert.text)
        #     self.driver.switch_to.alert.accept()
        # except:
        #     self.get_logger().error("There is no alert message")

        # Clicking the Edit button when checkbox is  not selected
        self.click(Locators.ER_EDIT)
        time.sleep(2)

        try:
            self.get_logger().info(self.driver.switch_to.alert.text)
            self.driver.switch_to.alert.accept()
        except:
            self.get_logger().error("There is no alert message")
