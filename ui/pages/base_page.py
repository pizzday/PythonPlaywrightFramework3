import allure
from playwright.sync_api import Page, expect
from playwright.sync_api import Error as PWError


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step('Click locator - {locator}')
    def click(self, locator: str):
        self.page.click(locator)

    @allure.step('Check checkbox locator - {locator}')
    def check(self, locator: str):
        self.page.check(locator)

    @allure.step('Uncheck checkbox locator - {locator}')
    def uncheck(self, locator: str):
        self.page.check(locator)

    @allure.step('Hover locator - {locator}')
    def hover(self, locator: str):
        self.page.hover(locator)

    @allure.step('Go to url - {url}')
    def go_to_url(self, url: str):
        self.page.goto(url)

    @allure.step('Type text - {text} into locator - {locator}')
    def fill(self, locator: str, text: str):
        self.click(locator)
        self.page.fill(locator, text)

    @allure.step('Select option - {option} in locator - {locator}')
    def select_option(self, locator: str, option: str):
        self.page.select_option(locator, option)

    @allure.step('Is element - {locator} present')
    def is_element_present(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator)
            return True
        except PWError:
            return False

    @allure.step('Is element - {locator} hidden')
    def is_element_hidden(self, locator: str) -> bool:
        try:
            self.page.wait_for_selector(locator, state='hidden')
            return True
        except PWError:
            return False

    @allure.step("Comparing URL")
    def compare_url_to(self, expected_url: str):
        expect(self.page).to_have_url(expected_url)


