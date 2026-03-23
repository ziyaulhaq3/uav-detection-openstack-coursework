import pytest
import sys
sys.path.insert(0, '../api')

def test_health_endpoint():
    from app import app
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200

def test_detect_no_image():
    from app import app
    client = app.test_client()
    response = client.post('/detect')
    assert response.status_code == 400
