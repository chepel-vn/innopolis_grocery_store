from fixtures.pages.basket import BasketPage
from fixtures.pages.search import SearchPage


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.searching = SearchPage(self)
        self.basket = BasketPage(self)

    def quit(self):
        self.driver.quit()

    def open_page(self):
        self.driver.get(self.url)
