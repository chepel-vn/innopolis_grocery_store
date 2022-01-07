import logging

from fixtures.models.search import SearchData

MSG_NO_FOUND = "Nothing here, see github"

logger = logging.getLogger("grocery_store")


class TestSearch:
    def test_search_some_exists_goods(self, app):
        """
        Check of situation with some exists goods
        """
        app.open_page()
        input_data = SearchData("apples")
        if app.searching.search(input_data):
            logger.info(f"Searching by '{input_data.search_string}'.")
        else:
            logger.info(f"Searching by '{input_data.search_string}' isn't done.")
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
        if app.searching.search(input_data):
            logger.info(f"Searching by '{input_data.search_string}'.")
        else:
            logger.info(f"Searching by '{input_data.search_string}' isn't done.")
        assert app.searching.is_empty_search()

    def test_add_to_basket_some_goods(self, app):
        """
        Check of situation with add to cart some goods
        """
        app.open_page()
        basket_quantity = app.basket.get_quantity()
        app.searching.buy_any_goods()
        basket_quantity_new = app.basket.get_quantity()
        assert basket_quantity_new == basket_quantity + 1

    def test_delete_from_basket_some_goods(self, app):
        """
        Check of situation with delete some goods from the basket
        """
        app.open_page()
        app.searching.buy_any_goods()
        basket_quantity = app.basket.get_quantity()
        basket_quantity_new = basket_quantity
        if app.basket.call():
            if app.basket.close_item():
                if app.basket.close():
                    basket_quantity_new = app.basket.get_quantity()

        assert basket_quantity == basket_quantity_new + 1

    def test_add_to_basket_the_same_goods(self, app):
        """
        Check of situation with add the same goods from the basket
        """
        app.open_page()
        if app.searching.buy_any_goods():
            total_price = 0
            total_price_new = 0
            if app.basket.call():
                total_price = app.basket.get_total_price()
                if total_price:
                    total_price_new = total_price
                    if app.basket.add_item():
                        total_price_new = app.basket.get_total_price()
        assert total_price_new == 2 * total_price

    def test_remove_from_basket_the_same_goods(self, app):
        """
        Check of situation with add the same goods from the basket
        """
        app.open_page()
        if app.searching.buy_any_goods():
            total_price = 0
            total_price_new = 0
            if app.basket.call():
                total_price = app.basket.get_total_price()
                if total_price:
                    total_price_new = total_price
                    if app.basket.add_item():
                        total_price_new = app.basket.get_total_price()
                        if total_price_new == 2 * total_price:
                            if app.basket.remove_item():
                                total_price_new = app.basket.get_total_price()
        logger.info(f"total_price_new='{total_price_new}; total_price={total_price}'.")
        assert total_price_new == total_price
