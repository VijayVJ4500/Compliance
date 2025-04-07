import time
import unittest


from hrm_automation.base import BasePage
from hrm_automation.locators import Locators


class payconfig(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """

    def __init__(self, driver):
        super().__init__(driver)

    def payconfig_tab(self):
        time.sleep(2)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.click(Locators.PAYROLL_CARD)
        time.sleep(2)
    def search(self):
        self.enter_text(Locators.PAYROLL_SEARCH,"Eric Peck")
        time.sleep(5)
        self.click(Locators.PAY_RESET)
        time.sleep(3)


    def pay_assign(self):
        self.click(Locators.PAYROLL_ASSIGN)
        time.sleep(3)
        self.dropdown_click(Locators.PAY_TEMP,2)
        time.sleep(2)
        self.click(Locators.PAY_UPDATE)
        time.sleep(2)
        self.enter_text(Locators.PAYROLL_ASSIGN_EARNING,"23822")
        time.sleep(2)
        self.enter_text(Locators.PAYROLL_ASSIGN_DEDUCTION, "25222666")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.clear(Locators.PAYROLL_ASSIGN_EARNING)
        time.sleep(1)
        self.clear(Locators.PAYROLL_ASSIGN_DEDUCTION)
        time.sleep(1)
        self.enter_text(Locators.PAYROLL_ASSIGN_EARNING, "2")
        time.sleep(2)
        self.enter_text(Locators.PAYROLL_ASSIGN_DEDUCTION, "2")
        time.sleep(2)
        self.click(Locators.PAYROLL_ASSIGN_SAVE_2)
        time.sleep(5)

    def pay_edit(self):
        self.click(Locators.PAYROLL_EDIT)
        time.sleep(10)
        self.dropdown_click(Locators.PAY_TEMP,1)
        time.sleep(4)
        self.click(Locators.PAYROLL_EDIT_UPDATE)
        time.sleep(2)
        self.clear(Locators.PAYROLL_EDIT_EARNING1)
        time.sleep(2)
        self.clear(Locators.PAYROLL_EDIT_DEDUCTION1)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        # self.click(Locators.PAYROLL_EDIT_UPDATE)
        # time.sleep(2)
        # try:
        #     self.assertEqual(self.driver.current_url, 'https://ipss.asset.techgenzi.com/employee/paylist')
        #     self.get_logger().info("All amount are coming in extra earning")
        #
        #     self.click(Locators.PAYROLL_EDIT)
        #     time.sleep(10)
        #     self.dropdown_click(Locators.PAY_TEMP, 1)
        #     time.sleep(4)
        #     self.click(Locators.PAYROLL_EDIT_UPDATE)
        #     time.sleep(2)
        #     self.clear(Locators.PAYROLL_EDIT_EARNING1)
        #     time.sleep(1)
        #     self.clear(Locators.PAYROLL_EDIT_DEDUCTION1)
        #     time.sleep(1)
        # self.enter_text(Locators.PAYROLL_EDIT_EARNING1, "5")
        # time.sleep(2)
        # self.enter_text(Locators.PAYROLL_EDIT_DEDUCTION1, "5")
        # time.sleep(2)
        # self.driver.execute_script("window.scrollBy(0,300)")
        # time.sleep(2)
        # self.click(Locators.PAYROLL_EDIT_SAVE)
        # time.sleep(2)
        #
        #
        #
        # except:
        #     self.get_logger().error("All amount should not be in extra earning")

        self.enter_text(Locators.PAYROLL_EDIT_EARNING1, "2")
        time.sleep(2)
        self.enter_text(Locators.PAYROLL_EDIT_DEDUCTION1, "2")
        time.sleep(2)
        self.click(Locators.PAYROLL_EDIT_SAVE)
        time.sleep(2)



    def payconfig_page(self):
        self.payconfig_tab()
        self.search()
        self.pay_assign()
        self.pay_edit()
