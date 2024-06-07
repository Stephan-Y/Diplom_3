from pages.main_page import MainPage
from pages.login_page import LoginPage
import allure


class TestMainFunctional:

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Конструктор»')
    def test_click_construction(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_order_list()
        assert main_page.get_total_order_count() is not None

    @allure.title('Проверка основного функционала')
    @allure.description('переход по клику на «Лента заказов»')
    def test_click_constructions(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_order_list()
        main_page.click_on_construction_button()
        assert main_page.get_text_on_construction_page() == 'Соберите бургер'

    @allure.title('Проверка основного функционала')
    @allure.description('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.click_on_first_ingredient()
        assert main_page.get_text_ditail_ingredient() == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('всплывающее окно закрывается кликом по крестику')
    def test_close_pop_up_windows_ingredients(self, browser):
        main_page = MainPage(browser)
        main_page.check_close_modal_window_ingredient()
        assert main_page.get_text_ditail_ingredient() == 'Детали ингредиента'

    @allure.title('Проверка основного функционала')
    @allure.description('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredients(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        count_start = main_page.get_count_of_ingrefient()
        source = login_page.find_burger()
        target = login_page.find_basket()
        login_page.drag_and_drop_method(source, target)
        count_finish = main_page.get_count_of_ingrefient()
        assert count_start < count_finish

    @allure.title('Проверка основного функционала')
    @allure.description('залогиненный пользователь может оформить заказ')
    def test_authorized_order(self, browser):
        main_page = MainPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find_burger()
        target = login_page.find_basket()
        login_page.drag_and_drop_method(source, target)
        login_page.click_order()
        assert main_page.check_order_placed()
