from locators.personal_account_page_locator import ConstructionPageLocators as cp, ConstructionPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def check_close_modal_window_ingredient(self):
        self.click_on_element(cp.FIRST_INGREDIENT)
        self.wait_element(cp.CHECK_TEXT_DITAIL_INGREDIENT)
        self.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT)
        self.wait_element(cp.CLOSE_INGREDIENT_WINDOW)
        self.click_on_element(cp.CLOSE_INGREDIENT_WINDOW)

    def get_first_count_ingredient(self):
        return self.find(cp.FIRST_INGREDIENT).text

    def check_order_placed(self):
        if self.find(ConstructionPageLocators.CHECK_SUCCESSFUL_ORDER_WINDOW):
            return True
