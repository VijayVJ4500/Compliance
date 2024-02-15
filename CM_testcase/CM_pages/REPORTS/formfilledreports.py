import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class FormfilledReport(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def formfilledreport_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.REPORTS)
        time.sleep(2)
        self.click(Locators.FORMFILLED_REPORT)
        time.sleep(2)

        self.click(Locators.REPORT_PERIOD)
        time.sleep(2)
        self.static_dropdown(Locators.REPORT_PERIOD_LIST,"This Month")
        time.sleep(2)
        self.click(Locators.PDF_DOWNLOAD)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.click(Locators.EXCEL_DOWNLOAD)
        time.sleep(2)
        print(self.is_element_clickable(Locators.FORMFILL_VIEW_REPORT))
        self.click(Locators.FORMFILL_VIEW_REPORT)
        time.sleep(2)
        self.click(Locators.REPORT_ASSIGN)
        time.sleep(2)
        self.send_keys(Locators.ASSIGN_ITEM,"Test")
        time.sleep(2)
        self.dropdown_click(Locators.ASSIGN_TO,1,"Compliance User")
        time.sleep(2)
        self.send_keys(Locators.EXPECTED_DATE,"10/2/2024")
        time.sleep(2)
        self.dropdown_click(Locators.PRIORITY,1,"High")
        time.sleep(2)
        self.click(Locators.ASS_SUBMIT)
        time.sleep(2)

        #Click the submit button without entering any data
        # self.click(Locators.REPORT_PERIOD)
        # time.sleep(2)
        # self.static_dropdown(Locators.REPORT_PERIOD_LIST,"Previous Week")
        # time.sleep(2)
        # self.click(Locators.FORMFILL_VIEW_REPORT)
        # time.sleep(2)
        # self.click(Locators.REPORT_ASSIGN)
        # time.sleep(2)
        # self.click(Locators.ASS_SUBMIT)
        # time.sleep(2)
        # self.required_error_msg(Locators.FORMFILL_ASSIGN_ALL_REQ_MSG)
        # time.sleep(2)





