
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rpl
from data.data import UserData as UD
import allure
from pages.recovery_password import RecoveryPassword


class TestCheckRecoveryPasswordPage:

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_check_recovery_password_page(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.click_on_recovery_password()
        assert recovery_password.get_element_text(rpl.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE) == 'Восстановление пароля'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_mail_and_click_button_recovery(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.click_on_recovery_password()
        recovery_password.fill_field(rpl.INPUT_USER_EMAIL, UD.email)
        recovery_password.click_on_element(rpl.RECOVERY_BUTTON)
        assert recovery_password.get_element_text(rpl.CHECK_TEXT_RECOVERY_PASSWORD) == 'Введите код из письма'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.fill_field(rpl.INPUT_PASSWORD_USER, UD.password)
        recovery_password.click_on_element(rpl.EYE_BUTTON)
        assert recovery_password.wait_element(rpl.CHECK_ACTIV_EYE_BUTTON) is not None
