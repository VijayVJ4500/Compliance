import time

from Utilities.base import Basepage
from Utilities.locators import Locators


class Group(Basepage):

    def __init__(self, driver):
        super().__init__(driver)


    def group_page(self):
        self.click(Locators.MENU)
        time.sleep(2)
        self.click(Locators.CONFIGURE)
        time.sleep(2)
        self.click(Locators.GROUP)
        time.sleep(2)
        self.send_keys(Locators.GROUP_TITLE,"Fire")
        time.sleep(2)
        self.send_keys(Locators.GROUP_DESC,"Safty group")
        time.sleep(2)
        self.click(Locators.GROUP_ICON)
        time.sleep(2)
        self.send_keys(Locators.GROUP_ICON_SEARCH,"Fire")
        time.sleep(2)
        self.click(Locators.GROUP_ICON_FIRE)
        time.sleep(2)
        self.click(Locators.GROUP_ADD)
        time.sleep(2)

        # Edit the group
        self.click(Locators.GROUP_EDIT)
        time.sleep(2)
        self.clear(Locators.GROUP_TITLE)
        time.sleep(2)
        self.send_keys(Locators.GROUP_TITLE,"Fire Safty")
        time.sleep(2)
        self.clear(Locators.GROUP_DESC)
        time.sleep(2)
        self.send_keys(Locators.GROUP_DESC, "Fire Safty Group")
        time.sleep(2)
        self.click(Locators.GROUP_UPDATE)
        time.sleep(2)

        # Delete the group
        self.click(Locators.GROUP_DELETE)
        time.sleep(2)

