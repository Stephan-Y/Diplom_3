from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    ACCOUNT_ENTRY = (By.XPATH, "//button[text()='Войти в аккаунт']")
    RECOVERY_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
    CHECK_TEXT_ON_RECOVERY_PASSWORD_PAGE = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    INPUT_USER_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    CHECK_TEXT_RECOVERY_PASSWORD = (By.XPATH, "//label[text()='Введите код из письма']")
    INPUT_PASSWORD_USER = (By.XPATH, "//input[@name='Пароль']")
    EYE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon')]")
    CHECK_ACTIV_EYE_BUTTON = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
    ENTER_BUTTON = (By.XPATH, './/button[contains(text(),"Войти")]')
    REGISTER_BUTTON = (By.XPATH, '//button[contains(text(), "Зарегистрироваться")]')
