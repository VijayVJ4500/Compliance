import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Manage_document(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def manage_document_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.MANAGE_DOCUMENT)
        time.sleep(2)
        self.click(Locators.MANAGE_DOC_CLICK)
        time.sleep(2)
        # self.click(Locators.MANAGE_DOC_ADD)
        # time.sleep(2)
        # self.send_keys(Locators.MANAGE_DOC_FIRST_INPUT, "235456")
        # time.sleep(2)
        # self.dropdown_click(Locators.MANAGE_DOC_SEC_INPUT, 1, "uyYBl")
        # time.sleep(2)
        # # self.click(Locators.MANAGE_DOC_THR_INPUT)
        # # time.sleep(2)
        # self.file_upload(Locators.MANAGE_DOC_THR_INPUT, r'C:\Users\vijay\PycharmProjects\Compliance\FileUpload.pdf')
        # time.sleep(2)
        # self.click(Locators.MANAGE_DOC_FOUR_INPUT)
        # time.sleep(2)
        # self.send_keys(Locators.MANAGE_DOC_FOUR_INPUT,"05-02-2024")
        # time.sleep(2)
        # self.click(Locators.MANAGE_DOC_SUBMIT)
        # time.sleep(2)

        self.click(Locators.MANAGE_DOC_CHECKBOX)
        time.sleep(2)
        self.click(Locators.MANAGE_DOC_EDIT)
        time.sleep(2)
        self.click(Locators.MANAGE_DOC_UPLOAD_DELETE)
        time.sleep(2)
        self.file_upload(Locators.MANAGE_DOC_THR_INPUT, r'C:\Users\vijay\Downloads\Form Report- 22-Jan-2024 (1).pdf')
        time.sleep(2)
        self.click(Locators.MANAGE_DOC_SUBMIT)
        time.sleep(2)


