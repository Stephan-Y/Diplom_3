import allure
from locators.personal_account_page_locator import ConstructionPageLocators as cp
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
from locators.main_page_locators import MainPageLocators as mpl
from data.data import UserData as ud
from pages.base_page import (BasePage)


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Авторизация")
    def authorize(self):
        self.find_element_with_waiting(rp.ACCOUNT_ENTRY)
        self.click_on_element(rp.ACCOUNT_ENTRY)
        self.fill_field(rp.INPUT_USER_EMAIL, ud.email)
        self.fill_field(rp.INPUT_PASSWORD_USER, ud.password)
        self.find_element_with_waiting(rp.ENTER_BUTTON)
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

    @allure.step("Клик по кнопке авторизации")
    def click_account_button(self):
        self.find_element_with_waiting(mpl.ACCOUNT_AUTHORIZE_BUTTON)
        self.click_on_element(mpl.ACCOUNT_AUTHORIZE_BUTTON)

    @allure.step("Проверка перехода на страницу личного кабинета")
    def get_check_text_account_pages(self):
        return self.get_element_text(mpl.CHECK_TEXT_ACCOUNT_PAGES)

    @allure.step("Ожидание кнопки Личный кабинет")
    def wait_account_button(self):
        self.wait_element(mpl.ACCOUNT_AUTHORIZE_BUTTON)

    @allure.step("Клик на историю заказов")
    def click_on_order_history(self):
        self.find_element_with_waiting(mpl.ORDER_HISTORY)
        self.click_on_element(mpl.ORDER_HISTORY)

    @allure.step('получаем текст "Выполнен" на странице')
    def get_text_order_history(self):
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
        return self.get_element_text(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)