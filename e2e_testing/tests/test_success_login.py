import pytest

from e2e_testing.data.assertions import Assertions



@pytest.mark.regression
class TestSuccessLogin:
    @pytest.mark.usefixtures('user_auth')
    def test_user_login_success(self, browser):
        self.assertion = Assertions(browser)

        self.assertion.check_URL("inventory.html", "Wrong URL")