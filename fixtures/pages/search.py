import logging

from fixtures.models.search import SearchData
from fixtures.pages.base_page import BasePage
from fixtures.locators.search import SearchLocators as LC
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger(__name__)


class SearchPage(BasePage):
    def _search_input(self) -> WebElement:
        element = self.custom_find_element(LC.SEARCH_STRING_INPUT)
        return element

    def _search_button(self) -> WebElement:
        submit_button = self.custom_find_element(LC.SEARCH_BTN)
        return submit_button

    def _buy_button(self) -> WebElement:
        buy_button = self.custom_find_element(LC.BUY_BTN)
        return buy_button

    def _prepare_button(self) -> WebElement:
        buy_button = self.custom_find_element(LC.PREPARE_BTN, 0.5)
        return buy_button

    def is_empty_search(self) -> WebElement:
        element = self.custom_find_element(LC.SEARCH_EMPTY)
        return type(element) == WebElement

    def is_get_ready_to_buy(self) -> WebElement:
        result = False
        try:
            result = type(self._buy_button()) == WebElement
        except TimeoutError:
            logger.warning(
                "Выход из процедуры проверки готовности к "
                "покупке по истечении времени ожидания."
            )
        finally:
            return result

    def is_get_ready_to_test(self) -> WebElement:
        result = False
        try:
            result = type(self._prepare_button()) != WebElement
        except TimeoutError:
            logger.warning(
                "Выход из процедуры проверки готовности к "
                "проведению теста по истечении времени ожидания."
            )
        finally:
            return result

    def buy_any_goods(self):
        if self.is_get_ready_to_buy():
            self._buy_button().click()

    def search(self, data: SearchData):
        result = 1
        try:
            if not self.is_get_ready_to_test():
                self._prepare_button().click()
            if self.is_get_ready_to_buy():
                self._search_input().send_keys(data.search_string)
                self._search_button().click()
        except TimeoutError:
            logger.warning(
                "Выход из процедуры поиска произошел так как истекло время ожидания."
            )
        else:
            result = 0
        finally:
            return result
