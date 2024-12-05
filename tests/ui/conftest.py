import os
import re
import time

import allure
import pytest
from playwright.sync_api import sync_playwright

from config.settings import *
from ui.pages.pim_module.add_employee_page import AddEmployeePage
from ui.pages.login_page import LoginPage
from ui.pages.pim_module.pim_module_page import PimModulePage


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as play:
        if os.getenv('DOCKER_CONTAINER') or os.getenv('GITHUB_RUN'):
            browser = play.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = play.chromium.launch(headless=False, slow_mo=500)

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


@pytest.fixture(scope="function")
def created_test_user_admin(page):
    add_employee_page = AddEmployeePage(page)
    add_employee_page.go_to_url(PIM_ADD_EMPLOYEE_URL)
    add_employee_page.add_employee(FIRST_NAME,
                                   MIDDLE_NAME,
                                   LAST_NAME,
                                   EMPLOYEE_ID,
                                   TEST_IMAGE_PATH,
                                   True,
                                   USERNAME,
                                   PASSWORD,
                                   PASSWORD,
                                   "Enabled")
    add_employee_page.compare_url_to(re.compile(
        r"https://opensource-demo\.orangehrmlive\.com/web/index\.php/pim/viewPersonalDetails/empNumber/.*"))
    yield
    pim_module_page = PimModulePage(page)
    pim_module_page.left_navbar.visit_pim_module()
    pim_module_page.search_employee_by_id(EMPLOYEE_ID)
    pim_module_page.delete_user_after_searching()


@pytest.fixture(scope="function")
def created_test_user_notadmin(page):

    add_employee_page = AddEmployeePage(page)
    add_employee_page.go_to_url(PIM_ADD_EMPLOYEE_URL)
    add_employee_page.add_employee(FIRST_NAME,
                                   MIDDLE_NAME,
                                   LAST_NAME,
                                   EMPLOYEE_ID,
                                   TEST_IMAGE_PATH)
    add_employee_page.compare_url_to(re.compile(
        r"https://opensource-demo\.orangehrmlive\.com/web/index\.php/pim/viewPersonalDetails/empNumber/.*"))
    yield
    pim_module_page = PimModulePage(page)
    pim_module_page.go_to_url(PIM_EMPLOYEE_LIST_URL)
    pim_module_page.search_employee_by_id(EMPLOYEE_ID)
    pim_module_page.delete_user_after_searching()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            allure.attach(page.screenshot(), name=f"failure_{item.name}", attachment_type=allure.attachment_type.PNG)
