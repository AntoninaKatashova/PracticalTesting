import pytest
from e2e_testing.pages.market_page import MarketPage
from e2e_testing.pages.product_page import ProductPage
from e2e_testing.pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestAddSingleItem:
    def test_add_single_product(self, browser):
        p = MarketPage(browser)
        p.open_random_product()

        p = ProductPage(browser)

        actual_name = []
        actual_name.append(p.get_name())

        actual_price = []
        actual_price.append(p.get_price())

        p.click_add_product_to_cart()
        p.follow_to_cart()

        p = CartPage(browser)

        p.get_item_count(1)
        p.get_list_of_cart_item_names(actual_name)
        p.get_list_of_cart_item_prices(actual_price)
