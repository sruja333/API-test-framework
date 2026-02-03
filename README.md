# API Test Automation Framework
This repository contains a production-inspired API test automation framework designed to validate backend services through automated testing and continuous integration.

The framework focuses on enforcing quality gates by validating API behavior, error handling, and system health before changes are merged or released.

# Tech Stack
- Python 3
- FastAPI (System Under Test)
- PyTest (Test Framework)
- Requests (API client)
- Docker (Containerized test execution)
- GitHub Actions (CI pipeline)

# Project Structure
```
api-test-framework/
├── app/                 # Sample backend service
├── tests/               # API automation tests
├── config/              # Environment configuration
├── docker/              # Dockerized test setup
└── .github/workflows/   # CI pipeline
``` 
# How it works
1. A sample FastAPI backend simulates a real-world service.
2. PyTest-based automation tests validate API contracts, response codes, and error scenarios.
3. Tests are categorized into smoke and regression suites.
4. A GitHub Actions pipeline runs tests automatically on every push.
5. The pipeline fails if any quality checks do not pass.

# Running locally
## Start backend
uvicorn app.main:app --reload
## Run tests
pytest -v

# Running with Docker
docker build -t api-tests -f docker/Dockerfile .
docker run api-tests

# Continous Integration
The project uses GitHub Actions to automatically execute tests on every code push.
Any test failure blocks the pipeline, ensuring only validated changes are integrated.
