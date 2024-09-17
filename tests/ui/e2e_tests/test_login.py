import allure

from config.settings import BASE_URL
from ui.pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:
    @allure.title("Login valid user")
    def test_valid_user_login(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL)
        login_page.login("Admin", "admin123")

