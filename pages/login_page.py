import allure
from locators.personal_account_page_locator import ConstructionPageLocators as cp
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
from data.data import UserData as ud
from pages.base_page import (BasePage)


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Авторизация")
    def authorize(self):
        self.click_on_element(rp.ACCOUNT_ENTRY)
        self.fill_field(rp.INPUT_USER_EMAIL, ud.email)
        self.fill_field(rp.INPUT_PASSWORD_USER, ud.password)
        self.click_on_element(rp.ENTER_BUTTON)

    @allure.step("Находим бургер")
    def find_burger(self):
        return self.find_element_with_waiting(cp.BUY_BURGER)

    @allure.step("Находим корзину")
    def find_basket(self):
        return self.find_element_with_waiting(cp.BASKET)

    @allure.step("Клик по заказу")
    def click_order(self):
        self.click_on_element(cp.CLICK_ORDER)