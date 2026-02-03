import requests
import pytest

@pytest.mark.smoke
def test_health_check(config):
    response = requests.get(f"{config['base_url']}/health")
    
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
