from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class DashboardModulePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)





