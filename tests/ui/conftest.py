import os
import re
import time

import allure
import pytest
from playwright.sync_api import sync_playwright

from config.settings import LOGIN_URL, BASE_URL, DEFAULT_TIMEOUT, ADMIN_USERNAME, ADMIN_PASSWORD, FIRST_NAME, \
    MIDDLE_NAME, LAST_NAME, EMPLOYEE_ID, USERNAME, PASSWORD, TEST_IMAGE_PATH
from ui.pages.pim_module.add_employee_page import AddEmployeePage
from ui.pages.login_page import LoginPage
from ui.pages.pim_module.pim_module_page import PimModulePage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as play:
        if os.getenv('DOCKER_CONTAINER') or os.getenv('GITHUB_RUN'):
            browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = play.chromium.launch(headless=False)

        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.set_default_timeout(DEFAULT_TIMEOUT)
    yield page
    context.close()


@pytest.fixture(scope="function")
def admin_login(page):
    login_page = LoginPage(page)
    login_page.go_to_url(LOGIN_URL)
    login_page.login(ADMIN_USERNAME, ADMIN_PASSWORD)
    login_page.compare_url_to(BASE_URL + "/dashboard/index")


# def created_test_user()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            allure.attach(page.screenshot(), name=f"failure_{item.name}", attachment_type=allure.attachment_type.PNG)
