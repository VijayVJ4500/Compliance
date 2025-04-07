# leave.py
from config import num_requests, num_threads
from load_test.Assign.holiday_assign import holiassign
from load_test.Assign.leave_assign import leaveassign
from load_test.Assign.shift_assign import shiftassign
from load_test.Assign.weekoff_assign import weekoffassign
from load_test.Sequence.sequence_add import sequenceadd
from load_test.Sequence.sequence_delete import sequencedelete
from load_test.Sequence.sequence_edit import sequenceedit
from load_test.Sequence.sequence_get_all import sequenceget
from load_test.base_configuration.attrition_add import attritionadd
from load_test.base_configuration.attrition_delete import attritiondelete
from load_test.base_configuration.attrition_edit import attritionedit
from load_test.base_configuration.attrition_get_all import attritionget
from load_test.base_configuration.band_add import bandadd
from load_test.base_configuration.band_delete import banddelete
from load_test.base_configuration.band_edit import bandedit
from load_test.base_configuration.band_get_all import bandget
from load_test.base_configuration.dept_add import deptadd
from load_test.base_configuration.dept_delete import deptdelete
from load_test.base_configuration.dept_edit import deptedit
from load_test.base_configuration.dept_get_all import deptget
from load_test.base_configuration.desg_add import desgadd
from load_test.base_configuration.desg_delete import desgdelete
from load_test.base_configuration.desg_edit import desgedit
from load_test.base_configuration.desg_get_all import desgget
from load_test.leave_config.leave_add import Leaveadd
from load_test.leave_config.leave_delete import Leavedelete
from load_test.leave_config.leave_edit import Leaveedit
from load_test.leave_config.leave_get_all import Leaveget
from load_test.shift_config.shift_add import shiftadd
from load_test.shift_config.shift_delete import shiftdelete
from load_test.shift_config.shift_edit import shiftedit
from load_test.shift_config.shift_get_all import shiftget


class AllTests:
    """
    Run all test cases here
    """
    def test_leave(self):
        # Initialize the classes
        #
        # #Leave configuration
        # self.leave_add = Leaveadd(self)
        # self.leave_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
        # self.leave_edit = Leaveedit(self)
        # self.leave_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.leave_get = Leaveget(self)
        # self.leave_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
        # self.leave_delete = Leavedelete(self)
        # self.leave_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

        # #Sequence
        # self.sequence_add = sequenceadd(self)
        # self.sequence_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
        # self.sequence_edit = sequenceedit(self)
        # self.sequence_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.sequence_get = sequenceget(self)
        # self.sequence_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
        # self.sequence_delete = sequencedelete(self)
        # self.sequence_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

        # #shift
        # self.shift_add = shiftadd(self)
        # self.shift_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
        # self.shift_edit = shiftedit(self)
        # self.shift_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.shift_get = shiftget(self)
        # self.shift_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
        # self.shift_delete = shiftdelete(self)
        # self.shift_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

        # #Assignn
        # self.holiday_add = holiassign(self)
        # self.holiday_add.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.shift_assign = shiftassign(self)
        # self.shift_assign.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.leave_assign = leaveassign(self)
        # self.leave_assign.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        self.weekoff_assign = weekoffassign(self)
        self.weekoff_assign.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)

        # attrition
        # self.attrition_add = attritionadd(self)
        # self.attrition_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
        # self.attrition_edit = attritionedit(self)
        # self.attrition_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
        # self.attrition_get = attritionget(self)
        # self.attrition_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
        # self.attrition_delete = attritiondelete(self)
        # self.attrition_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

 # band
 #        self.band_add = bandadd(self)
 #        self.band_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.band_edit = bandedit(self)
 #        self.band_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.band_get = bandget(self)
 #        self.band_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.band_delete = banddelete(self)
 #        self.band_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

 # department
 #        self.dept_add = deptadd(self)
 #        self.dept_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.dept_edit = deptedit(self)
 #        self.dept_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.dept_get = deptget(self)
 #        self.dept_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.dept_delete = deptdelete(self)
 #        self.dept_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)

 # # designation
 #        self.desg_add = desgadd(self)
 #        self.desg_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.desg_edit = desgedit(self)
 #        self.desg_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.desg_get = desgget(self)
 #        self.desg_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.desg_delete = desgdelete(self)
 #        self.desg_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)
 # # department
 #        self.shift_add = shiftadd(self)
 #        self.shift_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_edit = shiftedit(self)
 #        self.shift_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_get = shiftget(self)
 #        self.shift_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_delete = shiftdelete(self)
 #        self.shift_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)
 # # department/
 #        self.shift_add = shiftadd(self)
 #        self.shift_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_edit = shiftedit(self)
 #        self.shift_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_get = shiftget(self)
 #        self.shift_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_delete = shiftdelete(self)
 #        self.shift_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)
 # # department
 #        self.shift_add = shiftadd(self)
 #        self.shift_add.load_test_concurrent_users(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_edit = shiftedit(self)
 #        self.shift_edit.load_test_concurrent_patch_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_get = shiftget(self)
 #        self.shift_get.load_test_concurrent_get_requests(num_requests=num_requests, num_threads=num_threads)
 #        self.shift_delete = shiftdelete(self)
 #        self.shift_delete.load_test_concurrent_delete_requests(num_requests=num_requests, num_threads=num_threads)



if __name__ == "__main__":
    all_tests = AllTests()
    all_tests.test_leave()
