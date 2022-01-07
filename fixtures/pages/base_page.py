import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("grocery_store")


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=60):
        element = None
        try:
            element = WebDriverWait(self.app.driver, wait_time).until(
                EC.presence_of_element_located(locator),
                message=f"Can't find element by locator={locator}",
            )
        except TimeoutError:
            logger.warning(
                f"locator = '{locator}'. Выход из процедуры поиска элемента "
                f"по истечении времени ожидания."
            )
        finally:
            return element

    def custom_click_element(self, locator, wait_time=60):
        element = self.custom_find_element(locator, wait_time)
        if element:
            element.click()
        return element

    def custom_sendkeys_to_element(self, locator, send_str: str, wait_time=60):
        element = self.custom_find_element(locator, wait_time)
        if element:
            element.send_keys(send_str)
        return element
