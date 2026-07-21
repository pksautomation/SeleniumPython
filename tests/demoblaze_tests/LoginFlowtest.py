import allure
import pytest

from pages.phptravels import LoginApp
from pages.phptravels.LoginApp import LogingApp

@pytest.mark.usefixtures("setup")
class LoginFlowTest():
    @allure.title("Login Flow")
    @allure.description("Login Flow")
    def test_login_flow(self):
        logingApp = LogingApp(self.driver)
        logingApp.login()
