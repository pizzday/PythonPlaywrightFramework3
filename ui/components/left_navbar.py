from playwright.sync_api import Page

from ui.pages.base_page import BasePage


class LeftNavbar(BasePage):

    HOME_PAGE_LINK = "//a[@class='oxd-brand']"
    ADMIN_MODULE_LINK = "//a[@href='/web/index.php/admin/viewAdminModule']"
    PIM_MODULE_LINK = "//a[@href='/web/index.php/pim/viewPimModule']"

    def __init__(self, page: Page):
        super().__init__(page)

    def click_home_page_link(self):
        self.click(self.HOME_PAGE_LINK)

    def click_admin_module_link(self):
        self.click(self.ADMIN_MODULE_LINK)

    def click_pim_module_link(self):
        self.click(self.PIM_MODULE_LINK)

