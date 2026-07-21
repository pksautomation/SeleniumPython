import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class WaitHelper:
    DEFAULT_TIMEOUT = 10
    FLUENT_POLL_FREQUENCY = 1
    FLUENT_IGNORED_EXCEPTIONS = (NoSuchElementException,)

    # ---- Explicit wait: fixed timeout, Selenium's default 0.5s polling ----

    @allure.step("Waiting for element to be visible")
    def wait_for_visible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Waiting for element to be clickable")
    def wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Waiting for element to be present in DOM")
    def wait_for_present(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Waiting for element to become invisible")
    def wait_for_invisible(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    # ---- Fluent wait: configurable poll interval + ignored exceptions ----

    @allure.step("Fluent waiting for element to be visible")
    def fluent_wait_for_visible(self, locator, timeout=DEFAULT_TIMEOUT,
                                 poll_frequency=FLUENT_POLL_FREQUENCY,
                                 ignored_exceptions=FLUENT_IGNORED_EXCEPTIONS):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                              ignored_exceptions=ignored_exceptions).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Fluent waiting for element to be clickable")
    def fluent_wait_for_clickable(self, locator, timeout=DEFAULT_TIMEOUT,
                                   poll_frequency=FLUENT_POLL_FREQUENCY,
                                   ignored_exceptions=FLUENT_IGNORED_EXCEPTIONS):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                              ignored_exceptions=ignored_exceptions).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Fluent waiting for element to be present in DOM")
    def fluent_wait_for_present(self, locator, timeout=DEFAULT_TIMEOUT,
                                 poll_frequency=FLUENT_POLL_FREQUENCY,
                                 ignored_exceptions=FLUENT_IGNORED_EXCEPTIONS):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                              ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Fluent waiting for element to become invisible")
    def fluent_wait_for_invisible(self, locator, timeout=DEFAULT_TIMEOUT,
                                   poll_frequency=FLUENT_POLL_FREQUENCY,
                                   ignored_exceptions=FLUENT_IGNORED_EXCEPTIONS):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                              ignored_exceptions=ignored_exceptions).until(
            EC.invisibility_of_element_located(locator)
        )
