import allure
from pages.recovery_password import RecoveryPassword


class TestCheckRecoveryPasswordPage:

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_check_recovery_password_page(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.click_on_recovery_password()
        assert recovery_password.get_text_recovering_password() == 'Восстановление пароля'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('ввод почты и клик по кнопке «Восстановить»')
    def test_input_mail_and_click_button_recovery(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.click_on_recovery_password()
        recovery_password.fill_field_user_email()
        recovery_password.click_on_recovery_button()
        assert recovery_password.get_text_write_text_from_email() == 'Введите код из письма'

    @allure.title('Проверка функции: Восстановление пароля')
    @allure.description('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_button(self, browser):
        recovery_password = RecoveryPassword(browser)
        recovery_password.click_on_account_entry()
        recovery_password.fill_field_user_password()
        recovery_password.click_on_eye_button()
        result = recovery_password.check_field_is_active()
        assert result
