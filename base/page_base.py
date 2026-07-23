import allure

from utils.ui_utils.wait_helper import WaitHelper


class PageBase(WaitHelper):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()
