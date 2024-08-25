import pytest
from app import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


def test_register(client):
    response = client.post('/register', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'


def test_register_missing_username(client):
    response = client.post('/register', json={"password": "testpass"})
    assert response.status_code == 400


def test_register_missing_password(client):
    response = client.post('/register', json={"username": "testuser"})
    assert response.status_code == 400


def test_register_duplicate_username(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    response = client.post('/register', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 400


def test_login(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data


def test_login_invalid_username(client):
    response = client.post('/login', json={"username": "wronguser", "password": "testpass"})
    assert response.status_code == 401


def test_login_invalid_password(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    response = client.post('/login', json={"username": "testuser", "password": "wrongpass"})
    assert response.status_code == 401


def test_login_missing_username(client):
    response = client.post('/login', json={"password": "testpass"})
    assert response.status_code == 400


def test_login_missing_password(client):
    response = client.post('/login', json={"username": "testuser"})
    assert response.status_code == 400


def test_create_resource(client):
    # Register and login as Admin
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    # Provide required fields for resource creation
    response = client.post('/resource', json={
        "name": "Resource1",
        "location": "Location1",
        "cost": 10.0
    }, headers=headers)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Resource1'
    assert data['location'] == 'Location1'
    assert data['cost'] == 10.0


def test_create_resource_missing_name(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post('/resource', json={"location": "Location1", "cost": 10.0}, headers=headers)
    assert response.status_code == 400


def test_create_resource_non_admin(client):
    # Register and login as User
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    # Try creating a resource without Admin privileges
    response = client.post('/resource', json={
        "name": "Resource1",
        "location": "Location1",
        "cost": 10.0
    }, headers=headers)
    assert response.status_code == 403


def test_read_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={
        "name": "Resource1",
        "location": "Location1",
        "cost": 10.0
    }, headers=headers)
    response = client.get('/resource/1', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Resource1'
    assert data['location'] == 'Location1'
    assert data['cost'] == 10.0


def test_update_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={
        "name": "Resource1",
        "location": "Location1",
        "cost": 10.0
    }, headers=headers)
    response = client.put('/resource/1', json={
        "name": "Updated Resource1",
        "location": "Updated Location1",
        "cost": 15.0
    }, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Resource1'
    assert data['location'] == 'Updated Location1'
    assert data['cost'] == 15.0


def test_delete_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={
        "name": "Resource1",
        "location": "Location1",
        "cost": 10.0
    }, headers=headers)
    response = client.delete('/resource/1', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Resource deleted successfully'


def test_rate_limiting(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    rate_limit_exceeded = False
    for _ in range(11):
        response = client.post('/resource', json={
            "name": f"Resource{_}",
            "location": f"Location{_}",
            "cost": 10.0 + _
        }, headers=headers)
        if response.status_code == 429:
            rate_limit_exceeded = True
            break

    assert rate_limit_exceeded


def test_list_resources_pagination(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    for i in range(15):
        client.post('/resource', json={
            "name": f"Resource{i}",
            "location": f"Location{i}",
            "cost": 10.0 + i
        }, headers=headers)

    response = client.get('/resources?page=1&per_page=10', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['total'] == 15
    assert data['pages'] == 2
    assert len(data['resources']) == 10


def test_search_resources(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={
        "name": "TestResource1",
        "location": "TestLocation1",
        "cost": 10.0
    }, headers=headers)
    client.post('/resource', json={
        "name": "TestResource2",
        "location": "TestLocation2",
        "cost": 20.0
    }, headers=headers)

    response = client.get('/resources/search?query=TestResource', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2


def test_send_email(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/send-email', json={
        "email": "test@example.com",
        "message": "Hello, World!"
    }, headers=headers)
    assert response.status_code == 202
    data = response.get_json()
    assert data['message'] == 'Email is being sent'


def test_send_email_missing_message(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/send-email', json={"email": "test@example.com"}, headers=headers)
    assert response.status_code == 400


def test_send_email_invalid_email(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/send-email', json={"email": "invalid-email", "message": "Hello, World!"}, headers=headers)
    assert response.status_code == 400
