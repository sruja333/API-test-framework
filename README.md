# API Test Automation Framework
This repository contains a production-inspired API test automation framework designed to validate backend services through automated testing and continuous integration.

The framework focuses on enforcing quality gates by validating API behavior, error handling, and system health before changes are merged or released.

# Tech Stack
- Python 3
- FastAPI (System Under Test)
- PyTest (Test Automation Framework)
- FastAPI TestClient / httpx – In-process API testing
- Requests (API client)
- Docker (Containerized test execution)
- GitHub Actions (CI pipeline and quality gates)

# Project Structure
```
api-test-framework/
├── app/                    # Sample backend service (FastAPI)
├── tests/                  # API automation tests
│   ├── api/                # Smoke & regression test suites
│   └── conftest.py         # Shared test fixtures
├── quality/                # CI quality gate logic
│   ├── flaky_runner.py     # Flaky test detection controller
│   └── report.json         # Generated flakiness report
├── .github/workflows/      # CI pipeline
├── pytest.ini              # Pytest configuration
├── requirements.txt
└── README.md
``` 
# How it works
1. A sample FastAPI backend simulates a real-world service.
2. PyTest-based automation tests validate API contracts, response codes, and error handling.
3. Tests are categorized into smoke and regression suites.
4. Tests run using FastAPI’s TestClient, eliminating external service dependencies and ensuring CI-safe execution.
5. A GitHub Actions CI pipeline runs on every push.
6. A CI-level quality gate detects flaky tests by re-running the test suite multiple times.
7. The pipeline fails automatically if unstable or flaky tests are detected.

# CI Quality Gate
In addition to standard test execution, this project includes a CI quality gate that detects flaky tests.
## What it does
- Re-runs the test suite multiple times during CI execution
- Tracks pass/fail consistency per test
- Flags tests that behave inconsistently as flaky
- Blocks the pipeline if flakiness exceeds the defined threshold
- Generates a structured JSON report for analysis

This approach helps prevent unstable tests from silently entering production pipelines, a common real-world CI problem.

# Running locally
## Start backend
uvicorn app.main:app --reload
## Run tests
pytest -v
## Running the CI Quality Gate Locally
python quality/flaky_runner.py

# Running with Docker
docker build -t api-tests -f docker/Dockerfile .
docker run api-tests

# Continuous Integration
The project uses GitHub Actions to enforce automated quality checks on every push.
CI responsibilities include:
- Installing dependencies
- Executing the CI quality gate
- Blocking merges when tests fail or exhibit flaky behavior
  
This ensures that only stable and validated changes are integrated.

⭐ Key Concepts Demonstrated
- API contract testing
- Test infrastructure design
- CI/CD integration
- Flaky test detection
- Quality gate enforcement
- Python packaging & test reliability
