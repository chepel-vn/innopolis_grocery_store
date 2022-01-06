from fixtures.consts.search import SearchConsts as SC
from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_STRING_INPUT = (By.ID, "email_inline")
    SEARCH_BTN = (By.CLASS_NAME, "btn.search-btn")
    BUY_BTN = (By.XPATH, ".//button[text() = 'Buy']")
    SEARCH_EMPTY = (By.XPATH, f"//h3[text() = '{SC.SEARCH_IS_EMPTY}']")
    PREPARE_BTN = (By.XPATH, ".//button[text() = 'Prepere data']")
