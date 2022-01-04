import logging

from fixtures.models.search import SearchData

MSG_NO_FOUND = "Nothing here, see github"

logger = logging.getLogger(__name__)


class TestSearch:
    def test_search_some_exists_goods(self, app):
        """
        Check of situation with some exists goods
        """
        app.open_page()
        input_data = SearchData("apples")
        result = app.searching.search(input_data)
        if result == 0:
            logger.info(f"Searching by '{input_data.search_string}'.")
        assert (
            "Delicious red apples" in app.driver.page_source
            and "Russian potatoes" not in app.driver.page_source
        )

    def test_search_not_exists_goods(self, app):
        """
        Check of situation with not exists goods
        """
        app.open_page()
        input_data = SearchData().random()
        result = app.searching.search(input_data)
        is_empty = False
        if result == 0:
            logger.info(f"Searching by '{input_data.search_string}'.")
            is_empty = app.searching.is_empty_search()
        assert is_empty

    def test_add_to_cart_some_goods(self, app):
        """
        Check of situation with add to cart some goods
        """
        app.open_page()
        cart_quantity = app.basket.get_cart_quantity()
        app.searching.buy_any_goods()
        cart_quantity_new = app.basket.get_cart_quantity()
        assert cart_quantity_new == cart_quantity + 1

    def test_delete_from_cart_some_goods(self, app):
        """
        Check of situation with add to cart some goods
        """
        app.open_page()
        result = app.basket.call()
        assert result == 0
