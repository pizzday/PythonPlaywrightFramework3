from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.pim_module.employee_details.employee_details_base_page import EmployeeDetailsBasePage


class PersonalDetailsPage(EmployeeDetailsBasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)
