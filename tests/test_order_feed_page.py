import time
from pages.order_feed_page import OrderPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators as mp, MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators as of
from locators.personal_account_page_locator import ConstructionPageLocators as cp
import allure


class TestOrderFeed:

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_order_details(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.ORDER_LIST)
        order_page.click_on_element(of.FIRST_ORDER)
        assert order_page.check_modal_window_with_order_details_opened()

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_order_show_page_order_feed(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find(cp.BUY_BURGER)
        target = login_page.find(cp.BASKET)
        login_page.drag_and_drop_method(source, target)
        login_page.click_on_element(cp.CLICK_ORDER)
        login_page.click_on_element(of.CLOSE_MODAL_WIND)
        login_page.click_on_element(MainPageLocators.ORDER_LIST)
        order_page.wait_element(of.COUNT_ORDER_INDICATOR)
        order_count = '#0'+login_page.get_element_text(of.COUNT_ORDER_INDICATOR)
        login_page.click_on_element(mp.ACCOUNT_AUTHORIZE_BUTTON)
        login_page.click_on_element(mp.ORDER_HISTORY)
        order_count_in_account = login_page.get_element_text(of.COUNT_ORDER_INDICATOR_IN_PERSONAL_ACCOUNT)
        assert order_count in order_count_in_account

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_counter_is_increacing_all_time(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.ORDER_LIST)
        all_time_orders = order_page.get_element_text(of.COUNT_ALL_TIME)
        login_page.click_on_element(MainPageLocators.ACCOUNT_USER_BUTTON)
        source = login_page.find(cp.BUY_BURGER)
        target = login_page.find(cp.BASKET)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.CLICK_ORDER)
        order_page.click_on_element(of.CLOSE_MODAL_WIND)
        order_page.click_on_element(mp.ORDER_LIST)
        all_time_orders_after = order_page.get_element_text(of.COUNT_ALL_TIME)
        assert all_time_orders < all_time_orders_after

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_counter_is_increacing_today(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_element(mp.ORDER_LIST)
        all_time_orders = order_page.get_element_text(of.COUNT_TODAY)
        login_page.click_on_element(MainPageLocators.ACCOUNT_USER_BUTTON)
        source = order_page.find(cp.BUY_BURGER)
        target = order_page.find(cp.BASKET)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.CLICK_ORDER)
        order_page.wait_element(of.CLOSE_MODAL_WIND)
        order_page.click_on_element(of.CLOSE_MODAL_WIND)
        order_page.click_on_element(mp.ORDER_LIST)
        all_time_orders_after = order_page.get_element_text(of.COUNT_TODAY)
        assert all_time_orders < all_time_orders_after

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_show_in_list_in_progress(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = order_page.find(cp.BUY_BURGER)
        target = order_page.find(cp.BASKET)
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_element(cp.CLICK_ORDER)
        order_page.click_on_element(of.CLOSE_MODAL_WIND)
        order_page.click_on_element(mp.ORDER_LIST)
        order_page.wait_element(of.COUNT_ORDER_INDICATOR)
        number_order = '0'+login_page.get_element_text(of.COUNT_ORDER_INDICATOR)
        time.sleep(3)
        in_progress = order_page.get_element_text(of.ORDER_IN_PROGRESS)
        assert number_order == in_progress
