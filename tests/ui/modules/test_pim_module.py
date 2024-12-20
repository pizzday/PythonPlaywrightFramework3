import re
import time

import allure
import pytest

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
        add_employee_page.add_employee(
            FIRST_NAME,
            MIDDLE_NAME,
            LAST_NAME,
            EMPLOYEE_ID,
            TEST_IMAGE_PATH,
            True,
            USERNAME,
            PASSWORD,
            PASSWORD,
            "Enabled"
        )
        add_employee_page.compare_url_to(re.compile(
            r"https://opensource-demo\.orangehrmlive\.com/web/index\.php/pim/viewPersonalDetails/empNumber/.*"))
        try:
            pim_module_page = PimModulePage(page)
            pim_module_page.left_navbar.visit_pim_module()
            pim_module_page.search_employee_by_id(EMPLOYEE_ID)
        finally:
            pim_module_page.delete_user_after_searching()

    @pytest.mark.parametrize("""first_name, middle_name, last_name, employee_id, image_path, create_details,
            username, password1, password2, status""",
                             [("", "", "", "", "", "", "", "", "", ""),
                              (FIRST_NAME, "", "", "", "", "", "", "", "", ""),
                              ("", MIDDLE_NAME, "", EMPLOYEE_ID, "", "", "", "", "", ""),
                              (FIRST_NAME, "", LAST_NAME, EMPLOYEE_ID, "", "", "", "", "", "")
                              ])
    @allure.title("Create employee with empty fields")
    def test_create_employee_empty_fields(self, page, admin_login, first_name, middle_name, last_name, employee_id,
                                          image_path, create_details, username, password1, password2, status):
        pim_module_page = PimModulePage(page)
        pim_module_page.left_navbar.visit_pim_module()
        pim_module_page.click_add_employee_button()
        add_employee_page = AddEmployeePage(page)
        add_employee_page.add_employee(first_name,
                                       middle_name,
                                       last_name,
                                       employee_id,
                                       image_path,
                                       create_details,
                                       username,
                                       password1,
                                       password2,
                                       status)

        assert add_employee_page.is_element_present(add_employee_page.INPUT_ERROR_TITLES)
        add_employee_page.compare_url_to("https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee")
