import json

import pytest

from utils.api_utils.client import ApiClient
from tests.common_conftest import function_context, context, session_context  # noqa: F401 - re-exposed as fixtures

CONFIG_PATH = "api_config.json"


@pytest.fixture(scope="session")
def api_config():
    with open(CONFIG_PATH) as config_file:
        return json.load(config_file)


@pytest.fixture(scope="session")
def api_client(api_config):
    return ApiClient(api_config["base_url"], api_config["timeout"])
