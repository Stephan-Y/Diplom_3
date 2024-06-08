import allure
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rpl
from pages.base_page import BasePage


class RecoveryPassword(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("Клик на первый ингредиент")
    def click_on_account_entry(self):
        self.click_on_element(rpl.ACCOUNT_ENTRY)

    @allure.step("Клик на первый ингредиент")
    def click_on_recovery_password(self):
        self.click_on_element(rpl.RECOVERY_PASSWORD)

    @allure.step("Проверяем переход на детали ингредиента")
    def get_text_ditail_ingredient(self):
        return self.get_element_text(cp.CHECK_TEXT_DITAIL_INGREDIENT)