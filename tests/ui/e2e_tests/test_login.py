import allure

from config.settings import BASE_URL, LOGIN_URL
from ui.pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:
    @allure.title("Login valid user")
    def test_valid_user_login(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(LOGIN_URL)
        login_page.login("Admin", "admin123")
        login_page.compare_url_to(BASE_URL + "/dashboard/index")

    @allure.title("Login user with invalid password")
    def test_invalid_password_login(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(LOGIN_URL)
        login_page.login("Admin", "123")
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()

    @allure.title("Login user with invalid username")
    def test_invalid_username_login(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL+"/auth/login")
        login_page.login("123", "admin123")
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()

    @allure.title("panosik")
    def test_panosik_fail(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL+"/auth/login")
        login_page.login("123", "admin123")
        assert 1 == 2
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()


