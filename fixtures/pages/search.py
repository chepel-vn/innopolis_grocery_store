import logging

from fixtures.models.search import SearchData
from fixtures.pages.base_page import BasePage
from fixtures.locators.search import SearchLocators as LC
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("grocery_store")


class SearchPage(BasePage):
    def _search_input(self) -> WebElement:
        element = self.custom_find_element(LC.SEARCH_STRING_INPUT)
        return element

    def _search_input_send_keys(self, send_str: str) -> WebElement:
        element = self.custom_sendkeys_to_element(LC.SEARCH_STRING_INPUT, send_str)
        return element

    def _search_button(self) -> WebElement:
        search_button = self.custom_find_element(LC.SEARCH_BTN)
        return search_button

    def _search_button_click(self) -> WebElement:
        search_button = self.custom_click_element(LC.SEARCH_BTN)
        return search_button

    def _buy_button(self) -> WebElement:
        buy_button = self.custom_find_element(LC.BUY_BTN)
        return buy_button

    def _buy_button_click(self) -> WebElement:
        buy_button = self.custom_click_element(LC.BUY_BTN)
        return buy_button

    def _prepare_button(self) -> WebElement:
        prepare_button = self.custom_find_element(LC.PREPARE_BTN, 1)
        return prepare_button

    def _prepare_button_click(self) -> WebElement:
        prepare_button = self.custom_click_element(LC.PREPARE_BTN, 1)
        return prepare_button

    def is_empty_search(self) -> WebElement:
        element = self.custom_find_element(LC.SEARCH_EMPTY)
        return element

    def buy_any_goods(self):
        result = False
        self._prepare_button_click()
        if self._buy_button_click():
            result = True
        return result

    def search(self, data: SearchData):
        result = False
        self._prepare_button_click()
        if self._buy_button():
            self._search_input_send_keys(data.search_string)
            self._search_button_click()
            result = True
        return result
