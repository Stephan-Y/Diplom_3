from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
from data.data import UserData as ud
from pages.base_page import (BasePage)


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def authorize(self):
        self.click_on_element(rp.ACCOUNT_ENTRY)
        self.fill_field(rp.INPUT_USER_EMAIL, ud.email)
        self.fill_field(rp.INPUT_PASSWORD_USER, ud.password)
        self.click_on_element(rp.ENTER_BUTTON)
