import pytest
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("REQRES_API_KEY")
PROJECT_ID = "10504"

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="session")
def project_id():
    return PROJECT_ID

@pytest.fixture(scope="session")
def test_data():
    with open("fixtures/users.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def demo_session():
    """Endpoints demo — sem autenticação"""
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s

@pytest.fixture(scope="session")
def api_session():
    """Endpoints de projeto — requer x-api-key"""
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "x-api-key": "<YOUR-API-KEY-HERE>"
    })
    return s

@pytest.fixture(scope="session")
def created_product(base_url, project_id, api_session, test_data):
    """Cria um produto e retorna o objeto completo para uso nos testes de GET/PATCH/DELETE"""
    r = api_session.post(
        f"{base_url}/collections/products/records?project_id={project_id}",
        json={"data": test_data["valid_product"]}
    )
    assert r.status_code == 201
    return r.json()["data"]