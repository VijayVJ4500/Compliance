import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators


class attsum(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def attsum_tab(self):
        time.sleep(1)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.click(Locators.ATT_SUM_CARD)
        time.sleep(6)


    def ot_app(self):

    #OT opprove
        self.click(Locators.AS_OT_DATE_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_SEARCH_BT)
        time.sleep(1)
        self.click(Locators.AS_OT_CHECK_1)
        time.sleep(1)
        self.click(Locators.AS_OT_APP)
        time.sleep(5)

    #check the filters
        self.click(Locators.AS_OT_DATE_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_SEARCH_BT)
        time.sleep(1)
        self.enter_text(Locators.AS_OT_ID_FIL,11)
        time.sleep(1)
        self.dropdown_click(Locators.AS_OT_BAND_FIL,2)
        time.sleep(1)
        self.click(Locators.AS_OT_RESET_BT)
        time.sleep(1)
    def ot_edit(self):
        self.click(Locators.AS_OT_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_OT_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_SEARCH_BT)
        time.sleep(1)
        self.click(Locators.AS_OT_EDIT)
        time.sleep(1)
        self.enter_text(Locators.AS_OT_EDIT_HOURS, "1.2")
        time.sleep(1)
        self.click(Locators.AS_OT_EDIT_MOD_APP)
        time.sleep(4)
        self.click(Locators.AS_OT_RESET_BT)
        time.sleep(3)
    def ot_revert(self):

        self.click(Locators.AS_OT_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_OT_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_OT_SEARCH_BT)
        time.sleep(1)
        self.click(Locators.AS_OT_REVERT)
        time.sleep(1)
        self.click(Locators.AS_OT_CHECK_1)
        time.sleep(1)
        self.click(Locators.AS_OT_REJECT)
        time.sleep(1)
    def leave_app(self):
        self.click(Locators.AS_LEAVE_RADIO)
        time.sleep(1)
    #leave approve without declare leave
        self.click(Locators.AS_LEAVE_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_LEAVE_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_SEARCH)
        time.sleep(3)
        self.click(Locators.AS_LEAVE_CHECK1)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_DECLARE)
        time.sleep(1)
        self.dropdown_click(Locators.AS_LEAVE_TYPE,1)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_SUBMIT)
        time.sleep(1)
        # leave approve
        # self.click(Locators.AS_LEAVE_DATE_FIL)
        # time.sleep(2)
        # self.click(Locators.AS_LEAVE_MONTH_FIL)
        # time.sleep(1)
        # self.click(Locators.AS_LEAVE_SEARCH)
        # time.sleep(3)
        # self.click(Locators.AS_LEAVE_CHECK1)
        # time.sleep(1)
        # self.dropdown_click(Locators.AS_LEAVE_TYPE,1)
        # time.sleep(1)
        # self.click(Locators.AS_LEAVE_SUBMIT)
        # time.sleep(1)

    #to check all the filters are working
        self.click(Locators.AS_OT_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_LEAVE_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_SEARCH)
        time.sleep(1)
        self.enter_text(Locators.AS_LEAVE_ID, 11)
        time.sleep(1)
        self.dropdown_click(Locators.AS_LEAVE_BAND_FIL, 2)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_ALL_FIL)
        time.sleep(2)
        self.click(Locators.AS_LEAVE_ALL)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_RESET)
        time.sleep(1)
    def leave_revert(self):
        self.click(Locators.AS_LEAVE_REVERT)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_LEAVE_MONTH_FIL)
        time.sleep(1)
        self.click(Locators.AS_LEAVE_SEARCH)
        time.sleep(3)
        self.click(Locators.AS_LEAVE_CHECK1)
        time.sleep(2)
        self.click(Locators.AS_LEAVE_REJECT)
        time.sleep(1)

    def od_app(self):
        self.click(Locators.AS_OD_RADIO)
        time.sleep(3)
        self.click(Locators.AS_LEAVE_REVERT)
        time.sleep(1)
        # od approve
        self.click(Locators.AS_OD_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_OD_MONTH)
        time.sleep(1)
        self.click(Locators.AS_OD_SEARCH)
        time.sleep(1)
        self.click(Locators.AS_OD_CHECK)
        time.sleep(1)
        self.click(Locators.AS_OD_APP)
        time.sleep(1)
        # to check all the filters are working
        self.click(Locators.AS_OD_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_OD_MONTH)
        time.sleep(1)
        self.click(Locators.AS_OD_SEARCH)
        time.sleep(1)
        self.enter_text(Locators.AS_OD_ID_FIL, 11)
        time.sleep(1)
        self.dropdown_click(Locators.AS_OD_BAND_FIL, 2)
        time.sleep(1)
        self.click(Locators.AS_OD_RESET)
        time.sleep(1)

    def od_revert(self):
        self.click(Locators.AS_OD_REVERT)
        time.sleep(1)
        self.click(Locators.AS_OD_DATE_FIL)
        time.sleep(2)
        self.click(Locators.AS_OD_MONTH)
        time.sleep(1)
        self.click(Locators.AS_OD_SEARCH)
        time.sleep(1)
        self.click(Locators.AS_OD_CHECK)
        time.sleep(1)
        self.click(Locators.AS_OD_REJECT)
        time.sleep(1)



    def attsum_page(self):
        self.attsum_tab()
        # self.ot_app()
        # self.ot_edit()
        # self.ot_revert()
        self.leave_app()
        self.leave_revert()
        self.od_app()
        self.od_revert()
