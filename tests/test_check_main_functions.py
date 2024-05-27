from locators.main_page_locators import MainPageLocators as mp
from locators.personal_account_page_locator import ConstructionPageLocators as cp
from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure


class TestMainFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Конструктор»')
    def test_click_construction(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(mp.ORDER_LIST)
        assert main_page.get_element_text(mp.TOTAL_ORDER_COUNT) is not None

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Лента заказов»')
    def test_click_constructions(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(mp.ORDER_LIST)
        main_page.click_on_element(mp.CONSTRUCTION_BUTTON)
        assert main_page.get_element_text(mp.CHECK_PAGE_IN_CONSTRUCTION_PAGE) == 'Соберите бургер'

    @allure.title('Проверка основного функционала')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_element(cp.FIRST_INGREDIENT)
        assert main_page.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT) == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('всплывающее окно закрывается кликом по крестику')
    def test_close_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.check_close_modal_window_ingredient()
        assert main_page.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT) == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredients(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        count_start = main_page.get_element_text(cp.CHECK_INGREDIENT_COUNT)
        source = login_page.find(cp.BUY_BURGER)
        target = login_page.find(cp.BASKET)
        login_page.drag_and_drop_method(source, target)
        count_finish = main_page.get_element_text(cp.CHECK_INGREDIENT_COUNT)
        assert count_start < count_finish

    @allure.title('Проверка основного функционала')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_authorized_order(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find(cp.BUY_BURGER)
        target = login_page.find(cp.BASKET)
        login_page.drag_and_drop_method(source, target)
        login_page.click_on_element(cp.CLICK_ORDER)
        assert main_page.check_order_placed()
