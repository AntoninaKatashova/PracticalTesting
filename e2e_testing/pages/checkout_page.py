from e2e_testing.pages.base import Base
from e2e_testing.Locators.checkout import Checkout
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def checkout(self, first_name, last_name, _zip, text, message):
        self.input(Checkout.FIRST_NAME, first_name)
        self.input(Checkout.LAST_NAME, last_name)
        self.input(Checkout.ZIP, _zip)
        self.click(Checkout.CNT_BTN)
        self.click(Checkout.FINISH_BTN)
        self.assertions.have_text(Checkout.FINAL_TEXT, text, message)