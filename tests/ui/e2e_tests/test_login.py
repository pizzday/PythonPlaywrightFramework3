import allure
import pytest

from config.settings import BASE_URL, LOGIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD
from ui.pages.login_page import LoginPage


@allure.feature("Login")
class TestLogin:
    @allure.title("Login valid user")
    def test_valid_user_login(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(LOGIN_URL)
        login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
        login_page.compare_url_to(BASE_URL + "/dashboard/index")

    @pytest.mark.parametrize(
        "username, password",
        [
            ("InvalidUsername", ADMIN_PASSWORD),
            (ADMIN_USERNAME, "InvalidPassword")
        ]
    )
    @allure.title("Login user with invalid credentials")
    def test_invalid_credentials(self, page, username, password):
        login_page = LoginPage(page)
        login_page.go_to_url(LOGIN_URL)
        login_page.login(username, password)
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()

    @allure.title("panosik")
    def test_panosik_fail(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL + "/auth/login")
        login_page.login("123", ADMIN_PASSWORD)
        assert 1 == 2
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()
        print("main branch")
        print("test-feature branch")

    @allure.title("Demo test")
    def test_demo(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL + "/auth/login")
        login_page.login("123", ADMIN_PASSWORD)
        login_page.compare_url_to(LOGIN_URL)
        login_page.is_invalid_credentials_title_presented()

    @allure.title("Demo test 02")
    def test_demo_02(self, page):
        login_page = LoginPage(page)
        login_page.go_to_url(BASE_URL + "/auth/login")
        login_page.login("123", ADMIN_PASSWORD)
        login_page.compare_url_to(LOGIN_URL)
