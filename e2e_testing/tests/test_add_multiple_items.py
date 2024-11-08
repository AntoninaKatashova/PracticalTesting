import pytest
from e2e_testing.pages.market_page import MarketPage
from e2e_testing.pages.product_page import ProductPage
from e2e_testing.pages.cart_page import CartPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestAddMultipleItems:
    def test_add_multiple_products(self, browser):
        p = MarketPage(browser)

        number_of_items = 3
        actual_name = []
        actual_price = []

        product_urls = p.open_random_products(number_of_items)

        for url in product_urls:
            p.open_page_product(url)

            p = ProductPage(browser)

            actual_name.append(p.get_name())
            actual_price.append(p.get_price())

            p.click_add_product_to_cart()
            p.back_to_products()

            p = MarketPage(browser)

        p.follow_to_cart()

        p = CartPage(browser)

        p.get_item_count(number_of_items)
        p.get_list_of_cart_item_names(actual_name)
        p.get_list_of_cart_item_prices(actual_price)