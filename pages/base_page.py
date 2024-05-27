import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)

    def click_on_element(self, locator):
        button = self.browser.find_element(*locator)
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(locator))
        button.click()

    def get_element_text(self, locator):
        element_dom = self.browser.find_element(*locator)
        return element_dom.text

    def fill_field(self, locator, value):
        field = self.browser.find_element(*locator)
        field.clear()
        field.send_keys(value)

    def find(self, locator):
        return self.browser.find_element(*locator)

    def wait_element(self, locator):
        return WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(locator))

    def drag_and_drop_method(self, source, target):
        self.actions.drag_and_drop(source, target).perform()


