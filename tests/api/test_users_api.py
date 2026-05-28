from api.api_client import APIClient
from api.endpoints import USERS


client = APIClient()


def test_get_users():

    response = client.get(USERS)

    assert response.status_code == 200

    response_body = response.json()

    assert "data" in response_body