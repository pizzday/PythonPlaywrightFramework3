import re

from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class EmployeeDetailsBasePage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def get_emp_number(self):
        match = re.search(r"/empNumber/(\d+)$", self.page.url)
        if match:
            return match.group(1)
        raise ValueError("Employee number not found in the URL")

