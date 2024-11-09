import pytest
from e2e_testing.pages.login_page import LoginPage
from e2e_testing.data.constants import Constants


@pytest.fixture(scope='function')
def user_auth(browser):
    p = LoginPage(browser)
    p.user_login(Constants.login, Constants.password)
