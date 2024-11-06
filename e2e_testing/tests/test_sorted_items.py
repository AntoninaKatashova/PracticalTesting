import pytest

from e2e_testing.pages.market_page import MarketPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestSortedItems:
    def test_sorted_lohi(self, browser):
        p = MarketPage(browser)
        p.sortByLoHi()

    def test_sorted_hilo(self, browser):
        p = MarketPage(browser)
        p.sortByHiLo()

    def test_sorted_az(self, browser):
        p = MarketPage(browser)
        p.sortByAZ()

    def test_sorted_za(self, browser):
        p = MarketPage(browser)
        p.sortByZA()