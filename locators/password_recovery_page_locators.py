from selenium.webdriver.common.by import By


class PasswordRecoveryPage:
    account_entry = (By.XPATH, "//button[text()='Войти в аккаунт']")
    recovery_password = (By.XPATH, ".//a[text()='Восстановить пароль']")
    check_text_on_page_recovery_password = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    input_email_user = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    recovery_button = (By.XPATH, "//button[text()='Восстановить']")
    check_text_code_recovery_password = (By.XPATH, "//label[text()='Введите код из письма']")
    input_password_user = (By.XPATH, "//input[@name='Пароль']")
    eye_button = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    check_activ_eye_button = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
    button_enter = (By.XPATH, './/button[contains(text(),"Войти")]')
    register_button = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
