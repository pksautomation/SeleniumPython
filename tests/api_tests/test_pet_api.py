import random

import allure
import pytest

from utils.api_utils.services.pet_service import PetService
from utils.api_utils.api_data import PetData

pytestmark = [pytest.mark.api, pytest.mark.regression]


@allure.title("Pet API - CRUD flow")
class TestPetApi:
    @pytest.mark.order(1)
    def test_add_and_get_pet(self, api_client, context, function_context):
        pet_service = PetService(api_client)
        pet = PetData(pet_id=random.randint(100000, 999999), name="Buddy")

        add_response = pet_service.add_pet(pet.to_payload())
        assert add_response.status_code == 200

        # scratch data needed only inside THIS test - never meant for later steps
        function_context.set("add_response_time_ms", add_response.elapsed.total_seconds() * 1000)
        assert function_context.get("add_response_time_ms") < 10000

        # share this pet's identity with every later step in this scenario
        context.set("pet_id", pet.pet_id)
        context.set("pet_name", pet.name)

        get_response = pet_service.get_pet_by_id(context.get("pet_id"))
        assert get_response.status_code == 200
        assert get_response.json()["name"] == context.get("pet_name")

    @pytest.mark.order(2)
    def test_update_pet_status(self, api_client, context, function_context):
        pet_service = PetService(api_client)
        # proves function_context is isolated per test - unlike context, this never leaks across methods
        assert not function_context.has("add_response_time_ms")

        # depends on the pet created in test_add_and_get_pet
        pet = PetData(pet_id=context.get("pet_id"), name=context.get("pet_name"), status="sold")

        response = pet_service.update_pet(pet.to_payload())
        assert response.status_code == 200
        assert response.json()["status"] == "sold"
        context.set("pet_status", "sold")

    @pytest.mark.order(3)
    def test_find_pets_by_status(self, api_client, context):
        pet_service = PetService(api_client)
        # depends on the status set by test_update_pet_status
        response = pet_service.find_by_status(context.get("pet_status"))
        assert response.status_code == 200
        returned_ids = [pet["id"] for pet in response.json()]
        assert context.get("pet_id") in returned_ids

    @pytest.mark.order(4)
    def test_delete_pet(self, api_client, context):
        pet_service = PetService(api_client)
        # depends on the pet created in test_add_and_get_pet
        response = pet_service.delete_pet(context.get("pet_id"))
        assert response.status_code == 200
