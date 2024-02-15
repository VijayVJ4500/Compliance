import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Actionstage(Basepage):

    def __init__(self, driver):
        super().__init__(driver)

    def actionstage_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.ACTION_STAGE)
        time.sleep(2)
        self.click(Locators.ACTION_STAGE_ADD)
        time.sleep(2)
        self.send_keys(Locators.ACTION_LEVEL,"5")
        time.sleep(2)
        self.send_keys(Locators.ACTION_STAGE_NAME,"Verifiyed")
        time.sleep(2)
        self.send_keys(Locators.ACTION_STAGE_DESC,"Final stage")
        time.sleep(2)
        # self.click(Locators.ACTION_LAST_STAGE)
        # time.sleep(2)
        self.click(Locators.ACTION_STAGE_SUBMIT)
        time.sleep(2)
        # self.click(Locators.ACTION_STAGE_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_EDIT)
        # time.sleep(2)
        # self.click(Locators.ACTION_LAST_STAGE)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_UPDATE)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_CHECKBOX)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_DELETE)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_DELETE_YES)
        # time.sleep(2)
        # self.click(Locators.ACTION_STAGE_DOWNLOAD)
        # time.sleep(2)


