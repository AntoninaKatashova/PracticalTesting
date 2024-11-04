import pytest
from e2e_testing.pages.market_page import MarketPage

@pytest.mark.regression
@pytest.mark.usefixtures('user_auth')
class TestBuyProduct:
    def test_buy_product(self, browser):
        p = MarketPage(browser)
        p.add_to_cart()
        p.checkout()
