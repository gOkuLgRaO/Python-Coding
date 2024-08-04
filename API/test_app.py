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
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/resource', json={"name": "Resource1"}, headers=headers)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Resource1'


def test_read_resource(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
    response = client.get('/resource/1', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Resource1'


def test_update_resource(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
    response = client.put('/resource/1', json={"name": "Updated Resource1"}, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Updated Resource1'


def test_delete_resource(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    client.post('/resource', json={"name": "Resource1"}, headers=headers)
    response = client.delete('/resource/1', headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Resource deleted successfully'
