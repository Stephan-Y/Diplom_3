import allure
from locators.main_page_locators import MainPageLocators as mp
from locators.personal_account_page_locator import ConstructionPageLocators as cp, ConstructionPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("")
    def check_close_modal_window_ingredient(self):
        self.click_on_element(cp.FIRST_INGREDIENT)
        self.wait_element(cp.CHECK_TEXT_DITAIL_INGREDIENT)
        self.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT)
        self.wait_element(cp.CLOSE_INGREDIENT_WINDOW)
        self.click_on_element(cp.CLOSE_INGREDIENT_WINDOW)

    @allure.step("Получаем первый ингредиент")
    def get_first_count_ingredient(self):
        return self.find(cp.FIRST_INGREDIENT).text

    @allure.step("Проверяем всплывающее окно с успешно созданным заказом")
    def check_order_placed(self):
        if self.find(ConstructionPageLocators.CHECK_SUCCESSFUL_ORDER_WINDOW):
            return True

    @allure.step("Клик на список заказов")
    def click_on_order_list(self):
        self.click_on_element(mp.ORDER_LIST)

    @allure.step("Получаем количество заказов")
    def get_total_order_count(self):
        return self.get_element_text(mp.TOTAL_ORDER_COUNT)

    @allure.step("Клик на конструктор")
    def click_on_construction_button(self):
        self.click_on_element(mp.CONSTRUCTION_BUTTON)

    @allure.step("Проверяем переход на конструктор бургера")
    def get_text_on_construction_page(self):
        return self.get_element_text(mp.CHECK_PAGE_IN_CONSTRUCTION_PAGE)

    @allure.step("Клик на первый ингредиент")
    def click_on_first_ingredient(self):
        self.click_on_element(cp.FIRST_INGREDIENT)

    @allure.step("Проверяем переход на детали ингредиента")
    def get_text_ditail_ingredient(self):
        return self.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT)

    @allure.step("Проверяем переход на детали ингредиента")
    def get_count_of_ingredient(self):
        return self.get_element_text(cp.CHECK_INGREDIENT_COUNT)
