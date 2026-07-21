import allure
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from base.page_base import PageBase
from locators.locators import LoginFlowLocators


class LogingApp(PageBase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Login Page")
    def Login(self):
        self.driver.get(self.login_link)
        # Fluent wait: polls every 1s (instead of the 0.5s default) for up to 10s,
        # and keeps retrying through the two exceptions instead of failing on the first miss.
        self.fluent_wait_for_clickable(
            LoginFlowLocators.loginbutton,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=(NoSuchElementException, ElementClickInterceptedException),
        ).click()