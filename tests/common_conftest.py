import pytest

from utils.common.context import FunctionContext, ClassContext, SessionContext


@pytest.fixture(scope="session")
def session_context():
    return SessionContext()


@pytest.fixture(scope="class")
def context():
    return ClassContext()


@pytest.fixture()
def function_context():
    return FunctionContext()
