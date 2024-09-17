from playwright.sync_api import Page

from ui.pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_SUBMIT_BUTTON = "//button[@type='submit']"
    INVALID_CREDENTIALS_ERROR_TITLE = "//p[text()='Invalid credentials']"

    def __init__(self, page: Page):
        super().__init__(page)

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def is_invalid_credentials_title_presented(self):
        assert self.is_element_present(self.INVALID_CREDENTIALS_ERROR_TITLE)

