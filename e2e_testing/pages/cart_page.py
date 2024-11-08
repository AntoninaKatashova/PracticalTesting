from e2e_testing.pages.base import Base
from e2e_testing.Locators.cart import Cart
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page


class CartPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def get_item_count(self, expected: int):
        cart_items = self.page.query_selector_all(Cart.CART_ITEM)
        self.assertions.check_equals(len(cart_items), expected, "The shopping cart does not contain a product")

    def get_list_of_cart_item_names(self, expected: list[str]):
        item_names = self.page.query_selector_all(Cart.CART_ITEM_NAME)
        self.assertions.check_equals([str(name.text_content()) for name in item_names], expected,"The item name in cart does not match to name from product page")


    def get_list_of_cart_item_prices(self, expected: list[float]):
        item_prices = self.page.query_selector_all(Cart.CART_ITEM_PRICE)
        self.assertions.check_equals([float(price.text_content().replace("$", "")) for price in item_prices], expected,"The product price does not match to product price from inventory page")
