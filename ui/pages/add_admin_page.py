import time

from playwright.sync_api import Page

from ui.pages.base_page import BasePage


class AddAdminPage(BasePage):

    USER_ROLE_DROPDOWN = "//div[@data-v-c93bdbf3][@class='oxd-grid-item oxd-grid-item--gutters'][1]//div[@class='oxd-select-text oxd-select-text--active']"
    USER_ROLE = lambda self, user_role: f"//span[@data-v-13cf171c][text()='{user_role}']"
    USER_STATUS_DROPDOWN = "//div[@data-v-c93bdbf3][@class='oxd-grid-item oxd-grid-item--gutters'][3]//div[@class='oxd-select-text oxd-select-text--active']"
    USER_STATUS = lambda self, user_status: f"//span[@data-v-13cf171c][text()='{user_status}']"
    EMPLOYEE_NAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input"
    EMPLOYEE_NAME_OPTION = lambda self, employee_name: f"//span[contains(text(),'{employee_name}')]"
    USERNAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"
    PASSWORD1_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"
    PASSWORD2_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"
    SAVE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]"

    def __init__(self, page: Page):
        super().__init__(page)

    def add_user(self, user_role, user_status, employee_name, username, password1, password2):
        self.click(self.USER_ROLE_DROPDOWN)
        self.click(self.USER_ROLE(user_role))

        self.click(self.USER_STATUS_DROPDOWN)
        self.click(self.USER_STATUS(user_status))

        self.fill(self.USERNAME_INPUT, username)

        self.fill(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.click(self.EMPLOYEE_NAME_OPTION(employee_name))

        self.fill(self.PASSWORD1_INPUT, password1)
        self.fill(self.PASSWORD2_INPUT, password2)

        self.click(self.SAVE_BUTTON)
