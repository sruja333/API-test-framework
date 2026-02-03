import requests
import pytest

@pytest.mark.regression
@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_create_user(config, name):
    payload = {"name": name}
    
    response = requests.post(
        f"{config['base_url']}/users",
        json=payload
    )

    assert response.status_code == 200
    assert response.json()["name"] == name
