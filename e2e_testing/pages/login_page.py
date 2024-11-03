from e2e_testing.pages.base import Base
from e2e_testing.data.constants import Constants
from e2e_testing.Locators.login import Login
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page

class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self):
        self.open("")
        self.input(Login.USERNAME_INPUT, Constants.login)
        self.input(Login.PASSWORD_INPUT, Constants.password)
        self.click(Login.LOGIN_BTN)
        self.assertion.check_URL('inventory.html', "Wrong URL")
