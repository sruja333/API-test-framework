import subprocess
import time
import pytest
import yaml

@pytest.fixture(scope="session", autouse=True)
def start_api_server():
    """
    Starts the FastAPI server before tests and stops it after.
    """
    process = subprocess.Popen(
        ["uvicorn", "app.main:app"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # Give server time to start
    time.sleep(2)

    yield

    process.terminate()


@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)
