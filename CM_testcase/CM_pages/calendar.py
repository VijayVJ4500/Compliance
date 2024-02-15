import time

from Utilities.base import Basepage
from Utilities.locators import Locators
from Utilities.logger_file import GetLogger


class Calendar(Basepage, GetLogger):

    def __init__(self, driver):
        super().__init__(driver)

    def calendar_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CALENDER)
        time.sleep(2)
        self.click(Locators.CAL_ADD)
        time.sleep(2)
        self.send_keys(Locators.CAL_EVENT_NAME, "Daily once")
        time.sleep(2)
        self.send_keys(Locators.EVENT_DESC, "Daliy once Event")
        time.sleep(2)
        self.send_keys(Locators.START_DATE, "11-12-2023")
        time.sleep(2)
        self.clear(Locators.CAL_REPEAT)
        time.sleep(2)
        self.send_keys(Locators.CAL_REPEAT, "1")
        time.sleep(2)
        # self.static_dropdown(Locators.CAL_REPEAT_DAY, "Day")
        # time.sleep(2)
        self.click(Locators.CAL_HOURSLY)
        time.sleep(2)
        self.send_keys(Locators.CAL_REP_HRS, "00:30:00")
        time.sleep(2)
        self.send_keys(Locators.CAL_START_TIME, "10:00")
        time.sleep(2)
        self.send_keys(Locators.CAL_END_TIME, "18:00")
        time.sleep(2)
        self.send_keys(Locators.END_DATE, "20-12-2023")
        time.sleep(2)


        self.click(Locators.CAL_SUBMIT)
        time.sleep(2)
        # self.click(Locators.CAL_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.CAL_EDIT)
        # time.sleep(2)
        # self.send_keys(Locators.CAL_EDIT_START_TIME, "12-12-2023")
        # time.sleep(2)
        # self.click(Locators.CAL_UPDATE)
        # time.sleep(2)
        # self.click(Locators.CAL_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.CAL_DELETE)
        # time.sleep(2)
        # self.click(Locators.CAL_DELETE_YES)
        # time.sleep(2)

        #Click the submit button without enter the data
        # self.click(Locators.MENU)
        # time.sleep(2)
        # self.click(Locators.CALENDER)
        # time.sleep(2)
        # self.click(Locators.CAL_ADD)
        # time.sleep(2)
        # self.click(Locators.CAL_SUBMIT)
        # time.sleep(2)
        # self.required_error_msg(Locators.CAL_ALL_REQ_MSG)
        # time.sleep(2)
