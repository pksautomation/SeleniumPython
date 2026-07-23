import random

import allure
import pytest

from utils.api_utils.services.user_service import UserService
from utils.api_utils.api_data import UserData

pytestmark = [pytest.mark.api, pytest.mark.regression]


@allure.title("User API - CRUD flow")
class TestUserApi:
    @pytest.mark.order(1)
    def test_create_and_get_user(self, api_client, context):
        user_service = UserService(api_client)
        user = UserData(
            username=f"testuser_fw_{random.randint(100000, 999999)}",
            first_name="Test",
            last_name="User",
            email="testuser_fw1@example.com",
            password="Pass@123",
        )

        create_response = user_service.create_user(user.to_payload())
        assert create_response.status_code == 200

        # share this user's identity with every later step in this scenario
        context.set("username", user.username)
        context.set("password", user.password)

        get_response = user_service.get_user(context.get("username"))
        assert get_response.status_code == 200
        assert get_response.json()["username"] == context.get("username")

    @pytest.mark.order(2)
    def test_login_user(self, api_client, context):
        user_service = UserService(api_client)
        # depends on the user created in test_create_and_get_user
        response = user_service.login(context.get("username"), context.get("password"))
        assert response.status_code == 200

    @pytest.mark.order(3)
    def test_delete_user(self, api_client, context):
        user_service = UserService(api_client)
        # depends on the user created in test_create_and_get_user
        response = user_service.delete_user(context.get("username"))
        assert response.status_code == 200
