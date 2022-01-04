from selenium.webdriver.common.by import By


class BasketLocators:
    BASKET_QUANTITY = (By.CLASS_NAME, "cart-quantity")
    BASKET = (By.CSS_SELECTOR, "i.material-icons")
    BUY_BTN = (By.CLASS_NAME, "btn red btn-small")
    BASKET_CAPTION = (By.CSS_SELECTOR, "li.collection-item")
    BASKET_REMOVE_ITEM = (By.XPATH, ".//i[@class = 'material-icons basket-quantity' and text()='remove'")
    BASKET_ADD_ITEM = (By.XPATH, ".//i[@class = 'material-icons basket-quantity' and text()='add'")
    BASKET_CLOSE_ITEM = (By.XPATH, ".//i[@class = 'material-icons basket-delete' and text()='close'")
