from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.actions = ActionChains(browser)

    def find_element_with_waiting(self, locator, time=20):
        WebDriverWait(self.browser, time).until(ec.visibility_of_element_located(locator))
        return self.browser.find_element(*locator)

    def click_on_element(self, locator, time=30):
        click = ActionChains(self.browser)
        element = self.find_element_with_waiting(locator, time)
        click.move_to_element(element).click().perform()

    def get_element_text(self, locator):
        return self.find_element_with_waiting(locator).text

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
