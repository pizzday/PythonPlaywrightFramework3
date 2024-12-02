import time

import allure

from config.settings import FIRST_NAME, MIDDLE_NAME, LAST_NAME, EMPLOYEE_ID, USERNAME, PASSWORD, TEST_IMAGE_PATH
from ui.pages.add_admin_page import AddAdminPage
from ui.pages.add_employee_page import AddEmployeePage
from ui.pages.pim_module_page import PimModulePage


@allure.feature("Login")
class TestPimModule:
    @allure.title("Create valid employee")
    def test_create_valid_employee(self, page, admin_login):

        pim_module_page = PimModulePage(page)
        pim_module_page.left_navbar.click_pim_module_link()
        pim_module_page.click_add_employee_button()

        add_employee_page = AddEmployeePage(page)
        add_employee_page.add_employee(True, FIRST_NAME, MIDDLE_NAME, LAST_NAME, EMPLOYEE_ID, USERNAME, PASSWORD, PASSWORD, image_path=TEST_IMAGE_PATH)


        time.sleep(3)


