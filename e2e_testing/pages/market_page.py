import random
from e2e_testing.pages.base import Base
from e2e_testing.Locators.cart import Cart
from e2e_testing.Locators.market import Market
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

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


    def get_list_of_product_urls(self):
        product_urls_list = []
        product_links = self.page.query_selector_all("div[class='inventory_item_label'] > a")
        urls = [link.get_attribute('href') for link in product_links]

        urls_with_id = []
        for url in urls:
            url_index = random.randrange(0, len(urls))
            url = url.replace("#", "https://www.saucedemo.com/inventory-item.html")
            url = f"{url}?id={url_index}"
            urls_with_id.append(url)

        return urls_with_id

    def open_random_product(self):
        product_urls_list = self.get_list_of_product_urls()
        url_index = random.randrange(0, len(product_urls_list))
        product_url = product_urls_list[url_index]
        self.page.goto(product_url)


    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0)
        self.click(Market.FOLLOW_TO_CART)

    def checkout(self):
        self.click(Cart.CHECKOUT_BTN)
        self.input(Cart.FIRST_NAME, "Ivan")
        self.input(Cart.LAST_NAME, "Ivanov")
        self.input(Cart.ZIP, "123456")
        self.click(Cart.CNT_BTN)
        self.click(Cart.FINISH_BTN)
        self.assertions.have_text(Cart.FINAL_TEXT, "Checkout: Complete!", "no")
