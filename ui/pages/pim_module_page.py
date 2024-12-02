
from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class PimModulePage(BasePage):

    ADD_EMPLOYEE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def click_add_employee_button(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

