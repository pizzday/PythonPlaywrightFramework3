import time

import allure

from config.settings import FIRST_NAME, USERNAME, PASSWORD
from ui.pages.admin_module.add_admin_page import AddAdminPage
from ui.pages.admin_module.admin_module_page import AdminModulePage


@allure.feature("Login")
class TestAdminModule:
    @allure.title("Add valid admin")
    def test_add_valid_admin(self, page, admin_login, created_test_user_notadmin):
        admin_module_page = AdminModulePage(page)
        admin_module_page.left_navbar.visit_admin_module()
        admin_module_page.click_add_admin_button()

        add_admin_page = AddAdminPage(page)
        add_admin_page.add_user("Admin", "Enabled", FIRST_NAME, USERNAME, PASSWORD, PASSWORD)




