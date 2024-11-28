from playwright.sync_api import Page

from ui.pages.base_page import BasePage


class AddAdminPage(BasePage):

    USERNAME_INPUT = "//input[@name='username']"

    def __init__(self, page: Page):
        super().__init__(page)


