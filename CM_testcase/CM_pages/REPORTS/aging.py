import time



from Utilities.base import Basepage
from Utilities.locators import Locators


class AgingReport(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def agingreport_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.REPORTS)
        time.sleep(2)
        self.click(Locators.AGING_REPORT)
        time.sleep(2)
        self.dropdown_click(Locators.AGING_ACTION_STAGE, 1, "Completed")
        time.sleep(2)
        self.dropdown_click(Locators.AGING_ASSIGN_TO, 1, "Compliance User ")
        time.sleep(2)

        self.click(Locators.ECD_DATE)
        time.sleep(2)
        self.click(Locators.NEXT_MONTH)
        time.sleep(2)
        self.click(Locators.ECD_DATE_BOX)
        time.sleep(2)

        self.click(Locators.PDF_DOWNLOAD)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.click(Locators.EXCEL_DOWNLOAD)
        time.sleep(2)

        # self.specific_horizontal_scroll(Locators.SCROLL, 200)
        # time.sleep(2)
        # print(self.is_element_clickable(Locators.AGING_VIEW))
        # self.click(Locators.AGING_VIEW)
        # print("clickable")
        # time.sleep(2)
        # self.click(Locators.OUTSIDE_CLICK)
        # time.sleep(2)

        # self.click(Locators.CLOSE)

        # self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(Locators.RESET)
        time.sleep(2)


