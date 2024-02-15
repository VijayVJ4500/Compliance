import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class ChecklistReport(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def checklistreport_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.REPORTS)
        time.sleep(2)
        self.click(Locators.CHECKLIST)
        time.sleep(2)
        # self.dropdown_click(Locators.COMP_CODE_LIST,1,"GJI")
        # time.sleep(2)
        self.dropdown_click(Locators.SORT_BY,1,"Building Safety")
        time.sleep(2)
        self.click(Locators.REPORT_PERIOD)
        time.sleep(2)
        self.static_dropdown(Locators.REPORT_PERIOD_LIST, "This Month")
        time.sleep(2)
        self.click(Locators.PDF_DOWNLOAD)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.click(Locators.EXCEL_DOWNLOAD)
        time.sleep(2)

        self.click(Locators.CHECK_VIEW_REPORT)
        time.sleep(2)
        # self.click(Locators.IMAGE_VIEW)
        # time.sleep(2)


