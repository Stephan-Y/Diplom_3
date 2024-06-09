import allure
from locators.main_page_locators import MainPageLocators as mpl
from locators.order_feed_page_locators import OrderFeedPageLocators as ofl
from locators.personal_account_page_locator import ConstructionPageLocators as cpl
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Проверка наличия деталей заказа в модульном окне")
    def check_modal_window_with_order_details_opened(self):
        if self.find(OrderFeedPageLocators.ORDER_DETAILS):
            return True

    @allure.step("клик на лист заказов")
    def click_on_order_list(self):
        self.wait_element(mpl.ORDER_LIST)
        self.click_on_element(mpl.ORDER_LIST)


    @allure.step("Клик на первый заказ")
    def click_on_first_order(self):
        self.wait_element(ofl.FIRST_ORDER)
        self.click_on_element(ofl.FIRST_ORDER)


    @allure.step("Ожидаем появления новреа заказа")
    def skip_text_all_orders_are_ready(self):
        self.wait_element(ofl.TEXT_ALL_ORDERS_ARE_READY)
        self.find_element_with_waiting(ofl.TEXT_ALL_ORDERS_ARE_READY)
        self.wait_element_until_invisibility(ofl.TEXT_ALL_ORDERS_ARE_READY)


    @allure.step("Клик на Заказать")
    def click_on_make_order(self):
        self.wait_element(cpl.CLICK_ORDER)
        self.click_on_element(cpl.CLICK_ORDER)

    @allure.step("Закрываем окно")
    def click_on_close_modal_wind(self):
        self.wait_element(ofl.CLOSE_MODAL_WIND)
        self.click_on_element(ofl.CLOSE_MODAL_WIND)

    @allure.step("Клик на Ленты заказов")
    def click_on_order_list(self):
        self.wait_element(mpl.ORDER_LIST)
        self.click_on_element(mpl.ORDER_LIST)

    @allure.step("")
    def get_text_count_today(self):
        self.wait_element(ofl.COUNT_TODAY)
        return self.get_element_text(ofl.COUNT_TODAY)


    @allure.step("Получаем количество заказов за все время")
    def get_text_count_all_time(self):
        self.wait_element(ofl.COUNT_ALL_TIME)
        return self.get_element_text(ofl.COUNT_ALL_TIME)

    @allure.step("получаем номер заказа")
    def get_text_number_of_order(self):
        self.wait_element(ofl.COUNT_ORDER_INDICATOR)
        return f"0{self.get_element_text(ofl.COUNT_ORDER_INDICATOR)}"


    @allure.step('Получаем номер заказа в процессе приготовления')
    def get_text_order_in_progress(self):
        self.wait_element(ofl.ORDER_IN_PROGRESS)
        return self.get_element_text(ofl.ORDER_IN_PROGRESS)