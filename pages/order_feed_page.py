import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Проверка наличия деталей заказа в модульном окне")
    def check_modal_window_with_order_details_opened(self):
        if self.find(OrderFeedPageLocators.ORDER_DETAILS):
            return True
