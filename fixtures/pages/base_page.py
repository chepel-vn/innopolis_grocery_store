import logging

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

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
            logger.warning(f"Выход из процедуры поиска элемента по истечении времени ожидания.")
        finally:
            return element



