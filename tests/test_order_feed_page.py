from pages.order_feed_page import OrderPage
from pages.login_page import LoginPage
import allure


class TestOrderFeed:

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_show_in_list_in_progress(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find_burger()
        target = login_page.find_basket()
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_make_order()
        order_page.click_on_close_modal_wind()
        order_page.click_on_order_list()
        number_order = order_page.get_text_number_of_order()
        order_page.skip_text_all_orders_are_ready()
        in_progress = order_page.get_text_order_in_progress()
        assert number_order == in_progress

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order_open_order_details(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_order_list()
        order_page.click_on_first_order()
        assert order_page.check_modal_window_with_order_details_opened()

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_history_order_show_page_order_feed(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        source = login_page.find_burger()
        target = login_page.find_basket()
        login_page.drag_and_drop_method(source, target)
        order_page.click_on_make_order()
        order_page.click_on_close_modal_wind()
        order_page.click_on_order_list()
        order_count = f'#{order_page.get_text_number_of_order()}'
        login_page.click_account_button()
        login_page.click_on_order_history()
        order_count_in_account = login_page.get_text_order_indicator_in_personal_account()
        assert order_count in order_count_in_account

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_new_order_counter_is_increasing_all_time(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_order_list()
        all_time_orders = order_page.get_text_count_all_time()
        login_page.click_on_account_user_button()
        source = login_page.find_burger()
        target = login_page.find_basket()
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_make_order()
        order_page.click_on_close_modal_wind()
        order_page.click_on_order_list()
        all_time_orders_after = order_page.get_text_count_all_time()
        assert int(all_time_orders) < int(all_time_orders_after)

    @allure.title('Проверка раздела: «Лента заказов»')
    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_new_order_counter_is_increasing_today(self, browser):
        order_page = OrderPage(browser)
        login_page = LoginPage(browser)
        login_page.authorize()
        order_page.click_on_order_list()
        all_time_orders = order_page.get_text_count_today()
        login_page.click_on_account_user_button()
        source = login_page.find_burger()
        target = login_page.find_basket()
        order_page.drag_and_drop_method(source, target)
        order_page.click_on_make_order()
        order_page.click_on_close_modal_wind()
        order_page.click_on_order_list()
        browser.refresh()
        all_time_orders_after = order_page.get_text_count_today()
        assert int(all_time_orders) < int(all_time_orders_after)
