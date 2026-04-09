import requests

def test_TC011_get_user_not_found(base_url, api_session):
    r = api_session.get(f"{base_url}/users/9999")
    assert r.status_code == 404

def test_TC012_get_resource_not_found(base_url, api_session):
    r = api_session.get(f"{base_url}/unknown/9999")
    assert r.status_code == 404

def test_TC013_login_missing_password(base_url, api_session):
    r = api_session.post(f"{base_url}/login", json={"email": "eve.holt@reqres.in"})
    assert r.status_code == 400
    assert "error" in r.json()

def test_TC014_login_missing_email(base_url, api_session):
    r = api_session.post(f"{base_url}/login", json={"password": "cityslicka"})
    assert r.status_code == 400
    assert "error" in r.json()

def test_TC015_login_invalid_email(base_url, api_session):
    r = api_session.post(f"{base_url}/login", json={"email": "naoexiste@fake.com", "password": "wrong"})
    assert r.status_code == 400
    assert "error" in r.json()

def test_TC016_register_missing_password(base_url, api_session):
    r = api_session.post(f"{base_url}/register", json={"email": "eve.holt@reqres.in"})
    assert r.status_code == 400
    assert "error" in r.json()

def test_TC017_create_product_without_data_wrapper(base_url, project_id, api_session, test_data):
    r = api_session.post(
        f"{base_url}/collections/products/records?project_id={project_id}",
        json=test_data["valid_product"]
    )
    assert r.status_code == 400

def test_TC018_access_collections_without_api_key(base_url, project_id):
    r = requests.get(
        f"{base_url}/collections/products/records?project_id={project_id}"
    )
    assert r.status_code == 401

def test_TC019_get_product_invalid_id(base_url, project_id, api_session):
    r = api_session.get(
        f"{base_url}/collections/products/records/id-inexistente?project_id={project_id}"
    )
    assert r.status_code == 404

def test_TC020_delete_product_invalid_id(base_url, project_id, api_session):
    r = api_session.delete(
        f"{base_url}/collections/products/records/id-inexistente?project_id={project_id}"
    )
    assert r.status_code == 404