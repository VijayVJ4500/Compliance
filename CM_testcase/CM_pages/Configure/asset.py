import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Assettype(Basepage):

    def __init__(self, driver):
        super().__init__(driver)


    def assettype_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.ASSET_TYPES)
        time.sleep(2)
        # self.click(Locators.ASSET_ADD)
        # time.sleep(2)
        # self.send_keys(Locators.ADD_ASSET_TYPE,"Law")
        # time.sleep(2)
        # self.send_keys(Locators.ADD_ASSET_PATH,"User")
        # time.sleep(2)
        # self.send_keys(Locators.ADD_ASSET_LABEL1,"Rule")
        # time.sleep(2)
        # self.send_keys(Locators.ADD_ASSET_LABEL2,"Emp")
        # time.sleep(2)
        # # self.click(Locators.ADD_ASSET_CANCEL)
        # # time.sleep(2)
        # self.click(Locators.ADD_ASSET_SUBMIT)
        # time.sleep(2)

        #Edit the Asset types

        self.click(Locators.ASSET_CHECKBOX)
        time.sleep(2)
        self.click(Locators.ASSET_EDIT)
        time.sleep(2)
        self.clear(Locators.ADD_ASSET_LABEL2)
        time.sleep(2)
        self.send_keys(Locators.ADD_ASSET_LABEL2,"Polices")
        time.sleep(2)
        self.click(Locators.ADD_ASSET_SUBMIT)
        time.sleep(2)




