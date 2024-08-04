import pytest
from app import app, db

"""
pytest: A testing framework for Python.
Imports the app and db objects from the application module.
"""


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


"""
Defines a pytest fixture named client for setting up and tearing down the test environment.
Sets the Flask app configuration to TESTING mode.
Uses a separate SQLite database (test.db) for testing.
Creates a test client using app.test_client().
Establishes an application context to create the database tables.
Yields the test client for use in the tests.
Drops all tables after the tests are done.
"""


def test_register(client):
    response = client.post('/register', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['username'] == 'testuser'


"""
Tests the user registration endpoint.
Sends a POST request to /register with a JSON payload containing username and password.
Asserts that the response status code is 201 (Created).
Extracts the JSON response data.
Asserts that the username in the response data matches the expected value.
"""


def test_login(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    data = response.get_json()
    assert 'access_token' in data


"""
Tests the user login endpoint.
Registers a user first to ensure there is a user to log in with.
Sends a POST request to /login with the same username and password.
Asserts that the response status code is 200 (OK).
Extracts the JSON response data.
Asserts that the response contains an access_token.
"""


def test_create_resource(client):
    client.post('/register', json={"username": "testuser", "password": "testpass"})
    login_response = client.post('/login', json={"username": "testuser", "password": "testpass"})
    token = login_response.get_json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post('/resource', json={"name": "Resource1"}, headers=headers)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Resource1'


"""
Tests the resource creation endpoint.
Registers a user and logs in to get an access token.
Constructs the authorization headers with the token.
Sends a POST request to /resource with a JSON payload containing the resource name and the authorization headers.
Asserts that the response status code is 201 (Created).
Extracts the JSON response data.
Asserts that the resource name in the response matches the expected value.
"""


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


"""
Tests the resource retrieval endpoint.
Registers a user and logs in to get an access token.
Constructs the authorization headers with the token.
Creates a resource first.
Sends a GET request to /resource/1 (assuming the resource ID is 1) with the authorization headers.
Asserts that the response status code is 200 (OK).
Extracts the JSON response data.
Asserts that the resource name in the response matches the expected value.
"""


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


"""
Tests the resource update endpoint.
Registers a user and logs in to get an access token.
Constructs the authorization headers with the token.
Creates a resource first.
Sends a PUT request to /resource/1 (assuming the resource ID is 1) with a JSON payload containing the updated resource name and the authorization headers.
Asserts that the response status code is 200 (OK).
Extracts the JSON response data.
Asserts that the updated resource name in the response matches the expected value.
"""


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


"""
Tests the resource deletion endpoint.
Registers a user and logs in to get an access token.
Constructs the authorization headers with the token.
Creates a resource first.
Sends a DELETE request to /resource/1 (assuming the resource ID is 1) with the authorization headers.
Asserts that the response status code is 200 (OK).
Extracts the JSON response data.
Asserts that the response message indicates the resource was deleted successfully.
"""
