from locators.main_page_locators import MainPageLocators as mp
from pages.login_page import LoginPage
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators as rp
import allure


class TestPersonalAccount:
    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход по клику на «Личный кабинет»')
    def test_click_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.ACCOUNT_AUTHORIZE_BUTTON)
        login_page.wait_element(mp.CHECK_TET_ACCOUNT_PAGES)
        assert login_page.get_element_text(mp.CHECK_TET_ACCOUNT_PAGES) == 'В этом разделе вы можете изменить свои персональные данные'

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('переход в раздел «История заказов»,')
    def test_click_order_history(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.ACCOUNT_AUTHORIZE_BUTTON)
        login_page.click_on_element(mp.ORDER_HISTORY)
        login_page.wait_element(mp.CHECK_TEXT_ORDER_HISTORY)
        assert login_page.get_element_text(mp.CHECK_TEXT_ORDER_HISTORY) in "Выполнен"

    @allure.title('Проверка раздела: Личный кабинет')
    @allure.description('выход из аккаунта.')
    def test_exit_personal_account(self, browser):
        login_page = LoginPage(browser)
        login_page.authorize()
        login_page.click_on_element(mp.EXIT_BUTTON)
        login_page.wait_element(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE)
        assert login_page.get_element_text(rp.CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE) == 'Восстановление пароля'