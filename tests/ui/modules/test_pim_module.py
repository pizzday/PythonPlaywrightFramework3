import re

import allure

from config.settings import EMPLOYEE_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, USERNAME, PASSWORD, TEST_IMAGE_PATH
from ui.pages.pim_module.add_employee_page import AddEmployeePage
from ui.pages.pim_module.pim_module_page import PimModulePage


@allure.feature("Login")
class TestPimModule:
    @allure.title("Create valid employee")
    def test_create_valid_employee(self, page, admin_login):
        pim_module_page = PimModulePage(page)
        pim_module_page.left_navbar.visit_pim_module()
        pim_module_page.click_add_employee_button()

        add_employee_page = AddEmployeePage(page)
        employee_data = {
            "first_name": "John",
            "middle_name": "A.",
            "last_name": "Doe",
            "employee_id": "12345",
            "create_details": True,
            "username": "johndoe",
            "password1": "securePassword",
            "password2": "securePassword",
            "status": "Enabled",
            "image_path": "/path/to/image.jpg",
        }

        add_employee_page.add_employee(True, FIRST_NAME, MIDDLE_NAME, LAST_NAME, EMPLOYEE_ID, USERNAME, PASSWORD, PASSWORD, image_path=TEST_IMAGE_PATH)


        add_employee_page.compare_url_to(re.compile(
            r"https://opensource-demo\.orangehrmlive\.com/web/index\.php/pim/viewPersonalDetails/empNumber/.*"))
        try:
            pim_module_page = PimModulePage(page)
            pim_module_page.left_navbar.visit_pim_module()
            pim_module_page.search_employee_by_id(EMPLOYEE_ID)
        finally:
            pim_module_page.delete_user_found_by_id()


