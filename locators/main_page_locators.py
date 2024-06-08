from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_AUTHORIZE_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    CHECK_TEXT_ACCOUNT_PAGES = (By.XPATH, '//p[@class="Account_text__fZAIn text text_type_main-default"]')
    ACCOUNT_USER_BUTTON = (By.XPATH, '//p[@class="AppHeader_header__linkText__3q_va ml-2"]')
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    CHECK_TEXT_ORDER_HISTORY = (By.XPATH, '//p[contains(text(), "Выполнен")]')
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_LIST = (By.XPATH, "//p[text() = 'Лента Заказов']")
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    CONSTRUCTION_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    CHECK_PAGE_IN_CONSTRUCTION_PAGE = (By.CSS_SELECTOR, 'h1.text.text_type_main-large.mb-5.mt-10')
