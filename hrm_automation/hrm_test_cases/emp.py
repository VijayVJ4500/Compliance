import random
import re
import string
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from driver import driver
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from google.auth.transport import requests

from selenium.webdriver.support.wait import WebDriverWait

from hrm_automation import headers
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import requests
from hrm_automation.logger_file import get_logger

# Get logger instance
logger = get_logger('Employee')

class Employee2(BasePage, unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.fake = Faker()
        self.logger = get_logger("Employee")

    def emp_tab(self):
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.click(Locators.EMP_CARD)
        time.sleep(3)

    def search(self):
        self.click(Locators.EMP_SEARCH)
        time.sleep(1)
        self.enter_text(Locators.SEARCH_NAME, self.fake.random_int(100000000000, 999999999999))  # Using faker for generating name
        time.sleep(1)
        self.clear(Locators.SEARCH_NAME)
        time.sleep(1)
        self.enter_text(Locators.SEARCH_NAME, self.fake.name())  # Using faker for generating name
        time.sleep(1)
        self.click(Locators.SEARCH_CLOSE)
        time.sleep(1)
        self.clear(Locators.EMP_SEARCH_BT)
        time.sleep(1)
        self.enter_text(Locators.EMP_SEARCH_BT, "Karthik")
        time.sleep(5)
        self.click(Locators.VIEW)
        time.sleep(2)
        self.click(Locators.PROFILE_DOWNLOAD)
        time.sleep(4)
        self.click(Locators.PRO_EDIT)
        time.sleep(10)
        self.click(Locators.PRO_EMP_GO)
        time.sleep(2)
        self.click(Locators.PRO_GO)
        time.sleep(1)
        self.logger.info('Employee Searching Functionality is Working fine')

    def quick(self):
        # Check the cancel button
        self.click(Locators.QUICKONBOARD)
        time.sleep(1)
        self.click(Locators.QCANCEL)
        time.sleep(1)
        # Add the quick onboard without any details
        self.click(Locators.QUICKONBOARD)
        time.sleep(1)
        self.click(Locators.QSUBMIT)
        time.sleep(3)

        # Add the quick onboard
        self.enter_text(Locators.QNAME, self.fake.name())  # Using faker for generating name
        time.sleep(1)
        self.dropdown_click(Locators.QGENDER, 1)
        time.sleep(1)
        self.enter_text(Locators.QAADHAR, self.fake.random_int(100000000000, 999999999999))
        time.sleep(1)
        self.enter_text(Locators.QDOJ, "12-12-2021")
        time.sleep(1)
        self.enter_text(Locators.QUDOJ, "14-12-2021")
        time.sleep(1)
        self.dropdown_click(Locators.QSHIFT, 1)
        time.sleep(1)
        self.dropdown_click(Locators.QCATEGORY, 1)
        time.sleep(1)
        self.dropdown_click(Locators.QDEPT, 1)
        time.sleep(2)
        self.dropdown_click(Locators.QDESG, 1)
        time.sleep(1)
        self.click(Locators.QSUBMIT)
        time.sleep(3)
        self.logger.info('Quick Onboard is Working Fine')

    def add(self):
        self.click(Locators.DETAIL_ONBOARD)
        time.sleep(10)
        self.click(Locators.EMP_GO_BACK)
        time.sleep(1)
        self.click(Locators.DETAIL_ONBOARD)
        time.sleep(10)
        self.click(Locators.NEXT)
        time.sleep(10)
        photo_path = "D:\\ssl\\HRM-Backend\\hrm_automation\\screenshot.png"  # Replace with the actual file path
        self.file_upload(Locators.FILE_UPLOAD, photo_path)
        time.sleep(1)
        self.enter_text(Locators.FNAME, self.fake.first_name())  # Using faker for generating first name
        time.sleep(1)
        self.enter_text(Locators.MNAME, "")
        time.sleep(1)
        self.enter_text(Locators.LNAME, self.fake.last_name())  # Using faker for generating last name
        time.sleep(1)
        self.enter_text(Locators.DOB, "13-09-2002")  # Using faker for generating DOB
        time.sleep(1)
        self.dropdown_click(Locators.GENDER, 1)
        time.sleep(1)
        self.dropdown_click(Locators.RELIGION, 1)
        time.sleep(1)
        self.dropdown_click(Locators.NATIONALITY, 1)
        time.sleep(1)
        self.dropdown_click(Locators.BLOOD_GRP, 1)
        time.sleep(1)
        self.dropdown_click(Locators.DISABLTY, 1)
        time.sleep(1)
        self.dropdown_click(Locators.MARITALSTS, 1)
        time.sleep(1)
        self.enter_text(Locators.MOB, str(random.randint(6, 9)) + ''.join(random.choice("0123456789") for _ in range(9)))
        time.sleep(1)
        self.enter_text(Locators.ALT_MOB, str(random.randint(6, 9)) + ''.join(random.choice("0123456789") for _ in range(9)))
        time.sleep(1)
        self.enter_text(Locators.EMAIL, self.fake.email())  # Using faker for generating email
        time.sleep(1)
        self.enter_text(Locators.ALT_EMAIL, self.fake.email())
        time.sleep(5)
        self.dropdown_click(Locators.CATE, 6)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.enter_text(Locators.CAD1, self.fake.street_address())  # Using faker for generating address
        time.sleep(1)
        self.enter_text(Locators.CAD2, self.fake.street_address())
        time.sleep(1)
        self.dropdown_click(Locators.VILLAGE, 1)
        time.sleep(1)
        self.enter_text(Locators.PIN, str(random.randint(600000, 699999)))  # Using faker for generating ZIP code
        time.sleep(5)
        self.enter_text(Locators.PAD1, self.fake.street_address())
        time.sleep(1)
        self.enter_text(Locators.PAD2, self.fake.street_address())
        time.sleep(1)
        self.dropdown_click(Locators.PVILLAGE, 2)
        time.sleep(1)
        self.enter_text(Locators.PPIN, str(random.randint(600000, 699999)))
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.CHECK)
        time.sleep(1)
        self.click(Locators.NEXT)
        time.sleep(20)
        self.logger.info('Personal Information is added successfully')
        time.sleep(1)
        self.enter_text(Locators.DOJ, "03-02-2024")
        time.sleep(2)
        self.enter_text(Locators.SAT_DOJ, "15-12-2024")
        time.sleep(2)
        self.enter_text(Locators.UNIT_DOJ, "17-12-2024")
        time.sleep(2)
        time.sleep(15)
        self.dropdown_click(Locators.SHIFT, 1)
        time.sleep(4)
        self.enter_text(Locators.SHIFT_START_EMP, "15-09-2025")
        time.sleep(5)
        self.enter_text(Locators.SHIFT_END_EMP, "14-09-2026")  # Using faker for generating DOB
        time.sleep(2)
        # id proof
        photo_path = "D:\\ssl\\HRM-Backend\\hrm_automation\\screenshot.png"
        self.file_upload(Locators.FILE_UPLOAD1, photo_path)
        time.sleep(2)
        self.enter_text(Locators.NAME_ADHAR, self.fake.name())  # Using faker for generating name
        time.sleep(1)
        self.enter_text(Locators.AADHAR_N0, str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))  # Using faker for generating SSN
        time.sleep(1)
        self.enter_text(Locators.PAN_NO, ''.join(random.choices(string.ascii_uppercase, k=5)) + ''.join(random.choices(string.digits, k=4)) + random.choice(string.ascii_uppercase))  # Using faker for generating PAN
        time.sleep(4)
        self.enter_text(Locators.DL_NO, self.fake.random_int(1000000000, 9999999999))  # Using faker for generating DL number
        time.sleep(1)
        self.enter_text(Locators.PASSPORT_N0, self.fake.random_int(1000000000, 9999999999))  # Using faker for generating passport number
        time.sleep(1)
        self.enter_text(Locators.PASSPORT_PLACE, self.fake.city())  # Using faker for generating passport place
        time.sleep(1)
        self.enter_text(Locators.PASSPORT_ISSUE_DT,"13-09-2017")  # Using faker for generating passport issue date
        time.sleep(1)
        self.enter_text(Locators.PASSPORT_EXPIRY_DT, "13-08-2028")  # Using faker for generating passport expiry date
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.dropdown_click(Locators.DEPT, 1)
        time.sleep(3)
        self.dropdown_click(Locators.DESG, 1)
        time.sleep(1)
        self.dropdown_click(Locators.PRIMARY_MAN, 1)
        time.sleep(1)
        # Or assign webdriver to a variable
        # browser = webdriver
        # checkboxes = browser.find_elements(By.XPATH, "(//input[@id='incharge'])[1]")
        # self.click(checkboxes[0])  # Access the first element of the list
        self.click(Locators.NEXT_EMP)
        time.sleep(10)
        self.logger.info('Job Details is added successfully')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-250)")
        time.sleep(2)
        # social security

        self.dropdown_click(Locators.SAL_TYPE, 1)
        time.sleep(2)
        self.enter_text(Locators.DAILY_WAGES, self.fake.random_int(10000, 50000))  # Using faker for generating daily wages
        time.sleep(2)
        self.click(Locators.PF_CHECK)
        time.sleep(2)
        self.enter_text(Locators.PF_NO, self.fake.random_int(100000000000, 999999999999))  # Using faker for generating PF number
        time.sleep(1)
        self.enter_text(Locators.UAN_NO, str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))  # Using faker for generating UAN number
        time.sleep(1)
        self.enter_text(Locators.PF_ISSUE_DT, "07-10-2023")  # Using faker for generating PF issue date
        time.sleep(1)
        self.enter_text(Locators.PF_RELEIVE_DT, "07-10-2029")  # Using faker for generating PF relieve date
        time.sleep(1)
        self.click(Locators.ARBY_CHECK)
        time.sleep(1)
        self.enter_text(Locators.ARBY_END_DT,"07-10-2024")  # Using faker for generating arbitration end date
        time.sleep(1)
        self.click(Locators.ESI_CHECK)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.enter_text(Locators.ESI_NO, self.fake.random_int(100000000000, 999999999999))  # Using faker for generating ESI number
        time.sleep(1)
        self.enter_text(Locators.ESI_ISSUE_DT, "07-10-2023")  # Using faker for generating ESI issue date
        time.sleep(1)
        self.enter_text(Locators.ESI_RELEIVE_DT, "07-10-2028")  # Using faker for generating ESI relieve date
        time.sleep(1)
        # BANK DETAILS
        self.click(Locators.BANK_DET_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.enter_text(Locators.IFSC_CODE, self.fake.random_int(100000, 999999))  # Using faker for generating IFSC code
        time.sleep(1)
        self.enter_text(Locators.BANK_NAME,"City Union Bank")  # Using faker for generating bank name
        time.sleep(1)
        self.enter_text(Locators.ACC_NO, self.fake.random_int(100000000000, 999999999999))  # Using faker for generating account number
        time.sleep(1)
        self.enter_text(Locators.ACC_HOLD_NAME, self.fake.name())  # Using faker for generating account holder name
        time.sleep(1)
        self.enter_text(Locators.BRANCH_NAME, self.fake.city())  # Using faker for generating branch name
        time.sleep(1)
        self.click(Locators.SAVE_BANK)
        time.sleep(1)
        self.logger.info('Bank Details is added successfully')
        time.sleep(1)
        self.click(Locators.NEXT_2)
        time.sleep(1)
        self.logger.info('Social Security Information is added successfully')
        time.sleep(1)
        # Family Details
        self.click(Locators.FAM_BT)
        time.sleep(1)
        self.enter_text(Locators.NAME, self.fake.name())  # Using faker for generating family member name
        time.sleep(1)
        self.enter_text(Locators.AGE, self.fake.random_int(18, 80))  # Using faker for generating age
        time.sleep(1)
        self.enter_text(Locators.RELATIONSHIP, self.fake.random_element(elements=('Father', 'Mother', 'Brother', 'Sister', 'Spouse')))  # Using faker for generating relationship
        time.sleep(1)
        self.click(Locators.NOMINEE)
        self.click(Locators.YES)
        time.sleep(1)
        self.enter_text(Locators.FAM_ADHAR_NO, str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))  # Using faker for generating family member SSN
        time.sleep(1)
        self.click(Locators.SAVE_FAM)
        time.sleep(1)
        self.click(Locators.FAM_BT)
        time.sleep(1)
        self.logger.info('Family Details is added successfully')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        # Education Details
        self.click(Locators.EDU_BT)
        time.sleep(1)
        self.enter_text(Locators.DEGREE, "BE")
        time.sleep(1)
        self.enter_text(Locators.INSTITUTION,"SSI")  # Using faker for generating institution name
        time.sleep(1)
        self.enter_text(Locators.PERCENT, self.fake.random_int(50, 100))  # Using faker for generating percentage
        time.sleep(1)
        self.enter_text(Locators.YEAR_PASS, "14-09-2002")
        time.sleep(1)
        self.click(Locators.SAVE_EDU)
        time.sleep(1)
        self.logger.info('Education details is added successfully')
        time.sleep(1)
        self.click(Locators.EDU_BT)
        time.sleep(1)
        # Experience Details
        self.click(Locators.EXP_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.enter_text(Locators.COMP, "Techgenzi Private Limited")  # Using faker for generating company name
        time.sleep(1)
        self.enter_text(Locators.DESG_EXP, "TESTER")
        time.sleep(1)
        self.enter_text(Locators.EXP_MON, "6")
        time.sleep(1)
        self.enter_text(Locators.SALARY, self.fake.random_int(30000, 150000))  # Using faker for generating salary
        time.sleep(1)
        self.click(Locators.SAVE_EXP)
        time.sleep(1)
        self.logger.info('Experience Details is added successfully')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-100)")
        time.sleep(2)
        self.click(Locators.EXP_BT)
        time.sleep(1)
        # Training details
        self.click(Locators.TRAIN_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.enter_text(Locators.TITLE, "webdeveloper")
        time.sleep(1)
        self.enter_text(Locators.LOCATION, "chennai")
        time.sleep(1)
        self.enter_text(Locators.DURATION, "6")
        time.sleep(1)
        self.enter_text(Locators.DATE, "12-12-2023")
        time.sleep(1)
        self.click(Locators.SAVE_TRAIN)
        time.sleep(1)
        self.logger.info('Training Details is added successfully')
        time.sleep(1)
        self.click(Locators.TRAIN_BT)
        time.sleep(1)
        # Miscellaneous
        self.click(Locators.MIS_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.enter_text(Locators.IDENT, "one scar in hand")
        time.sleep(1)
        self.enter_text(Locators.BLOOD_PRE, "120/50hg/mm")
        time.sleep(1)
        self.enter_text(Locators.HEIGHT, "145")
        time.sleep(1)
        self.enter_text(Locators.WEIGHT, "45")
        time.sleep(1)
        self.dropdown_click(Locators.REFERENCE, 1)
        time.sleep(1)
        self.click(Locators.SAVE_MIS)
        time.sleep(1)
        self.logger.info('Misscelleneous Information is added successfully')
        time.sleep(1)
        # Generate Employee
        self.click(Locators.GENERATE_EMP)
        time.sleep(5)
        self.logger.info('Employee Information is Saved successfully')
        time.sleep(1)

    def edit_button(self):
        self.click(Locators.EMP_EDIT_BT)
        time.sleep(5)

    def edit_invalid_first_name(self):
        fake = Faker()


        # Invalid First Name (Empty)
        self.clear(Locators.EDIT_FNAME)
        time.sleep(2)
        self.enter_text(Locators.EDIT_FNAME, "")
        self.click(Locators.EDIT_NEXT)
        time.sleep(2)


    def edit_gender(self):
        self.clear(Locators.EDIT_GENDER)
        time.sleep(2)
        self.click(Locators.EDIT_NEXT)
        time.sleep(2)
    def edit_invalid_dob(self):
        fake=Faker()
        # Invalid First Name (Empty)
        self.clear(Locators.EDIT_DOB)
        time.sleep(2)
        self.enter_text(Locators.EDIT_DOB, "")
        self.click(Locators.EDIT_NEXT)
        time.sleep(2)
        assert "Field is required" in self.driver.find_element_by_id("//p[@id='gender-helper-text']").text

    def edit(self):
        # self.click(Locators.EMP_EDIT_BT)
        # time.sleep(2)

        fake = Faker()
        time.sleep(2)
        self.enter_text(Locators.EDIT_FNAME, fake.first_name())

        # Middle Name
        self.clear(Locators.EDIT_MNAME)
        time.sleep(2)
        self.enter_text(Locators.EDIT_MNAME, fake.first_name())

        # Last Name
        self.clear(Locators.EDIT_LNAME)
        time.sleep(2)
        self.enter_text(Locators.EDIT_LNAME, fake.last_name())

        # Date of Birth
        self.enter_text(Locators.EDIT_DOB, "13-01-1991")

        # Gender
        self.dropdown_click(Locators.EDIT_GENDER, fake.random_int(min=1, max=2))

        # Religion
        self.dropdown_click(Locators.EDIT_RELIGION, fake.random_int(min=1, max=5))

        # Nationality
        self.dropdown_click(Locators.EDIT_NATIONALITY, fake.random_int(min=1, max=5))

        # Blood Group
        self.dropdown_click(Locators.EDIT_BLOOD_GRP, fake.random_int(min=1, max=5))

        # Disability
        self.dropdown_click(Locators.EDIT_DISABLTY, fake.random_int(min=1, max=3))

        # Marital Status
        self.dropdown_click(Locators.EDIT_MARITALSTS, fake.random_int(min=1, max=4))

        # Mobile Number
        self.clear(Locators.EDIT_MOB)
        time.sleep(1)
        self.enter_text(Locators.EDIT_MOB,
                        str(random.randint(6, 9)) + ''.join(random.choice("0123456789") for _ in range(9)))

        # Alternate Mobile Number
        self.clear(Locators.EDIT_ALT_MOB)
        time.sleep(1)
        self.enter_text(Locators.EDIT_ALT_MOB,
                        str(random.randint(6, 9)) + ''.join(random.choice("0123456789") for _ in range(9)))

        # Email
        self.clear(Locators.EDIT_EMAIL)
        time.sleep(1)
        self.enter_text(Locators.EDIT_EMAIL, fake.email())

        # Alternate Email
        self.clear(Locators.EDIT_ALT_EMAIL)
        time.sleep(1)
        self.enter_text(Locators.EDIT_ALT_EMAIL, fake.email())

        # Category
        self.dropdown_click(Locators.CATE, fake.random_int(min=1, max=10))

        # Contact Address
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.clear(Locators.EDIT_CAD1)
        time.sleep(1)
        self.enter_text(Locators.EDIT_CAD1, self.fake.street_address())  # Using faker for generating address
        time.sleep(1)
        self.clear(Locators.EDIT_CAD2)
        time.sleep(1)
        self.enter_text(Locators.EDIT_CAD2, self.fake.street_address())
        time.sleep(1)
        self.dropdown_click(Locators.EDIT_VILLAGE1, 1)
        time.sleep(1)
        self.clear(Locators.EDIT_PIN)
        time.sleep(1)
        self.enter_text(Locators.EDIT_PIN, str(random.randint(600000, 699999)))
        time.sleep(5)
        self.clear(Locators.EDIT_PAD1)
        time.sleep(1)
        self.enter_text(Locators.EDIT_PAD1, self.fake.street_address())
        time.sleep(1)
        self.clear(Locators.EDIT_PAD2)
        time.sleep(1)
        self.enter_text(Locators.EDIT_PAD2, self.fake.street_address())
        time.sleep(1)
        self.dropdown_click(Locators.EDIT_VILLAGE2, 2)
        time.sleep(1)
        self.clear(Locators.PPIN)
        time.sleep(1)
        self.enter_text(Locators.EDIT_PPIN, str(random.randint(600000, 699999)))
        time.sleep(5)
        self.click(Locators.EDIT_NEXT)
        time.sleep(6)
        self.logger.info('Personal Information is Updated successfully')
        time.sleep(1)

    def dup_aadhar(self):
        fake = Faker()
        aadhar = "876901508870"

        # Enter Aadhaar number
        self.enter_text(Locators.AADHAR_N0, aadhar)

        # Define URL for the PATCH request
        url = 'https://ipssapi.techgenzi.com/employee_hrm/29752/'

        try:
            # Make the PATCH request
            response = requests.patch(url, json={"aadhar": aadhar}, headers=headers.get_headers())

            # Check the response status code
            if response.status_code == 200:
                logger.warning("Aadhaar number is accepted")
            elif response.status_code == 409:
                logger.info("Aadhaar number already exists")
            else:
                logger.error(f"Unexpected status code received: {response.status_code}")

        except requests.RequestException as e:
            # Log any exceptions that occur during the request
            logger.error(f"An error occurred: {e}")

        # Clear the Aadhaar field and re-enter the Aadhaar number
        self.clear(Locators.EDIT_AADHAR_N0)
        time.sleep(3)
        self.enter_text(Locators.EDIT_AADHAR_N0, aadhar)
        self.click(Locators.NEXT_EMP)
        time.sleep(5)

    def dup_pan(self):
        fake = Faker()
        panno = "GKQAW1823O"

        # Enter Aadhaar number
        self.enter_text(Locators.PAN_NO, panno)

        # Define URL for the PATCH request
        url = 'https://ipssapi.techgenzi.com/employee_hrm/29752/'

        try:
            # Make the PATCH request
            response = requests.patch(url, json={"panno": panno}, headers=headers.get_headers())

            # Check the response status code
            if response.status_code == 200:
                logger.warning("PAN number is accepted")
            elif response.status_code == 409:
                logger.info("pan number already exists")
            else:
                logger.error(f"Unexpected status code received: {response.status_code}")

        except requests.RequestException as e:
            # Log any exceptions that occur during the request
            logger.error(f"An error occurred: {e}")

        # Clear the Aadhaar field and re-enter the Aadhaar number
        self.clear(Locators.PAN_NO)
        time.sleep(3)
        self.enter_text(Locators.PAN_NO, panno)
        self.click(Locators.NEXT_EMP)
        time.sleep(5)

    def dup_passport(self):
        fake = Faker()
        passport = "3870669583"

        # Enter Aadhaar number
        self.enter_text(Locators.PASSPORT_N0, passport)

        # Define URL for the PATCH request
        url = 'https://ipssapi.techgenzi.com/employee_hrm/29752/'

        try:
            # Make the PATCH request
            response = requests.patch(url, json={"passportno": passport}, headers=headers.get_headers())

            # Check the response status code
            if response.status_code == 200:
                logger.warning("PASSPORT number is accepted")
            elif response.status_code == 409:
                logger.info("PASSPORT  number already exists")
            else:
                logger.error(f"Unexpected status code received: {response.status_code}")

        except requests.RequestException as e:
            # Log any exceptions that occur during the request
            logger.error(f"An error occurred: {e}")

        # Clear the Aadhaar field and re-enter the Aadhaar number
        self.clear(Locators.PASSPORT_N0)
        time.sleep(3)
        self.enter_text(Locators.PASSPORT_N0, passport)
        self.click(Locators.NEXT_EMP)
        time.sleep(5)

    def dup_driving_licensce(self):
        fake = Faker()
        dl = "3921504155"

        # Enter Aadhaar number
        self.enter_text(Locators.DL_NO, dl)

        # Define URL for the PATCH request
        url = 'https://ipssapi.techgenzi.com/employee_hrm/29752/'

        try:
            # Make the PATCH request
            response = requests.patch(url, json={"drivinglicenceno": dl}, headers=headers.get_headers())

            # Check the response status code
            if response.status_code == 200:
                logger.warning("Driving license number is accepted")
            elif response.status_code == 409:
                logger.info("Driving License number already exists")
            else:
                logger.error(f"Unexpected status code received: {response.status_code}")

        except requests.RequestException as e:
            # Log any exceptions that occur during the request
            logger.error(f"An error occurred: {e}")

        # Clear the Aadhaar field and re-enter the Aadhaar number
        self.clear(Locators.DL_NO)
        time.sleep(3)
        self.enter_text(Locators.DL_NO, dl)
        self.click(Locators.NEXT_EMP)
        time.sleep(5)

    def edit1(self):
        fake = Faker()
        # Employment Date
        time.sleep(15)
        self.enter_text(Locators.EDIT_DOJ, "12-12-2012")
        time.sleep(4)
        # Shift
        self.dropdown_click(Locators.EDIT_SHIFT, fake.random_int(min=1, max=3))

        self.click(Locators.OT_APPLICABLE)
        time.sleep(1)

        # Identity Proof
        self.clear(Locators.EDIT_NAME_ADHAR)
        time.sleep(3)
        fake = Faker()

        # Assuming employee_name is already generated somewhere
        employee_name = fake.name()  # Example: John Doe

        self.enter_text(Locators.EDIT_NAME_ADHAR, re.sub(r'[^a-zA-Z]', '', employee_name))
        time.sleep(1)
        self.clear(Locators.EDIT_AADHAR_N0)
        time.sleep(3)
        self.enter_text(Locators.EDIT_AADHAR_N0,
                        str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))

        self.clear(Locators.EDIT_PAN_NO)
        time.sleep(3)
        self.enter_text(Locators.EDIT_PAN_NO, ''.join(random.choices(string.ascii_uppercase, k=5)) + ''.join(
            random.choices(string.digits, k=4)) + random.choice(string.ascii_uppercase))

        self.clear(Locators.EDIT_DL_NO)
        time.sleep(3)
        self.enter_text(Locators.EDIT_DL_NO, fake.random_int(min=1000000000000, max=9999999999999))

        self.clear(Locators.EDIT_PASSPORT_N0)
        time.sleep(3)
        self.enter_text(Locators.EDIT_PASSPORT_N0, fake.random_int(min=1000001110001, max=9929999999999))

        self.clear(Locators.EDIT_PASSPORT_PLACE)
        time.sleep(3)
        self.enter_text(Locators.EDIT_PASSPORT_PLACE, fake.city())

        self.clear(Locators.EDIT_PASSPORT_ISSUE_DT)
        time.sleep(3)
        self.enter_text(Locators.EDIT_PASSPORT_ISSUE_DT, "12-12-2012")

        self.clear(Locators.EDIT_PASSPORT_EXPIRY_DT)
        time.sleep(3)
        self.enter_text(Locators.EDIT_PASSPORT_EXPIRY_DT, "12-12-2024")
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        # Employee Role
        self.dropdown_click(Locators.DEPT, 1)
        time.sleep(3)
        self.dropdown_click(Locators.DESG, 1)
        time.sleep(3)
        self.dropdown_click(Locators.PRIMARY_MAN, 1)
        time.sleep(1)
        # self.click(Locators.INCHARGE)
        # time.sleep(1)
        # self.click(Locators.INCHARGE1)
        # time.sleep(1)
        self.click(Locators.NEXT_EMP)
        time.sleep(10)
        self.logger.info('Job details is updated successfully')
        time.sleep(1)

        # Social Security
        self.clear(Locators.PF_NO)
        time.sleep(1)
        self.enter_text(Locators.PF_NO, fake.random_int(min=10000000, max=99999999))

        self.clear(Locators.UAN_NO)
        time.sleep(3)
        self.enter_text(Locators.UAN_NO, str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))

        self.enter_text(Locators.PF_ISSUE_DT, "12-12-2012")
        time.sleep(2)
        self.enter_text(Locators.PF_RELEIVE_DT, "12-12-2024")
        time.sleep(2)
        self.enter_text(Locators.ARBY_END_DT, "12-12-2024")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.clear(Locators.ESI_NO)
        time.sleep(1)
        self.enter_text(Locators.ESI_NO, fake.random_int(min=1000000000, max=9999999999))
        time.sleep(1)
        self.enter_text(Locators.ESI_ISSUE_DT, "12-12-2012")
        time.sleep(1)
        self.enter_text(Locators.ESI_RELEIVE_DT,"12-12-2024")
        time.sleep(1)
        self.click(Locators.BANK_DET_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        # self.driver.execute_script("arguments[0].scrollIntoView();",
        #                            self.driver.find_element_by_xpath("//xpath/to/EDIT_BANK_DETAIL"))
        # time.sleep(1)
        fake = Faker()
        self.enter_text(Locators.IFSC_CODE, fake.random_element(["CIUB991541116", "ABCD12345678", "XYZW09876543"]))
        time.sleep(1)
        self.enter_text(Locators.BANK_NAME, re.sub(r'[^a-zA-Z]', '', Faker().word()))
        time.sleep(1)

    def dup_bank(self):
        fake = Faker()
        acc = "123456"

        # Enter Aadhaar number
        self.enter_text(Locators.ACC_NO, acc)

        # Define URL for the PATCH request
        url = 'https://ipssapi.techgenzi.com/employee_hrm/employee_bank/22955/'

        try:
            # Make the PATCH request
            response = requests.patch(url, json={"passportno": acc}, headers=headers.get_headers())

            # Check the response status code
            if response.status_code == 200:
                logger.warning("Account number is accepted")
            elif response.status_code == 409:
                logger.info("Account  number already exists")
            else:
                logger.error(f"Unexpected status code received: {response.status_code}")

        except requests.RequestException as e:
            # Log any exceptions that occur during the request
            logger.error(f"An error occurred: {e}")

        # Clear the Aadhaar field and re-enter the Aadhaar number
        self.clear(Locators.ACC_NO)
        time.sleep(3)
        self.enter_text(Locators.ACC_NO, acc)
        self.click(Locators.SAVE_BANK)
        time.sleep(10)

        self.enter_text(Locators.ACC_NO, fake.random_number(digits=12))
        time.sleep(1)
        self.enter_text(Locators.ACC_HOLD_NAME, fake.name())
        time.sleep(1)
        self.enter_text(Locators.BRANCH_NAME, fake.city() + " Branch")
        time.sleep(1)
        self.click(Locators.SAVE_BANK)
        time.sleep(1)
        self.logger.info('Bank Details is Updated successfully')
        time.sleep(1)
        self.click(Locators.NEXT_2)
        time.sleep(6)
        self.logger.info('Social security Information is Updated successfully')
        time.sleep(1)
        # Family Details
        self.click(Locators.FAM_BT)
        time.sleep(1)
        self.enter_text(Locators.NAME, self.fake.name())  # Using faker for generating family member name
        time.sleep(1)
        self.enter_text(Locators.AGE, self.fake.random_int(18, 80))  # Using faker for generating age
        time.sleep(1)
        self.enter_text(Locators.RELATIONSHIP, self.fake.random_element(elements=('Father', 'Mother', 'Brother', 'Sister', 'Spouse')))  # Using faker for generating relationship
        time.sleep(1)
        self.click(Locators.NOMINEE)
        self.click(Locators.YES)
        time.sleep(1)
        self.enter_text(Locators.FAM_ADHAR_NO, str(random.randint(1, 9)) + ''.join(random.choice("0123456789") for _ in range(11)))  # Using faker for generating family member SSN
        time.sleep(1)
        self.click(Locators.SAVE_FAM)
        time.sleep(1)
        self.logger.info('Family Details is added successfully')
        time.sleep(1)
        self.click(Locators.FAM_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        # Education Details
        self.click(Locators.EDU_BT)
        time.sleep(1)
        self.enter_text(Locators.DEGREE, "BE")
        time.sleep(1)
        self.enter_text(Locators.INSTITUTION,"SSI")  # Using faker for generating institution name
        time.sleep(1)
        self.enter_text(Locators.PERCENT, self.fake.random_int(50, 100))  # Using faker for generating percentage
        time.sleep(1)
        self.enter_text(Locators.YEAR_PASS, "14-09-2002")
        time.sleep(1)
        self.click(Locators.SAVE_EDU)
        time.sleep(1)
        self.click(Locators.EDU_BT)
        time.sleep(1)
        self.logger.info('Education details is added successfully')
        time.sleep(1)
        # Experience Details
        self.click(Locators.EXP_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.enter_text(Locators.COMP, "Techgenzi Private Limited")  # Using faker for generating company name
        time.sleep(1)
        self.enter_text(Locators.DESG_EXP, "TESTER")
        time.sleep(1)
        self.enter_text(Locators.EXP_MON, "6")
        time.sleep(1)
        self.enter_text(Locators.SALARY, self.fake.random_int(30000, 150000))  # Using faker for generating salary
        time.sleep(1)
        self.click(Locators.SAVE_EXP)
        time.sleep(1)
        self.logger.info('Experience Detail is added successfully')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        # self.click(Locators.EXP_BT)
        # time.sleep(1)
        # Training details
        self.click(Locators.TRAIN_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-300)")
        time.sleep(1)
        self.enter_text(Locators.TITLE, "webdeveloper")
        time.sleep(1)
        self.enter_text(Locators.LOCATION, "chennai")
        time.sleep(1)
        self.enter_text(Locators.DURATION, "6")
        time.sleep(1)
        self.enter_text(Locators.DATE, "12-12-2023")
        time.sleep(1)
        self.click(Locators.SAVE_TRAIN)
        time.sleep(1)
        self.logger.info('Training Details is added successfully')
        time.sleep(1)
        self.click(Locators.TRAIN_BT)
        time.sleep(1)
        # Miscellaneous
        self.click(Locators.MIS_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        self.enter_text(Locators.IDENT, "one scar in hand")
        time.sleep(1)
        self.enter_text(Locators.BLOOD_PRE, "120/50hg/mm")
        time.sleep(1)
        self.enter_text(Locators.HEIGHT, "145")
        time.sleep(1)
        self.enter_text(Locators.WEIGHT, "45")
        time.sleep(1)
        self.dropdown_click(Locators.REFERENCE, 1)
        time.sleep(1)
        self.click(Locators.SAVE_MIS)
        time.sleep(1)
        self.logger.info('Misscellenious is added successfully')
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-500)")
        time.sleep(1)

        # Family Details
        self.click(Locators.EDIT_FAM_BT)
        time.sleep(4)
        self.click(Locators.EDIT_FAM_DET)
        time.sleep(3)
        self.clear(Locators.EDIT_NAME)
        time.sleep(1)
        self.enter_text(Locators.EDIT_NAME, fake.name())
        time.sleep(1)
        self.click(Locators.EDIT_SAVE_FAM)
        time.sleep(2)
        self.click(Locators.EDIT_FAM_BT)
        time.sleep(2)
        self.logger.info('Family Information is Updated successfully')
        time.sleep(1)

        # Education Details
        self.click(Locators.EDU_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(1)
        self.click(Locators.EDIT_EDUC_DET)
        time.sleep(1)
        self.clear(Locators.DEGREE)
        time.sleep(1)
        self.enter_text(Locators.DEGREE, fake.random_element(["BE", "B.Tech", "MBA", "BA", "BSc", "PhD"]))
        time.sleep(1)
        self.clear(Locators.INSTITUTION)
        time.sleep(1)
        self.enter_text(Locators.INSTITUTION, fake.company())
        time.sleep(1)
        self.clear(Locators.PERCENT)
        time.sleep(1)
        self.enter_text(Locators.PERCENT, fake.random_int(min=50, max=100))
        time.sleep(1)
        self.enter_text(Locators.YEAR_PASS, "12-12-2023")
        time.sleep(1)
        self.click(Locators.SAVE_EDU)
        time.sleep(1)
        self.click(Locators.EDU_BT)
        time.sleep(1)
        self.logger.info('Education Information is Updated successfully')
        time.sleep(1)

        # Experience Details
        self.click(Locators.EDIT_EXP_BT)
        time.sleep(1)
        # self.driver.execute_script("window.scrollBy(0,250)")
        # time.sleep(1)
        self.click(Locators.EDIT_EX_DET)
        time.sleep(1)
        self.clear(Locators.COMP)
        time.sleep(1)
        self.enter_text(Locators.COMP, fake.company())
        time.sleep(1)
        self.clear(Locators.DESG_EXP)
        time.sleep(1)
        self.enter_text(Locators.DESG_EXP, fake.job())
        time.sleep(1)
        self.clear(Locators.EXP_MON)
        time.sleep(1)
        self.enter_text(Locators.EXP_MON, fake.random_int(min=1, max=24))
        time.sleep(1)
        self.clear(Locators.SALARY)
        time.sleep(1)
        self.enter_text(Locators.SALARY, fake.random_int(min=30000, max=150000))
        time.sleep(1)
        self.click(Locators.SAVE_EXP)
        time.sleep(1)
        self.click(Locators.EXP_BT)
        time.sleep(1)
        self.logger.info('Experience Details is Updated successfully')
        time.sleep(1)

        # Training details
        self.click(Locators.EDIT_TRAIN_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(1)
        self.click(Locators.EDIT_TRAIN_DET)
        time.sleep(1)
        self.clear(Locators.EDIT_TITLE)
        time.sleep(1)
        self.enter_text(Locators.EDIT_TITLE, fake.job())
        time.sleep(1)
        self.clear(Locators.EDIT_LOCATION)
        time.sleep(1)
        self.enter_text(Locators.EDIT_LOCATION, fake.city())
        time.sleep(1)
        self.clear(Locators.EDIT_DURATION)
        time.sleep(1)
        self.enter_text(Locators.EDIT_DURATION, fake.random_int(min=1, max=12))
        time.sleep(1)
        self.enter_text(Locators.EDIT_DATE, fake.date_between(start_date='-1y', end_date='today').strftime('%d-%m-%Y'))
        time.sleep(1)
        self.click(Locators.EDIT_SAVE_TRAIN)
        time.sleep(1)
        self.click(Locators.EDIT_TRAIN_BT)
        time.sleep(1)
        self.logger.info('Training Details is Updated successfully')
        time.sleep(1)

        # Miscellaneous
        self.click(Locators.EDIT_MIS_BT)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(1)
        self.clear(Locators.EDIT_IDENT)
        time.sleep(1)
        self.enter_text(Locators.EDIT_IDENT, fake.sentence())
        time.sleep(1)
        self.clear(Locators.EDIT_BLOOD_PRE)
        time.sleep(1)
        self.enter_text(Locators.EDIT_BLOOD_PRE, fake.random_element(["120/80 HG MM", "130/85 HG MM", "140/90 HG MM"]))
        time.sleep(1)
        self.clear(Locators.EDIT_HEIGHT)
        time.sleep(1)
        self.enter_text(Locators.EDIT_HEIGHT, fake.random_int(min=140, max=200))
        time.sleep(1)
        self.enter_text(Locators.EDIT_WEIGHT, fake.random_int(min=40, max=150))
        time.sleep(1)
        self.dropdown_click(Locators.EDIT_REFERENCE, fake.random_int(min=1, max=5))
        time.sleep(1)
        self.click(Locators.EDIT_SAVE_MIS)
        time.sleep(1)
        self.logger.info('Misscelleneous Information is Updated successfully')
        time.sleep(1)

        # Generate Employee
        self.click(Locators.GENERATE_EMP)
        time.sleep(5)
        self.logger.info('Employee Information is Updated successfully')
        time.sleep(1)

    def emp_config2(self):
        self.emp_tab()
        self.search()
        # self.quick()
        # self.quick()
        # self.quick()
        self.quick()
        self.add()
        self.edit_button()
        self.edit_invalid_first_name()
        self.edit()
        self.dup_aadhar()
        self.dup_pan()
        self.dup_passport()
        self.dup_driving_licensce()
        self.edit1()
        self.dup_bank()
