import time

from Utilities.base import Basepage
from Utilities.locators import Locators
from Utilities.logger_file import GetLogger


class Actiontracker(Basepage, GetLogger):

    def __init__(self, driver):
        super().__init__(driver)

    def action_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.ACTION_TRACKER)
        time.sleep(2)
        self.dropdown_click(Locators.ACTION_ITEM, 1, "Test")
        time.sleep(2)
        self.dropdown_click(Locators.ACTION_TRACKER_STAGE, 1, "Created")
        time.sleep(2)
        self.dropdown_click(Locators.ACTION_ASSIGN_TO, 1, "Compliance User")
        time.sleep(2)
        self.dropdown_click(Locators.ACTION_ASSIGN_BY, 1, "Compliance User")
        time.sleep(2)
        self.dropdown_click(Locators.ACTION_PRIORITY, 1, "High")
        time.sleep(2)
        self.dropdown_click(Locators.ASSIGN_NEXT, 1, "30 Days")
        time.sleep(2)
        self.click(Locators.ACTION_EDIT)
        time.sleep(2)
        self.clear(Locators.EDIT_ITEM)
        time.sleep(2)

        self.send_keys(Locators.EDIT_ITEM, "DEMO1")
        time.sleep(2)
        self.send_keys(Locators.EDIT_ECD, "29-02-2023")
        time.sleep(2)
        self.static_dropdown(Locators.EDIT_PRIORITY, "High")
        time.sleep(2)
        self.click(Locators.EDIT_SUBMIT)
        time.sleep(2)
        # self.click(Locators.ACTION_DELETE)
        # time.sleep(2)
        #
        #
        # try:
        #     self.get_logger().info(
        #     self.driver.switch_to.alert.text)
        #
        #     self.driver.switch_to.alert.accept()
        # except:
        #     self.get_logger().error("There is no alert message")

        # self.drag_and_drop(Locators.SOURCE,Locators.TARGET)
        # time.sleep(2)
