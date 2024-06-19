import allure
from locators.personal_account_page_locator import ConstructionPageLocators as cp
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
from locators.main_page_locators import MainPageLocators as mpl
from locators.order_feed_page_locators import OrderFeedPageLocators as ofl
from data.data import UserData as ud
from pages.base_page import (BasePage)


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Авторизация")
    def authorize(self):
        self.wait_element(rp.ACCOUNT_ENTRY)
        self.find_element_with_waiting(rp.ACCOUNT_ENTRY)
        self.click_on_element(rp.ACCOUNT_ENTRY)
        self.wait_element(rp.INPUT_USER_EMAIL)
        self.fill_field(rp.INPUT_USER_EMAIL, ud.email)
        self.fill_field(rp.INPUT_PASSWORD_USER, ud.password)
        self.wait_element(rp.ENTER_BUTTON)
        self.find_element_with_waiting(rp.ENTER_BUTTON)
        self.click_on_element(rp.ENTER_BUTTON)

    @allure.step("Находим бургер")
    def find_burger(self):
        self.wait_element(cp.BUY_BURGER)
        return self.find_element_with_waiting(cp.BUY_BURGER)

    @allure.step("Находим корзину")
    def find_basket(self):
        self.wait_element(cp.BASKET)
        return self.find_element_with_waiting(cp.BASKET)

    @allure.step("Клик по заказу")
    def click_order(self):
        self.wait_element(cp.CLICK_ORDER)
        self.click_on_element(cp.CLICK_ORDER)

    @allure.step("Клик по кнопке авторизации")
    def click_account_button(self):
        self.wait_element(mpl.ACCOUNT_AUTHORIZE_BUTTON)
        self.find_element_with_waiting(mpl.ACCOUNT_AUTHORIZE_BUTTON)
        self.click_on_element(mpl.ACCOUNT_AUTHORIZE_BUTTON)

    @allure.step("Проверка перехода на страницу личного кабинета")
    def get_check_text_account_pages(self):
        self.wait_element(mpl.CHECK_TEXT_ACCOUNT_PAGES)
        return self.get_element_text(mpl.CHECK_TEXT_ACCOUNT_PAGES)

    @allure.step("Ожидание кнопки Личный кабинет")
    def wait_account_button(self):
        self.wait_element(mpl.ACCOUNT_AUTHORIZE_BUTTON)

    @allure.step("Клик на историю заказов")
    def click_on_order_history(self):
        self.wait_element(mpl.ORDER_HISTORY)
        self.find_element_with_waiting(mpl.ORDER_HISTORY)
        self.click_on_element(mpl.ORDER_HISTORY)

    @allure.step('получаем текст "Выполнен" на странице')
    def get_text_order_history(self):
        self.wait_element(mpl.CHECK_TEXT_ORDER_HISTORY)
        return self.get_element_text(mpl.CHECK_TEXT_ORDER_HISTORY)

    @allure.step("Клик на кнопку выхода")
    def click_on_exit_button(self):
        self.wait_element(mpl.EXIT_BUTTON)
        self.click_on_element(mpl.EXIT_BUTTON)

    @allure.step("Клик на восстановление пароля")
    def click_on_recovery_password(self):
        self.wait_element(rp.RECOVERY_PASSWORD)
        self.click_on_element(rp.RECOVERY_PASSWORD)

    @allure.step("Проверка текста на страние восстановления пароля")
    def get_text_on_recovery_password_page(self):
        self.wait_element(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)
        return self.get_element_text(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)

    @allure.step("Клик на личный кабинет")
    def click_on_account_user_button(self):
        self.wait_element(mpl.ACCOUNT_USER_BUTTON)
        self.click_on_element(mpl.ACCOUNT_USER_BUTTON)

    @allure.step("Получаем номер заказа в личном аккаунте")
    def get_text_order_indicator_in_personal_account(self):
        self.wait_element(ofl.COUNT_ORDER_INDICATOR_IN_PERSONAL_ACCOUNT)
        return self.get_element_text(ofl.COUNT_ORDER_INDICATOR_IN_PERSONAL_ACCOUNT)