import pytest
from e2e_testing.pages.login_page import LoginPage


@pytest.fixture(scope='class')
def user_login(browser):
    m = LoginPage(browser)
    m.user_login()
