import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.mark.usefixtures("setup")
class Basepage():

    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_enabled(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_enable()

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def send_keys(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def to_hover(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def is_element_present(self, by_locator):
        try:
            self.driver.find_elements(by_locator[0], by_locator[1])
        except NoSuchElementException:
            return False
        return True

    def is_element_clickable(self, by_locator):
        try:
            self.driver.find_elements(by_locator[0], by_locator[1])
        except NoSuchElementException:
            return False
        return True

    def get_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def get_attribute(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).get_attribute('value')

    def is_selected(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_selected()

    def located_elements(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    def clear(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
            Keys.CONTROL + 'a' + Keys.DELETE)

    def static_dropdown(self, by_locator, text):
        a = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))

        for b in a:

            if b.text == text:
                b.click()

    def dropdown_click(self, by_locator, n=1, search=''):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(search)
        for i in range(n):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(
                Keys.ARROW_DOWN)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def scroll_down(self, scroll):
        script = "window.scrollBy(0,{})"
        return self.driver.execute_script(script.format(scroll))

    def specific_horizontal_scroll(self, by_locator, scroll=0):
        source = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ActionChains(self.driver).drag_and_drop_by_offset(source, scroll, 0).perform()

    # def test_drag_and_drop(self):
    #
    #
    #
    #     # source_element = browser.find_element(By.ID, "source_element_id")
    #     # target_element = browser.find_element(By.ID, "target_element_id")
    #
    #     WebDriverWait(browser, 10).until(EC.visibility_of(source_element))
    #     WebDriverWait(browser, 10).until(EC.visibility_of(target_element))
    #
    #     action_chains = ActionChains(browser)
    #     action_chains.drag_and_drop(source_element, target_element).perform()
    #
    #     WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "target_element_id"), "Dropped!"))

    def drag_and_drop(self, by_source, by_target):
        source = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_source))
        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_target))
        # ActionChains(self.driver).drag_and_drop(source, target).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(source, 100, 170).perform()

    # ActionChains(self.driver).click_and_hold(source).pause(2).move_to_element(target).perform()
    # ActionChains(self.driver).click_and_hold(source).pause(2).move_to_element_with_offset(target,100,100).perform()

    def required_error_msg(self, by_locators):
        validation_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locators))
        print(f"Validation Message: {validation_message.text}")

    def specific_vertical_scroll(self, by_locator, scroll=0):
        source = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return ActionChains(self.driver).drag_and_drop_by_offset(source, scroll, 0).perform()

    def file_upload(self, by_locator, file_path):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).send_keys(file_path)
