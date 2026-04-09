def test_TC001_list_users_page1(base_url, api_session):
    r = api_session.get(f"{base_url}/users?page=1")
    assert r.status_code == 200
    assert "data" in r.json()
    assert len(r.json()["data"]) > 0

def test_TC002_get_single_user(base_url, api_session):
    r = api_session.get(f"{base_url}/users/2")
    assert r.status_code == 200
    assert r.json()["data"]["id"] == 2
    assert "email" in r.json()["data"]

def test_TC003_list_color_resources(base_url, api_session):
    r = api_session.get(f"{base_url}/unknown")
    assert r.status_code == 200
    assert "data" in r.json()
    assert len(r.json()["data"]) > 0

def test_TC004_login_success(base_url, api_session, test_data):
    r = api_session.post(f"{base_url}/login", json=test_data["valid_login"])
    assert r.status_code == 200
    assert "token" in r.json()

def test_TC005_register_success(base_url, api_session, test_data):
    r = api_session.post(f"{base_url}/register", json=test_data["valid_register"])
    assert r.status_code == 200
    assert "token" in r.json()

def test_TC006_create_product(base_url, project_id, api_session, test_data):
    r = api_session.post(
        f"{base_url}/collections/products/records?project_id={project_id}",
        json={"data": test_data["valid_product"]}
    )
    assert r.status_code == 201
    body = r.json()["data"]["data"]
    assert body["name"] == test_data["valid_product"]["name"]
    assert body["price"] == test_data["valid_product"]["price"]

def test_TC007_list_products(base_url, project_id, api_session):
    r = api_session.get(
        f"{base_url}/collections/products/records?project_id={project_id}"
    )
    assert r.status_code == 200
    assert "data" in r.json()

def test_TC008_get_single_product(base_url, project_id, api_session, created_product):
    product_id = created_product["id"]
    r = api_session.get(
        f"{base_url}/collections/products/records/{product_id}?project_id={project_id}"
    )
    assert r.status_code == 200
    assert r.json()["data"]["id"] == product_id

def test_TC009_update_product_patch(base_url, project_id, api_session, created_product, test_data):
    product_id = created_product["id"]
    r = api_session.patch(
        f"{base_url}/collections/products/records/{product_id}?project_id={project_id}",
        json={"data": test_data["updated_product"]}
    )
    assert r.status_code == 200
    assert r.json()["data"]["name"] == test_data["updated_product"]["name"]
   

def test_TC010_delete_product(base_url, project_id, api_session, created_product):
    product_id = created_product["id"]
    r = api_session.delete(
        f"{base_url}/collections/products/records/{product_id}?project_id={project_id}"
    )
    assert r.status_code == 204