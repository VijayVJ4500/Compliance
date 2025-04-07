import unittest
from hrm_automation.test_base import TestBase
from hrm_automation.hrm_test_cases.Idcard_detail import Idcard
from hrm_automation.hrm_test_cases.Import_biometrics import biometrics
from hrm_automation.hrm_test_cases.Presentdays_report import presentdays_report
from hrm_automation.hrm_test_cases.Rawdata import Rawdata
from hrm_automation.hrm_test_cases.Resign import resign
from hrm_automation.hrm_test_cases.absentee_report import Absentees_report
from hrm_automation.hrm_test_cases.approval_process import approve
from hrm_automation.hrm_test_cases.assign import assign
from hrm_automation.hrm_test_cases.attendance import attendance
from hrm_automation.hrm_test_cases.attendance_config import att_confg
from hrm_automation.hrm_test_cases.attendance_summary import attsum
from hrm_automation.hrm_test_cases.authentication.login import LoginPage
from hrm_automation.hrm_test_cases.authentication.logout import Logout
from hrm_automation.hrm_test_cases.biometric_log import BiometricHistory_report
from hrm_automation.hrm_test_cases.configure_payroll import PayrollConfiguration
# from hrm_automation.hrm_test_cases.configure_payroll import PayrollConfiguration
from hrm_automation.hrm_test_cases.continuous_leave import Contleave
from hrm_automation.hrm_test_cases.dashboard import dashboard
from hrm_automation.hrm_test_cases.define_bulk import define_bulk_page
from hrm_automation.hrm_test_cases.define_pay import define_pay_page
from hrm_automation.hrm_test_cases.emp import Employee2
from hrm_automation.hrm_test_cases.employee_history import employe_history
from hrm_automation.hrm_test_cases.employee_report import Employee_report
from hrm_automation.hrm_test_cases.form25 import form25
from hrm_automation.hrm_test_cases.form25b import form25b
from hrm_automation.hrm_test_cases.lateentry_report import Late_entry
from hrm_automation.hrm_test_cases.leave_status import leave_status
# from hrm_automation.hrm_test_cases.emp import Employee2
from hrm_automation.hrm_test_cases.leaveconfig import Leaveconfig
from hrm_automation.hrm_test_cases.manage_pay import manage_pay_page
from hrm_automation.hrm_test_cases.manpower import Manpower_Report
from hrm_automation.hrm_test_cases.modification import modify
from hrm_automation.hrm_test_cases.musterday import muster
from hrm_automation.hrm_test_cases.ot_report import OT_Report
from hrm_automation.hrm_test_cases.pay_config import payconfig
from hrm_automation.hrm_test_cases.pay_generation import pay_generation_page
from hrm_automation.hrm_test_cases.pay_status import pay_status_page
from hrm_automation.hrm_test_cases.payroll_csv import pay_csv_page
from hrm_automation.hrm_test_cases.payrolllog import Payrollog_report
from hrm_automation.hrm_test_cases.payslip import pay_slip_page
from hrm_automation.hrm_test_cases.paytable import paytable_report
from hrm_automation.hrm_test_cases.permission_report import Permission_Report
from hrm_automation.hrm_test_cases.pf_esi import PF_ESI
from hrm_automation.hrm_test_cases.sequence import sequence
from hrm_automation.hrm_test_cases.shift import shift
from hrm_automation.hrm_test_cases.stat import Stat
from hrm_automation.hrm_test_cases.template import template_page
from hrm_automation.hrm_test_cases.user_userrole import User

from hrm_automation.hrm_test_cases.leave_management import LeaveManagement
from hrm_automation.hrm_test_cases.Configuration import Configuration
from hrm_automation.hrm_test_cases.WFH import WFHManagement
from hrm_automation.hrm_test_cases.WFH_negative import WFHManagementNegative
from hrm_automation.hrm_test_cases.onduty_management import OnDutyManagement
from hrm_automation.hrm_test_cases.leave_management_negative import LeaveManagementNegative
from hrm_automation.hrm_test_cases.onduty_management_negative import OnDutyManagementNegative
from hrm_automation.hrm_test_cases.permission_management import PermissionManagement
from hrm_automation.hrm_test_cases.permission_management_negative import PermissionManagementNegative


