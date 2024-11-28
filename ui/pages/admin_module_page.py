from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class AdminModulePage(BasePage):

    ADD_ADMIN_BUTTON = "//div[@class='orangehrm-header-container']/button"

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def click_add_admin_button(self):
        self.click(self.ADD_ADMIN_BUTTON)





