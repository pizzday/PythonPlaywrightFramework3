from playwright.sync_api import Page

from ui.pages.base_page import BasePage


class LeftNavbar(BasePage):

    HOME_PAGE_LINK = "//a[@class='oxd-brand']"
    ADMIN_MODULE_LINK = "//a[@href='/web/index.php/admin/viewAdminModule']"
    PIM_MODULE_LINK = "//a[@href='/web/index.php/pim/viewPimModule']"

    def __init__(self, page: Page):
        super().__init__(page)

    def visit_home_page(self):
        self.click(self.HOME_PAGE_LINK)

    def visit_admin_module(self):
        self.click(self.ADMIN_MODULE_LINK)
        self.compare_url_to("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

    def visit_pim_module(self):
        self.click(self.PIM_MODULE_LINK)
        self.compare_url_to("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

