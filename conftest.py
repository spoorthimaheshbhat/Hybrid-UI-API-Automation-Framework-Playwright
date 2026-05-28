import pytest


@pytest.fixture(scope="function")
def test_data():

    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }