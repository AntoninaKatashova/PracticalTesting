from e2e_testing.pages.base import Base
from e2e_testing.Locators.basket import Basket
from e2e_testing.Locators.market import Market
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0)
        self.click(Market.FOLLOW_TO_BASKET)

    def sortByLoHi(self):
        self.selector(Market.PRODUCT_SORTED, "lohi")
        items = self.wait_for_all_elements(Market.PRODUCT_PRICE)
        prices = [item.text_content() for item in items]

        sorts = sorted(prices, key=lambda x: float(x[1:]))
        assert prices == sorts

    def sortByHiLo(self):
        self.selector(Market.PRODUCT_SORTED, "hilo")
        items = self.wait_for_all_elements(Market.PRODUCT_PRICE)
        prices = [item.text_content() for item in items]

        reverse = sorted(prices, key=lambda x: float(x[1:]), reverse=True)
        assert prices == reverse

    def sortByAZ(self):
        self.selector(Market.PRODUCT_SORTED, "az")
        items = self.wait_for_all_elements(Market.PRODUCT_NAME)
        names = [item.text_content() for item in items]

        sorts = sorted(names)
        assert names == sorts

    def sortByZA(self):
        self.selector(Market.PRODUCT_SORTED, "za")
        items = self.wait_for_all_elements(Market.PRODUCT_NAME)
        names = [item.text_content() for item in items]

        reverse = sorted(names, reverse=True)
        assert names == reverse


    def checkout(self):
        self.click(Basket.CHECKOUT_BTN)
        self.input(Basket.FIRST_NAME, "Ivan")
        self.input(Basket.LAST_NAME, "Ivanov")
        self.input(Basket.ZIP, "123456")
        self.click(Basket.CNT_BTN)
        self.click(Basket.FINISH_BTN)
        self.assertions.have_text(Basket.FINAL_TEXT, "Checkout: Complete!", "no")
