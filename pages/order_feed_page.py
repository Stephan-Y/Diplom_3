import allure
from locators.main_page_locators import MainPageLocators as mpl
from locators.order_feed_page_locators import OrderFeedPageLocators as ofl
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


    #@allure.step("")
    #def (self):

    #@allure.step("")
    #def (self):

    #@allure.step("")
    #def (self):

    #@allure.step("")
    #def (self):

    #@allure.step("")
    #def (self):