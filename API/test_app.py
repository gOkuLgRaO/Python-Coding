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


def test_login(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data


def test_create_resource(client):
    # Register and login as Admin
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post('/resource', json={"name": "Resource1"}, headers=headers)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Resource1'


def test_create_resource_non_admin(client):
    # Register and login as User
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post('/resource', json={"name": "Resource1"}, headers=headers)
    assert response.status_code == 403


def test_read_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
    response = client.get('/resource/1', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Resource1'


def test_update_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
    response = client.put('/resource/1', json={"name": "Updated Resource1"}, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Resource1'


def test_delete_resource(client):
    client.post('/register', json={"username": "adminuser", "password": "adminpass", "role": "Admin"})
    login_response = client.post('/login', json={"username": "adminuser", "password": "adminpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
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
        response = client.post('/resource', json={"name": f"Resource{_}"}, headers=headers)
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
        client.post('/resource', json={"name": f"Resource{i}"}, headers=headers)

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
    client.post('/resource', json={"name": "TestResource1"}, headers=headers)
    client.post('/resource', json={"name": "TestResource2"}, headers=headers)

    response = client.get('/resources/search?query=TestResource', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2


def test_send_email(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/send-email', json={"email": "test@example.com", "message": "Hello, World!"},
                           headers=headers)
    assert response.status_code == 202
    data = response.get_json()
    assert data['message'] == 'Email is being sent'
