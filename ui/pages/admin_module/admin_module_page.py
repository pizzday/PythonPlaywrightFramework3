from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class AdminModulePage(BasePage):

    ADD_ADMIN_BUTTON = "//div[@class='orangehrm-header-container']/button"
    USERNAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input"
    SEARCH_BUTTON = "//button[@data-v-10d463b7][text()=' Search ']"
    RECORDS_AMOUNT_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span"

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def click_add_admin_button(self):
        self.click(self.ADD_ADMIN_BUTTON)

    def search_user_by_username(self, username):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.click(self.SEARCH_BUTTON)
        self.should_have_text(self.RECORDS_AMOUNT_TITLE, "(1) Record Found")





