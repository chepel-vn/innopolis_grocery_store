import logging

from fixtures.pages.base_page import BasePage
from fixtures.locators.basket import BasketLocators as BL
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("grocery_store")


class BasketPage(BasePage):
    def _buy_button(self) -> WebElement:
        buy_button = self.custom_find_element(BL.BUY_BTN)
        return buy_button

    def get_quantity(self):
        element = self.custom_find_element(BL.BASKET_QUANTITY, 3)
        if not element:
            result = 0
        else:
            if len(element.text) > 0:
                result = int(element.text)
        return result

    def get_total_price(self):
        result = 0
        element = self.custom_find_element(BL.BASKET_TOTAL_PRICE, 5)
        if element:
            str = element.text.strip()
            if len(str) > 0:
                str = str.split(":")[1].strip()
                str = str.split(" ")
                result = int(str[0])
        return result

    def call(self):
        return self.custom_click_element(BL.BASKET, 3)

    def buy(self):
        return self.custom_click_element(BL.BUY_BTN, 3)

    def add_item(self):
        return self.custom_click_element(BL.BASKET_ADD_ITEM, 3)

    def remove_item(self):
        return self.custom_click_element(BL.BASKET_REMOVE_ITEM, 3)

    def close_item(self):
        return self.custom_click_element(BL.BASKET_CLOSE_ITEM, 3)

    def close(self):
        return self.custom_click_element(BL.BASKET_CLOSE, 3)
