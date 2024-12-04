import time

from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class AddEmployeePage(BasePage):

    ADD_IMAGE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button"
    FIRST_NAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input"
    MIDDLE_NAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input"
    LAST_NAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input"
    EMPLOYEE_ID_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    DETAILS_SWITCH = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span"
    USERNAME_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"
    ENABLED_STATUS_CHECKBOX = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/input"
    DISABLED_STATUS_CHECKBOX = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/input"
    PASSWORD1_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"
    PASSWORD2_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input"
    SAVE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def add_employee(self, create_details, first_name, middle_name, last_name, employee_id, username, password1, password2, status="Enabled", image_path=None):
        if image_path:
            self.set_input_files_for_dynamic_locator(self.ADD_IMAGE_BUTTON, image_path)

        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.MIDDLE_NAME_INPUT, middle_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.EMPLOYEE_ID_INPUT, employee_id)

        if create_details:
            self.click(self.DETAILS_SWITCH)
            self.fill(self.USERNAME_INPUT, username)
            if status is not "Enabled":
                self.click(self.DISABLED_STATUS_CHECKBOX)
            self.fill(self.PASSWORD1_INPUT, password1)
            self.fill(self.PASSWORD2_INPUT, password2)

        self.click(self.SAVE_BUTTON)

