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

    def follow_to_cart(self):
        self.click(Market.FOLLOW_TO_CART)

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
        product_links = self.page.query_selector_all("div[class='inventory_item_label'] > a")
        urls = [link.get_attribute('href') for link in product_links]

        urls_with_id = []
        for index, url in enumerate(urls):
            url_index = index
            url = url.replace("#", "https://www.saucedemo.com/inventory-item.html")
            url = f"{url}?id={url_index}"
            urls_with_id.append(url)

        return urls_with_id

    def open_random_product(self):
        product_urls_list = self.get_list_of_product_urls()
        url_index = random.randrange(0, len(product_urls_list))
        product_url = product_urls_list[url_index]
        self.page.goto(product_url)

    def open_page_product(self, product_url):
        self.page.goto(product_url)

    def open_random_products(self, number_of_items):
        product_urls_list = self.get_list_of_product_urls()

        indexes = []
        products_url = []

        url_index = random.randrange(0, len(product_urls_list))
        indexes.append(url_index)
        products_url.append(product_urls_list[url_index])

        while True:
            url_index = random.randrange(0, len(product_urls_list))
            if not(url_index in indexes) and len(products_url) != number_of_items:
                products_url.append(product_urls_list[url_index])
                indexes.append(url_index)
            elif len(products_url) == number_of_items:
                break

        return products_url
