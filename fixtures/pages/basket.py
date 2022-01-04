import logging

from fixtures.pages.base_page import BasePage
from fixtures.locators.basket import BasketLocators as BL
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)


class BasketPage(BasePage):
    def _buy_button(self) -> WebElement:
        buy_button = self.custom_find_element(BL.BUY_BTN)
        return buy_button

    def get_cart_quantity(self):
        element = self.custom_find_element(BL.BASKET_QUANTITY, 3)
        if not element:
            result = 0
        else:
            if len(element.text) > 0:
                result = int(element.text)
        return result

    def call(self):
        try:
            element = self.custom_find_element(BL.CART, 3)
            if element:
                element.click()
        except Exception:
            result = 1
        else:
            result = 0
        finally:
            return result

    def buy(self):
        try:
            element = self.custom_find_element(BL.BUY_BTN, 3)
            if element:
                element.click()
        except Exception:
            result = 1
        else:
            result = 0
        finally:
            return result
