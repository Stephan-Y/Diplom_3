from selenium.webdriver.common.by import By


class ConstructionPageLocators:
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    BUY_BURGER = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/img')
    CHECK_TEXT_DITAIL_INGREDIENT = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    CLOSE_INGREDIENT_WINDOW = (By.XPATH, '//button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    CHECK_INGREDIENT_COUNT = (By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj')]//p[contains(@class, 'counter_counter__num__3nue1')]")
    BASKET = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul')
    CLICK_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    CHECK_SUCCESSFUL_ORDER_WINDOW = ([By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//p[text()='идентификатор заказа']"])