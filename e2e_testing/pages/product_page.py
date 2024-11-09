from e2e_testing.pages.base import Base
from e2e_testing.Locators.product import Product
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page


class ProductPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def get_name(self) -> str:
        return self.get_text(Product.PRODUCT_NAME, 0)

    def get_price(self) -> float:
        product_price = self.get_text(Product.PRODUCT_PRICE, 0)
        return float(product_price.replace("$", ""))

    def click_add_product_to_cart(self):
        self.click(Product.ADD_TO_CART)

    def follow_to_cart(self):
        self.click(Product.FOLLOW_TO_CART)

    def back_to_products(self):
        self.click(Product.BACK_TO_PRODUCTS)
