import pytest
import app

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Tests the main '/' route for a 200 status and correct JSON."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == "Hello, World!"
    assert response.json['status'] == "success"

def test_health_route(client):
    """Tests the '/health' route to ensure the API is up."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == "up"
