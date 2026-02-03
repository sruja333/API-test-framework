import requests
import pytest

def test_create_user_without_name(config):
    response = requests.post(
        f"{config['base_url']}/users",
        json={}
    )

    assert response.status_code == 400
