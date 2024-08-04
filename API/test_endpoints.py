import requests

# Base URL
base_url = "http://127.0.0.1:5000"

# Register a new user
response = requests.post(f"{base_url}/register", json={"username": "testuser", "password": "testpass"})
print(response.json())

# Login to get access token
response = requests.post(f"{base_url}/login", json={"username": "testuser", "password": "testpass"})
token = response.json().get("access_token")
print(f"Token: {token}")

# Headers with Authorization
headers = {"Authorization": f"Bearer {token}"}

# Create a new resource
response = requests.post(f"{base_url}/resource", json={"name": "Resource1"}, headers=headers)
print(response.json())

# Read the resource
response = requests.get(f"{base_url}/resource/1", headers=headers)
print(response.json())

# Update the resource
response = requests.put(f"{base_url}/resource/1", json={"name": "Updated Resource1"}, headers=headers)
print(response.json())

# Delete the resource
response = requests.delete(f"{base_url}/resource/1", headers=headers)
print(response.json())
