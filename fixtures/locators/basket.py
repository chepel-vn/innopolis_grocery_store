from selenium.webdriver.common.by import By
from fixtures.consts.basket import BasketConsts as BC


class BasketLocators:
    BASKET_QUANTITY = (By.CLASS_NAME, "cart-quantity")
    BASKET = (By.CSS_SELECTOR, "i.material-icons")
    BUY_BTN = (By.XPATH, ".//button[text() = 'Buy']")
    BASKET_CAPTION = (By.CSS_SELECTOR, "li.collection-item")
    BASKET_PAYED = (By.CLASS_NAME, "toast")
    BASKET_REMOVE_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and text()='remove']",
    )
    BASKET_ADD_ITEM = (
        By.XPATH,
        ".//i[@class = 'material-icons basket-quantity' and text()='add']",
    )
    BASKET_CLOSE_ITEM = (By.CSS_SELECTOR, "span.secondary-content")
    BASKET_CLOSE = (By.CSS_SELECTOR, "i.material-icons.basket-close")
    BASKET_TOTAL_PRICE = (
        By.XPATH,
        f".//li[@class = 'collection-item active' "
        f"and contains(text(), '{BC.TOTAL_PRICE}')]",
    )
