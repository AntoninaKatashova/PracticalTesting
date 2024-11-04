from e2e_testing.pages.base import Base
from e2e_testing.Locators.login import Login
from e2e_testing.data.assertions import Assertions
from playwright.sync_api import Page

class LoginPage(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.assertion = Assertions(page)

    def user_login(self, username, password):
        self.open("")
        self.input(Login.USERNAME_INPUT, username)
        self.input(Login.PASSWORD_INPUT, password)
        self.click(Login.LOGIN_BTN)

    def check_error(self, error_message):
        self.assertion.contain_text(Login.ERROR_MESSAGE, error_message, "The error tests were successful")
