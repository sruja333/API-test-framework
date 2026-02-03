def test_create_user_without_name(client):
    response = client.post("/users", json={})

    assert response.status_code == 400
