import allure
import pytest

from api.user_service import UserService
from utils.api_data.user_data import UserData

pytestmark = [pytest.mark.api, pytest.mark.regression]


@allure.title("User API - CRUD flow")
class TestUserApi:
    def test_create_and_get_user(self, api_client):
        user_service = UserService(api_client)
        user = UserData(
            username="testuser_fw1",
            first_name="Test",
            last_name="User",
            email="testuser_fw1@example.com",
            password="Pass@123",
        )

        create_response = user_service.create_user(user.to_payload())
        assert create_response.status_code == 200

        get_response = user_service.get_user(user.username)
        assert get_response.status_code == 200
        assert get_response.json()["username"] == "testuser_fw1"

    def test_login_user(self, api_client):
        user_service = UserService(api_client)
        response = user_service.login("testuser_fw1", "Pass@123")
        assert response.status_code == 200

    def test_delete_user(self, api_client):
        user_service = UserService(api_client)
        response = user_service.delete_user("testuser_fw1")
        assert response.status_code == 200
