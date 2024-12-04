import time

from playwright.sync_api import Page

from ui.components.left_navbar import LeftNavbar
from ui.pages.base_page import BasePage


class PimModulePage(BasePage):

    ADD_EMPLOYEE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    EMPLOYEE_ID_INPUT = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
    SEARCH_EMPLOYEE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    RECORDS_TABLE_CARD_LOCATOR = "//div[@class='oxd-table-card']"
    CARD_ID_TITLE = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div"
    CARD_DELETE_BUTTON = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]"
    CARD_DELETE_CONFIRMATION_BUTTON = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"
    DELETING_SUCCESS_TITLE = "//p[@data-v-7b563373]/text()[. ='Successfully Deleted']"
    EMPLOYEE_INFORMATION_CARET = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button/i"

    def __init__(self, page: Page):
        super().__init__(page)
        self.left_navbar = LeftNavbar(page)

    def check_that_record_is_single(self):
        records = self.find_all_elements_with_locator(self.RECORDS_TABLE_CARD_LOCATOR)
        assert len(records) == 1

    def click_add_employee_button(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def search_employee_by_id(self, employee_id):
        self.fill(self.EMPLOYEE_ID_INPUT, employee_id)
        self.click(self.SEARCH_EMPLOYEE_BUTTON)
        time.sleep(1.5)
        self.check_that_record_is_single()
        self.should_have_text(self.CARD_ID_TITLE, employee_id)

    def delete_user_found_by_id(self):
        self.check_that_record_is_single()
        self.click(self.CARD_DELETE_BUTTON)
        self.click(self.CARD_DELETE_CONFIRMATION_BUTTON)
        self.is_element_present(self.DELETING_SUCCESS_TITLE)



