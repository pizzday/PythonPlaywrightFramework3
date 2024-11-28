import time

import allure

from config.settings import BASE_URL, LOGIN_URL
from ui.pages.admin_module_page import AdminModulePage
from ui.pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:
    @allure.title("Add valid admin")
    def test_add_valid_admin(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(LOGIN_URL)
        login_page.login("Admin", "admin123")
        login_page.compare_url_to(BASE_URL + "/dashboard/index")

        admin_module_page = AdminModulePage(page)
        admin_module_page.left_navbar.click_admin_module_link()
        admin_module_page.click_add_admin_button()


        time.sleep(123132)


