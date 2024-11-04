import pytest

from e2e_testing.pages.login_page import LoginPage
from e2e_testing.test_values.authorization_data import tests_with_incorrect_data



@pytest.mark.regression
class TestIncorrectLogin:
    @pytest.mark.parametrize("username, password, error_message", tests_with_incorrect_data)
    def test_user_incorrect_login(self, browser, username, password, error_message):
        m = LoginPage(browser)
        m.user_login(username, password)

        m.check_error(error_message)