from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
from pages.base_page import BasePage
from data.data import UserData as ud
import allure


class TestCheckRecoveryPasswordPage:

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_check_recovery_password_page(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.ACCOUNT_ENTRY)
        base_page.click_on_element(rp.RECOVERY_PASSWORD)
        assert base_page.get_element_text(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE) == 'Восстановление пароля'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_mail_and_click_button_recovery(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.ACCOUNT_ENTRY)
        base_page.click_on_element(rp.RECOVERY_PASSWORD)
        base_page.fill_field(rp.INPUT_USER_EMAIL, ud.email)
        base_page.click_on_element(rp.RECOVERY_BUTTON)
        assert base_page.get_element_text(rp.CHECK_TEXT_RECOVERY_PASSWORD) == 'Введите код из письма'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button(self, browser):
        base_page = BasePage(browser)
        base_page.click_on_element(rp.ACCOUNT_ENTRY)
        base_page.fill_field(rp.INPUT_PASSWORD_USER, ud.password)
        base_page.click_on_element(rp.EYE_BUTTON)
        assert base_page.wait_element(rp.CHECK_ACTIV_EYE_BUTTON) is not None
