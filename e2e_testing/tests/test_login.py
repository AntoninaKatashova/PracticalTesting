import pytest
from e2e_testing.pages.login_page import LoginPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = LoginPage(browser)
        m.user_login()
