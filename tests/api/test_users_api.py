from api_helpers.api_client import APIClient
from api_helpers.endpoints import USERS


client = APIClient()


def test_get_users():

    response = client.get(USERS)

    assert response.status_code == 200

    response_body = response.json()

    assert len(response_body) > 0

    assert response_body[0]["id"] == 1