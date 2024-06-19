from pages.login_page import LoginPage
import allure


class TestPersonalAccount:
    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_click_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.wait_account_button()
        login_page.click_account_button()
        assert login_page.get_check_text_account_pages() == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход в раздел «История заказов»,')
    def test_click_order_history(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_account_button()
        login_page.click_on_order_history()
        assert login_page.get_text_order_history() in "Выполнен"

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('Выход из аккаунта.')
    def test_exit_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_account_button()
        login_page.click_on_exit_button()
        login_page.click_on_recovery_password()
        assert login_page.get_text_on_recovery_password_page() == 'Восстановление пароля'
