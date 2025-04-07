import random
import time
import unittest
from selenium.webdriver.common.by import By
from ..headers import AppTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import requests

from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
from hrm_automation.logger_file import get_logger
import logging
# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler('hrm_log.log')
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Configuration(BasePage,unittest.TestCase):
    """
    Login common module for all user roles.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Configuration")
    def con_tab(self):
        # self.click(Locators.DRAW)
        # time.sleep(2)
        # self.click(Locators.CONFG_SIDEBAR_DRAW)
        # time.sleep(5)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,800)")
        time.sleep(1)
        self.click(Locators.DEF_COMP_CARD)
        time.sleep(2)
        # time.sleep(5)
        # self.click(Locators.CONFIG_CARD)
        # time.sleep(5)

    def band(self):
        
        self.click(Locators.BAND_BTN)
        time.sleep(1)

#CHECKING THE CANCEL BUTTON
        self.enter_text(Locators.BAND_NAME, "Band")
        time.sleep(1)
        self.click(Locators.BAND_CANCEL)
        time.sleep(2)
        self.logger.info("Cancel button clicked successfully")
#CHECKING THE SAVE BUTTON
        self.enter_text(Locators.BAND_NAME, "Band")
        time.sleep(1)
        self.click(Locators.BAND_SAVE)
        time.sleep(2)
        self.clear(Locators.BAND_NAME)
        time.sleep(2)
        self.logger.info("save button clicked successfully")
#CHECKING THE BAND NAME REQUIRED FIELD
        self.click(Locators.BAND_SAVE)
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Band is not entered so not submitted. So, Test passed")  # Pass the logger name
            time.sleep(1)
            self.click(Locators.BAND_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Band is Not Entered But may be submitted or not shown the Error, Test Failed")


        fake = Faker()

        url = "https://ipssapi.techgenzi.com/band_hrm/"

        for _ in range(1):  # Adjust the number of bands you want to create
            random_number = random.randint(5, 10000)  # Generates a random number between 1 and 1000
            band_name = f"Band {random_number}"  # Example: "Band 453", "Band 872", etc.

            try:
                response = requests.post(url, json={"bandname": band_name}, headers=AppTestCase.get_headers())

                if response.status_code == 200:
                    print(f"Category '{band_name}' created successfully")
                    self.logger.info(f"Category '{band_name}' created successfully")
                elif response.status_code == 409:
                    print(f"Category '{band_name}' already exists: Response code is {response.status_code}")
                    self.logger.warning(f"Category '{band_name}' already exists: Response code is {response.status_code}")
                else:
                    print(f"Category '{band_name}' creation failed: Response code is {response.status_code}")
                    self.logger.error(f"Category '{band_name}' creation failed: Response code is {response.status_code}")
            except requests.RequestException as e:
                print(f"An error occurred: {e}")
                raise e


    def edit_band(self):
# CHECKING THE EDIT BUTTON      
            self.click(Locators.BAND_EDIT)
            time.sleep(2)
# CHECKING THE SAVE BUTTON 
            self.click(Locators.BAND_SAVE)
            time.sleep(1)
            self.logger.info("Save button clicked successfully")
 #Click the Edit and click the cancel Button
            self.click(Locators.BAND_EDIT)
            time.sleep(2)
            self.click(Locators.BAND_CANCEL)
            time.sleep(1)
            self.logger.info("Cancel button clicked successfully")
# CHECKING REQUIRED FIELD          
            self.clear(Locators.BAND_NAME)
            time.sleep(1)
#CHECKING THE BAND NAME REQUIRED FIELD
            self.click(Locators.BAND_SAVE)
            time.sleep(2)
            error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
            if error_message.strip() == "Required input field":
                self.logger.warning("Band is not entered so not submitted. So, Test passed")  # Pass the logger name
                time.sleep(1)
                self.click(Locators.BAND_CANCEL)
                time.sleep(1)
            else:
                self.logger.error("Band is Not Entered But may be submitted or not shown the Error, Test Failed")
            
# Click the edit button
           
            self.click(Locators.BAND_EDIT)
            time.sleep(2)


            # Construct the API request
            url = f"https://ipssapi.techgenzi.com/band_hrm/683/"
            band_name = f"Band {random.randint(5, 10000)}"

            response = requests.patch(url, json={"bandname": band_name}, headers=AppTestCase.get_headers())

            # Log API response
            if response.status_code == 200:
                self.logger.info(f"Category '{band_name}' updated successfully")
            else:
                self.logger.error(f"Category update failed: Response code {response.status_code}")
            self.click(Locators.BAND_BTN)

    def group(self):
        self.click(Locators.EMPGRP_BTN)
        time.sleep(1)

        # CHECKING THE CANCEL BUTTON
        self.enter_text(Locators.EMP_GRP, "EMPGRP 5")
        time.sleep(1)
        self.enter_text(Locators.EMP_GRP_DESP, "GRP DESC")
        time.sleep(1)
        self.click(Locators.EMP_GRP_CANCEL)
        time.sleep(2)
        self.logger.info("Cancel button clicked successfully")

        # CHECKING THE SAVE BUTTON
        self.enter_text(Locators.EMP_GRP, "EMPGRP 5")
        time.sleep(1)
        self.enter_text(Locators.EMP_GRP_DESP, "GRP DESC")
        time.sleep(1)
        self.click(Locators.EMP_GRP_SAVE)
        time.sleep(2)
        self.logger.info("save button clicked successfully")

        # CHECKING THE GROUP NAME REQUIRED FIELD
        self.clear(Locators.EMP_GRP)
        time.sleep(1)
        self.clear(Locators.EMP_GRP_DESP)
        time.sleep(1)
        self.click(Locators.EMP_GRP_SAVE)
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Group name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.EMP_GRP_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Group name is not entered but may be submitted or not shown the error. Test failed.")

        fake = Faker()
        url = "https://ipssapi.techgenzi.com/employee_group_hrm/"

        for _ in range(1):
            random_number = random.randint(1, 10000)
            group_name = f"Group {random_number}"

            try:
                response = requests.post(url, json={
    "types": "Group",
    "description": "",
    "employee_group": group_name
}, headers=AppTestCase.get_headers())
                if response.status_code == 200:
                    self.logger.info(f"Group '{group_name}' created successfully")
                elif response.status_code == 409:
                    self.logger.warning(f"Group '{group_name}' already exists: Response code {response.status_code}")
                else:
                    self.logger.error(f"Group '{group_name}' creation failed: Response code {response.status_code}")
            except requests.RequestException as e:
                self.logger.error(f"An error occurred: {e}")
                raise e

    def edit_group(self):
        
        # CHECKING THE EDIT BUTTON
        self.click(Locators.EMP_GRP_EDIT_BTN)
        time.sleep(2)
        self.click(Locators.EMP_GRP_SAVE)
        time.sleep(1)

        # CLICK THE EDIT AND CLICK THE CANCEL BUTTON
        self.click(Locators.EMP_GRP_EDIT_BTN)
        time.sleep(2)
        self.click(Locators.EMP_GRP_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")

        # CHECKING REQUIRED FIELD
        self.clear(Locators.EMP_GRP_EDIT)
        time.sleep(1)
        self.clear(Locators.EMP_GRP_DESP_EDIT)
        time.sleep(1)
        self.click(Locators.EMP_GRP_SAVE)
        time.sleep(2)

        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Group name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.EMP_GRP_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Group name is not entered but may be submitted or not shown the error. Test failed.")

        # CLICK THE EDIT AND UPDATE THE DATA AND POST IT
        self.click(Locators.EMP_GRP_EDIT_BTN)
        time.sleep(2)
        group_name = f"Group {random.randint(5, 10000)}"
        url = f"https://ipssapi.techgenzi.com/employee_group_hrm/822/"

        response = requests.patch(url, json={
    "types": "Group",
    "description": "",
    "employee_group": group_name
}, headers=AppTestCase.get_headers())
        if response.status_code == 200:
            self.logger.info(f"Group '{group_name}' updated successfully") 
        else:
            self.logger.error(f"Group update failed: Response code {response.status_code}")
        self.click(Locators.EMPGRP_BTN)
        time.sleep(1)

    def dept(self):
        
        self.click(Locators.DEPT_BTN)
        time.sleep(1)

        # CHECKING THE CANCEL BUTTON
        self.enter_text(Locators.DEPT_DEPT, "EMP Cutting 4")
        time.sleep(1)
        self.enter_text(Locators.DEPT_DESP, "EMP DEPT DESC")
        time.sleep(1)
        self.click(Locators.DEPT_CANCEL)
        time.sleep(2)
        self.logger.info("Cancel button clicked successfully")

        # CHECKING EMPTY SUBMISSION
        self.click(Locators.DEPT_SAVE)
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Department name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.DEPT_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Department name is not entered but may be submitted or not shown the error. Test failed.")

        # CHECKING THE SAVE BUTTON
        self.enter_text(Locators.DEPT_DEPT, "Finishing Machines")
        time.sleep(1)
        self.enter_text(Locators.DEPT_DESP, "EMP DEPT DESC")
        time.sleep(1)
        self.click(Locators.DEPT_SAVE)
        time.sleep(2)
        self.logger.info("save button clicked successfully")


        # API CALL TO CREATE DEPARTMENT
        url = "https://ipssapi.techgenzi.com/department_hrm/"
        random_number = random.randint(1, 10000)
        dept_name = f"Department {random_number}"

        try:
            response = requests.post(url, json={
                "description": "New department",
                "dept_name": dept_name
            }, headers=AppTestCase.get_headers())
            if response.status_code == 200:
                self.logger.info(f"Department '{dept_name}' created successfully")
            elif response.status_code == 409:
                self.logger.warning(f"Department '{dept_name}' already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Department '{dept_name}' creation failed: Response code {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            raise e

    def edit_dept(self):
        # CHECKING THE EDIT BUTTON
        # self.click(Locators.DEPT_BTN)
        # time.sleep(2)
        self.click(Locators.DEPT_SAVE)
        time.sleep(1)
        self.logger.info("save button clicked successfully")
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)

        # CLICK THE EDIT AND CLICK THE CANCEL BUTTON
        self.click(Locators.EMP_DEPT_EDIT_BTN)
        time.sleep(2)
        self.click(Locators.DEPT_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")

        # CHECKING REQUIRED FIELD
        self.clear(Locators.DEPT_DEPT)
        time.sleep(1)
        self.clear(Locators.EDIT_DESP)
        time.sleep(1)
        self.click(Locators.DEPT_SAVE)
        time.sleep(2)

        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Department name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.DEPT_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Department name is not entered but may be submitted or not shown the error. Test failed.")

        # CLICK THE EDIT AND UPDATE THE DATA AND POST IT
        self.click(Locators.EMP_DEPT_EDIT_BTN)
        time.sleep(2)
        updated_dept_name = f"Department {random.randint(5, 10000)}"
        url = "https://ipssapi.techgenzi.com/department_hrm/414/"

        response = requests.patch(url, json={
            "description": "Updated department description",
            "dept_name": updated_dept_name
        }, headers=AppTestCase.get_headers())

        if response.status_code == 200:
            self.logger.info(f"Department '{updated_dept_name}' updated successfully")
        else:
            self.logger.error(f"Department update failed: Response code {response.status_code}")

        self.click(Locators.DEPT_BTN)
        time.sleep(1)

        

    def designation(self):
        fake=Faker()
        self.click(Locators.DESG_BTN)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)
        
        # Click the cancel button
        self.click(Locators.DESG_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")
        
        # Attempt to save without entering data
        self.click(Locators.DESG_SAVE)
        time.sleep(2)
        self.logger.info("save button clicked successfully")
        
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Designation name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.DESG_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Designation name is not entered but may be submitted or not shown the error. Test failed.")
        
        # Save the designation with a unique name
        designation_name = f"Designation {random.randint(1, 10000)}"
        print(designation_name) 

        # API call to create a designation
        url = "https://ipssapi.techgenzi.com/department_hrm/designation/416/"
        
        try:
            response = requests.post(url, json={
    "desg_name": designation_name,
    "deptmastid": 416,
    "description": ""
}, headers=AppTestCase.get_headers())
            if response.status_code == 200:
                self.logger.info(f"Designation '{designation_name}' created successfully")
            elif response.status_code == 409:
                self.logger.warning(f"Designation '{designation_name}' already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Designation '{designation_name}' creation failed: Response code {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
        
        # Click the edit button and update the designation
        self.click(Locators.DESG_EDIT_BTN)
        time.sleep(2)
        updated_designation_name = f"Designation {random.randint(1, 10000)}"
        edit_url = "https://ipssapi.techgenzi.com/department_hrm/designation/860/"
        
        response = requests.patch(edit_url, json={
    "desg_name": updated_designation_name,
    "deptmastid": 390,
    "description": "Updated designation description"
}, headers=AppTestCase.get_headers())
        
        if response.status_code == 200:
            self.logger.info(f"Designation '{updated_designation_name}' updated successfully")
        else:
            self.logger.error(f"Designation update failed: Response code {response.status_code}")
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,-200)")
        time.sleep(1)
        self.click(Locators.DESG_BTN)
        time.sleep(1)

    def grade(self):
        self.click(Locators.EMP_GRADE_BTN)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)

        #click the cancel button
        self.click(Locators.EMP_GRADE_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")

        #click the save button
        self.click(Locators.EMP_GRADE_SAVE)
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Grade name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.EMP_GRADE_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Grade name is not entered but may be submitted or not shown the error. Test failed.")

        #clicking save the grade
        self.enter_text(Locators.EMP_GRADE,"EDP Department")
        time.sleep(1)
        self.click(Locators.EMP_GRADE_SAVE)
        time.sleep(2)
        self.logger.info("save button clicked successfully")


        # API call to create a grade
        url = "https://ipssapi.techgenzi.com/employee_group_hrm/"
        random_number = random.randint(1, 10000)
        grade_name = f"Grade {random_number}"
        
        try:
            response = requests.post(url, json={
                "types": "Grade",
                "description": "description",
                "employee_group": grade_name
            }, headers=AppTestCase.get_headers())
            if response.status_code == 200:
                self.logger.info(f"Grade '{grade_name}' created successfully")
            elif response.status_code == 409:
                self.logger.warning(f"Grade '{grade_name}' already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Grade '{grade_name}' creation failed: Response code {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
    def grade_edit(self):
        
        #click the edit button and click the cancel button
        self.click(Locators.EMP_GRADE_EDIT_BTN)
        time.sleep(2)
        self.click(Locators.EMP_GRADE_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")
        
        #click the edit button and clear the data and click the submit button
        self.click(Locators.EMP_GRADE_EDIT_BTN)
        time.sleep(2)
        self.clear(Locators.EMP_GRADE)
        time.sleep(1)
        self.logger.info("save button clicked successfully")
      
      
        # Click the edit button and update the grade
        self.click(Locators.EMP_GRADE_EDIT_BTN)
        time.sleep(2)
        updated_grade_name = f"Updated Grade {random.randint(5, 10000)}"
        edit_url = "https://ipssapi.techgenzi.com/employee_group_hrm/823/"
        
        response = requests.patch(edit_url, json={
            "types": "Grade",
            "description": "Updated description",
            "employee_group": updated_grade_name
        }, headers=AppTestCase.get_headers())
        
        if response.status_code == 200:
            self.logger.info(f"Grade '{updated_grade_name}' updated successfully")
        else:
            self.logger.error(f"Grade update failed: Response code {response.status_code}")
        
        self.click(Locators.EMP_GRADE_BTN)
        time.sleep(5)
    def village(self):

        fake = Faker()
        self.click(Locators.EMP_VILLAGE_BTN)
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)
        
        # Click the cancel button
        self.click(Locators.EMP_VILLAGE_CANCEL)
        time.sleep(1)
        
        # Attempt to save without entering data
        self.click(Locators.EMP_VILLAGE_SAVE)
        time.sleep(2)
        
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Village name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.EMP_VILLAGE_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Village name is not entered but may be submitted or not shown the error. Test failed.")
        
        # Save the village with a unique name
        village_name = fake.city()
        self.enter_text(Locators.EMP_VILLAGE, "village")
        time.sleep(1)
        self.click(Locators.EMP_VILLAGE_SAVE)
        time.sleep(2)
        self.logger.info("save button is working fine")
        
        # API call to create a village
        url = "https://ipssapi.techgenzi.com/village_hrm/"
        
        try:
            response = requests.post(url, json={"villagename": village_name}, headers=AppTestCase.get_headers())
            if response.status_code == 200:
                self.logger.info(f"Village '{village_name}' created successfully")
            elif response.status_code == 409:
                self.logger.warning(f"Village '{village_name}' already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Village '{village_name}' creation failed: Response code {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
        self.driver.execute_script("window.scrollBy(0,250)")
        time.sleep(2)
        
        # Click the edit button and update the village
        self.click(Locators.EMP_VILLAGE_EDIT_BTN)
        time.sleep(2)
        updated_village_name = fake.city()
        edit_url = "https://ipssapi.techgenzi.com/village_hrm/140562"
        
        response = requests.patch(edit_url, json={"villagename": updated_village_name}, headers=AppTestCase.get_headers())
        
        if response.status_code == 200:
            self.logger.info(f"Village '{updated_village_name}' updated successfully")
        else:
            self.logger.error(f"Village update failed: Response code {response.status_code}")
        
        self.click(Locators.EMP_VILLAGE_BTN)
        time.sleep(5)
    def attrition(self):
        self.driver.execute_script("window.scrollBy(0,500)")
        time.sleep(2)
        self.click(Locators.ATTR_BTN)
        time.sleep(5)
        
        self.driver.execute_script("window.scrollBy(0,300)")
        time.sleep(2)
        #click the cancel button
        self.click(Locators.ATTRITIION_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")

        #click the save button and check required message
        self.click(Locators.ATTRITION_SAVE)
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.REQUIRED_MESSAGE).text
        if error_message.strip() == "Required input field":
            self.logger.warning("Attrition name is not entered, so not submitted. Test passed.")
            time.sleep(1)
            self.click(Locators.ATTRITIION_CANCEL)
            time.sleep(1)
        else:
            self.logger.error("Attrition name is not entered but may be submitted or not shown the error. Test failed.")

        #clicking save the Attrition
        self.enter_text(Locators.ATTRITION_REASON_NAME,"LEAVE")
        time.sleep(1)
        self.click(Locators.ATTRITION_SAVE)
        time.sleep(2)
        self.logger.info("save button clicked successfully")


        # API call to create a Attrition
        url = "https://ipssapi.techgenzi.com/resign/attri_config_hrm/"
        random_number = random.randint(1, 10000)
        attrition_name = f"Attrition Reason {random_number}"
        
        try:
            response = requests.post(url, json={
    "reason_name": attrition_name
}, headers=AppTestCase.get_headers())
            if response.status_code == 200:
                self.logger.info(f"Attrition '{attrition_name}' created successfully")
            elif response.status_code == 409:
                self.logger.warning(f"Attrition '{attrition_name}' already exists: Response code {response.status_code}")
            else:
                self.logger.error(f"Attrition '{attrition_name}' creation failed: Response code {response.status_code}")
        except requests.RequestException as e:
            self.logger.error(f"An error occurred: {e}")
            raise e
    def edit_attrition_reason(self):
        # self.driver.execute_script("window.scrollBy(0,300)")
        # time.sleep(2)
        
        #click the edit button and click the cancel button
        self.click(Locators.ATTRITION_EDIT)
        time.sleep(2)
        self.click(Locators.ATTRITIION_CANCEL)
        time.sleep(1)
        self.logger.info("Cancel button clicked successfully")
        
        #click the edit button and clear the data and click the submit button
        self.click(Locators.ATTRITION_EDIT)
        time.sleep(2)
        self.clear(Locators.ATTRITION_REASON_NAME)
        time.sleep(1)
        self.logger.info("save button clicked successfully")
      
      
        # Click the edit button and update the Attrition
        self.click(Locators.ATTRITION_EDIT)
        time.sleep(2)
        updated_Attrition_name = f"Updated Attrition {random.randint(5, 10000)}"
        edit_url = "https://ipssapi.techgenzi.com/resign/attri_config_hrm/57"
        
        response = requests.patch(edit_url, json={
    "reason_name": updated_Attrition_name,
    "attri_config_id": 57
}, headers=AppTestCase.get_headers())
        
        if response.status_code == 200:
            self.logger.info(f"Attrition '{updated_Attrition_name}' updated successfully")
        else:
            self.logger.error(f"Attrition update failed: Response code {response.status_code}")
        
        self.click(Locators.ATTR_BTN)
        time.sleep(5)

    def do_configurtion(self):
        self.con_tab()
        self.band()
        self.edit_band()
        self.group()
        self.edit_group()
        self.dept()
        self.edit_dept()
        self.grade()
        self.grade_edit()
        self.designation()
        self.village()
        self.attrition()
        self.edit_attrition_reason()
