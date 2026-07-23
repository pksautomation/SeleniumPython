import allure

from utils.api_utils.client.base_service import BaseService
from utils.api_utils.client.endpoints import UserEndpoints


class UserService(BaseService):
    @allure.step("Creating a new user")
    def create_user(self, user_payload):
        return self.client.post(UserEndpoints.CREATE_USER, json=user_payload)

    @allure.step("Getting user '{1}'")
    def get_user(self, username):
        return self.client.get(UserEndpoints.GET_USER.format(username=username))

    @allure.step("Updating user '{1}'")
    def update_user(self, username, user_payload):
        return self.client.put(UserEndpoints.UPDATE_USER.format(username=username), json=user_payload)

    @allure.step("Deleting user '{1}'")
    def delete_user(self, username):
        return self.client.delete(UserEndpoints.DELETE_USER.format(username=username))

    @allure.step("Logging in as '{1}'")
    def login(self, username, password):
        return self.client.get(UserEndpoints.LOGIN, params={"username": username, "password": password})
