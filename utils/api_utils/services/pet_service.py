import allure

from utils.api_utils.client.base_service import BaseService
from utils.api_utils.client.endpoints import PetEndpoints


class PetService(BaseService):
    @allure.step("Adding a new pet")
    def add_pet(self, pet_payload):
        return self.client.post(PetEndpoints.ADD_PET, json=pet_payload)

    @allure.step("Getting pet by id '{1}'")
    def get_pet_by_id(self, pet_id):
        return self.client.get(PetEndpoints.GET_PET_BY_ID.format(pet_id=pet_id))

    @allure.step("Updating pet")
    def update_pet(self, pet_payload):
        return self.client.put(PetEndpoints.UPDATE_PET, json=pet_payload)

    @allure.step("Deleting pet by id '{1}'")
    def delete_pet(self, pet_id):
        return self.client.delete(PetEndpoints.DELETE_PET.format(pet_id=pet_id))

    @allure.step("Finding pets by status '{1}'")
    def find_by_status(self, status):
        return self.client.get(PetEndpoints.FIND_BY_STATUS, params={"status": status})
