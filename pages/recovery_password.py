import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rpl
from locators.personal_account_page_locator import ConstructionPageLocators as cpl
from data.data import UserData as UD
from pages.base_page import BasePage


class RecoveryPassword(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Клик на первый ингредиент")
    def click_on_account_entry(self):
        self.wait_element(rpl.ACCOUNT_ENTRY)
        self.click_on_element(rpl.ACCOUNT_ENTRY)

    @allure.step("Клик на первый ингредиент")
    def click_on_recovery_password(self):
        self.click_on_element(rpl.RECOVERY_PASSWORD)

    @allure.step("Проверяем переход на детали ингредиента")
    def get_text_ditail_ingredient(self):
        return self.get_element_text(cpl.CHECK_TEXT_DITAIL_INGREDIENT)

    @allure.step("Получаем текст ")
    def get_text_on_recovery_password(self):
        self.wait_element(rpl.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)
        return self.get_element_text(rpl.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)

    @allure.step("Заполняем поле Почта пользователя")
    def fill_field_user_email(self):
        self.fill_field(rpl.INPUT_USER_EMAIL, UD.email)

    @allure.step("Клик на Восстановление пароля")
    def click_on_recovery_button(self):
        self.wait_element(rpl.RECOVERY_BUTTON)
        self.click_on_element(rpl.RECOVERY_BUTTON)

    @allure.step("Проверяем активное поле")
    def check_field_is_active(self):
        return self.find_element_with_waiting(rpl.CHECK_ACTIV_EYE_BUTTON)

    @allure.step("Проверяем наличие тектста 'Введите код из письма'")
    def get_text_write_text_from_email(self):
        return self.get_element_text(rpl.CHECK_TEXT_RECOVERY_PASSWORD)

    @allure.step("Проверка наличия текста 'Восстановление пароля'")
    def get_text_recovering_password(self):
        return self.get_element_text(rpl.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)

    @allure.step("Заполняем поле Пароль пользователя")
    def fill_field_user_password(self):
        self.wait_element(rpl.INPUT_PASSWORD_USER)
        self.fill_field(rpl.INPUT_PASSWORD_USER, UD.password)

    @allure.step("Клик на кнопку видимости пароля Глаз")
    def click_on_eye_button(self):
        self.wait_element(rpl.EYE_BUTTON)
        self.click_on_element(rpl.EYE_BUTTON)