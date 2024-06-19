from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    FIRST_ORDER = (By.CLASS_NAME, "OrderHistory_dataBox__1mkxK")
    CHECK_TEXT_DETAIL_ORDER = (By.XPATH, '//p[@class, "text text_type_main-medium mb-8"]')
    COUNT_ORDER_INDICATOR = (By.XPATH, ".//div/p[text()='Выполнено за все время:']/following-sibling::p")
    COUNT_ORDER_INDICATOR_IN_PERSONAL_ACCOUNT = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')]/ p[@class='text text_type_digits-default'])[last()]")
    COUNT_ALL_TIME = (By.XPATH, "//p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large'][1]")
    COUNT_TODAY = (By.XPATH, ".//div/p[text()='Выполнено за сегодня:']/following-sibling::p[text()=.]")
    CLOSE_MODAL_WIND = (By.XPATH, '//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    ORDER_DETAILS = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//ul/li/div[contains(@class, 'Modal_imgBox')]"]
    TEXT_ALL_ORDERS_ARE_READY =  [By.XPATH, ".//li[contains(text(),'Все текущие заказы готовы!')]"]


