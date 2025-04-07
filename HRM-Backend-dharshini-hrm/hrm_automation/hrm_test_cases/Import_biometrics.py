import time
import unittest
from hrm_automation.base import BasePage
from hrm_automation.locators import Locators
import random
from hrm_automation.logger_file import get_logger
from faker import Faker
class biometrics(BasePage, unittest.TestCase):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger("Import Biometrics")

    def biometrics_tab(self):
        time.sleep(1)
        self.click(Locators.HOME_SIDEBAR)
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0,400)")
        time.sleep(1)
        self.click(Locators.IMPORT_BIOMETRIC_CARD)
        time.sleep(6)

    def download(self):
        self.click(Locators.IMPORT_CHECK1)
        time.sleep(1)
        # self.click(Locators.IMPORT_CHECK2)
        # time.sleep(1)
        self.click(Locators.IMPORT_DOWNLOADALL)
        time.sleep(30)
        self.logger.info("The Selected Machine punch data downloaded successfully")
        time.sleep(3)
        self.click(Locators.IMPORT_CHECKALL)
        time.sleep(2)
        self.click(Locators.IMPORT_DOWNLOADALL)
        time.sleep(30)
        self.logger.info("All Machine punch data downloaded successfully")
        time.sleep(3)
        self.click(Locators.IMPORT_DOWNLOAD1)
        time.sleep(2)
        self.logger.info("1st Machine data downloaded successfully")
        time.sleep(3)
    def bio_add_tab(self):
        self.click(Locators.IMPORT_BIOMETRIC_ADD)
        time.sleep(7)

    def add(self):

        self.enter_text(Locators.IMPORT_MACHINENAME, 'MACHINE 001')
        time.sleep(2)
        self.click(Locators.IMPORT_CANCEL)
        time.sleep(2)
        # Initialize Faker
        fake = Faker()
        # Generate a fake IPv4 address
        fake_ip = fake.ipv4()

        self.enter_text(Locators.IMPORT_MACHINENAME, 'Machine'+str(random.randint(1000, 9999)))
        time.sleep(1)

        # Automation code using the generated IP address
        self.enter_text(Locators.IMPORT_IP, fake_ip)
        self.enter_text(Locators.IMPORT_PORT, str(random.randint(1000, 9999)))
        time.sleep(2)
        self.click(Locators.IMPORT_SUBMIT)
        time.sleep(2)
        self.click(Locators.IMPORT_ALERT_SUBMIT)
        time.sleep(2)
        self.logger.info("Machine Detail is Added successfully")
        time.sleep(7)
    def edit(self):
        self.click(Locators.IMPORT_EDIT)
        time.sleep(1)
        self.enter_text(Locators.IMPORT_MACHINENAME, 'MAChINE 2001')
        time.sleep(1)
        self.click(Locators.IMPORT_CANCEL)
        time.sleep(1)
        self.click(Locators.IMPORT_EDIT)
        time.sleep(1)
        self.clear(Locators.IMPORT_MACHINENAME)
        time.sleep(1)
        self.clear(Locators.IMPORT_IP)
        time.sleep(1)
        # self.clear(Locators.IMPORT_PORT)
        # time.sleep(1)

        fake = Faker()

        self.enter_text(Locators.IMPORT_MACHINENAME, 'Machine' + str(random.randint(1000, 9999)))
        time.sleep(4)
        # Initialize Faker


        # Generate a fake IPv4 address
        fake_ip = fake.ipv4()

        # Automation code using the generated IP address
        self.enter_text(Locators.IMPORT_IP, fake_ip)
        time.sleep(2)
        # self.enter_text(Locators.IMPORT_PORT, str(random.randint(10000, 9999)))
        # time.sleep(1)
        self.click(Locators.IMPORT_UPDATE)
        time.sleep(1)
        self.click(Locators.IMPORT_ALERT_SUBMIT)
        time.sleep(2)
        self.logger.info("Machine Detail is Updated successfully")
        time.sleep(3)


    def delete(self):
        self.click(Locators.IMPORT_DELETE)
        time.sleep(1)
        self.click(Locators.IMPORT_ALERT_DELETE)
        time.sleep(7)
        self.click(Locators.IMPORT_DELETE_OK)
        time.sleep(1)
        self.logger.info("Machine is deleted successfully")
        time.sleep(1)
        self.click(Locators.IMPORT_BACK)
        time.sleep(1)

    def biometrics_page(self):
        self.biometrics_tab()
        self.bio_add_tab()
        self.add()
        self.edit()
        self.delete()

        self.download()