class AllTests(TestBase):
    """
    Run all test cases here
    """

    def setUp(self) -> None:
        """
        Chrome driver setup from Base class
        :return:
        """
        super().setUp()

    def test_b_config(self):
        self.login = LoginPage(self.driver)
        self.login.login_page()

        # # Configuration
        # self.config = Configuration(self.driver)
        # self.config.do_configurtion()
        # self.sequence = sequence(self.driver)
        # self.sequence.sequence_tab()        
        # self.con_shift = shift(self.driver)
        # self.con_shift.shift_page()
        # self.assign1 = assign(self.driver)
        # self.assign1.assign_tab()
        # self.leave = Leaveconfig(self.driver)
        # self.leave.leave_page()
        # self.conpay = PayrollConfiguration(self.driver)
        # self.conpay.configure_pay()
       

        # Employee
        # self.emp2 = Employee2(self.driver)
        # self.emp2.emp_config2()
        # self.idcarddet = Idcard(self.driver)
        # self.idcarddet.idcard_page()
        # self.resig = resign(self.driver)
        # self.resig.resign_page()
        # self.employee_report = Employee_report(self.driver)
        # self.employee_report.employee_report_page()
        # self.statuatory = Stat(self.driver)
        # self.statuatory.stat_page()
        # self.emp_his = employe_history(self.driver)
        # self.emp_his.employe_history()

        # # attendance Module
        # self.biometric = biometrics(self.driver)
        # self.biometric.biometrics_page()
        # self.att_config = att_confg(self.driver)
        # self.att_config.attconfg_page()
        # self.atten = attendance(self.driver)
        # self.atten.attendance()
        # self.approval = approve(self.driver)
        # self.approval.approve_page()
        # self.modification = modify(self.driver)
        # self.modification.modify_page()
        # self.rawdata = Rawdata(self.driver)
        # self.rawdata.rawdata_page()
        # self.biohis=BiometricHistory_report(self.driver)
        # self.biohis.biodata()

        # payroll module
        # self.definepay = define_pay_page(self.driver)
        # self.definepay.define_pay()
        # self.definepay_bulk = define_bulk_page(self.driver)
        # self.definepay_bulk.define_pay_bulk()
        # self.managepay = manage_pay_page(self.driver)
        # self.managepay.manage_pay()
        # self.temp = template_page(self.driver)
        # self.temp.template()
        # self.paygen = pay_generation_page(self.driver)
        # self.paygen.pay_generation()
        # self.paysts = pay_status_page(self.driver)
        # self.paysts.pay_status()
        # self.paycsv = pay_csv_page(self.driver)
        # self.paycsv.pay_csv()
        # self.payslip = pay_slip_page(self.driver)
        # self.payslip.pay_slip()
        # self.paytablereport = paytable_report(self.driver)
        # self.paytablereport.paytable()
        # self.paylog=Payrollog_report(self.driver)
        # self.paylog.payroll_data()

        # REPORTS
        # self.muster_report = muster(self.driver)
        # self.muster_report.musterday()
        # self.dashboard_page = dashboard(self.driver)
        # self.dashboard_page.dash()
        # self.contleave = Contleave(self.driver)
        # self.contleave.continouse_leave()
        # self.leave_sts = leave_status(self.driver)
        # self.leave_sts.leavestatus()
        # self.lateentry_report = Late_entry(self.driver)
        # self.lateentry_report.lateentry()
        # self.pfandesi = PF_ESI(self.driver)
        # self.pfandesi.pfesi()
        # self.otreport = OT_Report(self.driver)
        # self.otreport.ot()
        # self.permissionreport = Permission_Report(self.driver)
        # self.permissionreport.permission()
        # self.manpower_report = Manpower_Report(self.driver)
        # self.manpower_report.manpower()
        # self.presendays_report = presentdays_report(self.driver)
        # self.presendays_report.presentdays()
        # self.absent_report = Absentees_report(self.driver)
        # self.absent_report.absentees()
        # self.form25page = form25(self.driver)
        # self.form25page.form25()
        # self.form25bpage = form25b(self.driver)
        # self.form25bpage.form25b()

        # self.user = User(self.driver)
        # self.user.userrole()
        # self.log_out = Logout(self.driver)
        # self.log_out.do_logout()



        # self.leave_management = LeaveManagement(self.driver)
        # self.leave_management.leave_management_page()
        # self.leave_management_negative = LeaveManagementNegative(self.driver)
        # self.leave_management_negative.run_all_negative_tests()
        # self.onduty_management = OnDutyManagement(self.driver)
        # self.onduty_management.onduty_management_flow()
        # self.onduty_management_negative = OnDutyManagementNegative(self.driver)
        # self.onduty_management_negative.run_all_negative_tests()
        # self.WFH_management = WFHManagement(self.driver)
        # self.WFH_management.WFH_management_flow()
        # self.WFH_management_negative = WFHManagementNegative(self.driver)
        # self.WFH_management_negative.run_all_negative_tests()
        # permission_tests = PermissionManagement(self.driver)
        # permission_tests.permission_management_flow()
        # permission_neg_tests = PermissionManagementNegative(self.driver)
        # permission_neg_tests.run_negative_tests()




# class Alltest2(TestBaseFireFox):
#     def test_c_c.onfig(self):
#         self.login = Login(self.driver)
#         self.login.do_login()
#         self.employee = Employee(self.driver)
#         self.employee.emp_confg()

if __name__ == "__main__":
    test_suite = unittest.TestSuite()
    test_suite.addTest(AllTests('test_b_config'))
    # test_suite.addTest(Alltest2('test_c_config'))
    unittest.TextTestRunner().run(test_suite)
