import allure
import pytest

from api.pet_service import PetService
from utils.api_data.pet_data import PetData

pytestmark = [pytest.mark.api, pytest.mark.regression]


@allure.title("Pet API - CRUD flow")
class TestPetApi:
    def test_add_and_get_pet(self, api_client):
        pet_service = PetService(api_client)
        pet = PetData(pet_id=1001, name="Buddy")

        add_response = pet_service.add_pet(pet.to_payload())
        assert add_response.status_code == 200

        get_response = pet_service.get_pet_by_id(pet.pet_id)
        assert get_response.status_code == 200
        assert get_response.json()["name"] == "Buddy"

    def test_update_pet_status(self, api_client):
        pet_service = PetService(api_client)
        pet = PetData(pet_id=1001, name="Buddy", status="sold")

        response = pet_service.update_pet(pet.to_payload())
        assert response.status_code == 200
        assert response.json()["status"] == "sold"

    def test_find_pets_by_status(self, api_client):
        pet_service = PetService(api_client)
        response = pet_service.find_by_status("available")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self, api_client):
        pet_service = PetService(api_client)
        response = pet_service.delete_pet(1001)
        assert response.status_code == 200
