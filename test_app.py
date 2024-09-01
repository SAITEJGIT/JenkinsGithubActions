import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_home(client):
    response = client.get('/greetings')
    assert response.status_code == 200
    assert response.json == {'message': 'Hello, Sai!'}

def test_add(client):
    response = client.post('/add', json={'a': 3, 'b': 4})
    assert response.status_code == 200
    assert response.json == {'result': 7}
