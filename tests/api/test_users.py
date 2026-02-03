import pytest

@pytest.mark.regression
@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_create_user(client, name):
    response = client.post("/users", json={"name": name})

    assert response.status_code == 200
    assert response.json()["name"] == name
