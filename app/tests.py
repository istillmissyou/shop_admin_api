from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_category():
    response = client.post('/api/v1/categories', json={"name": "test_name"})
    assert response.status_code == 200
    assert response.json() == {
        "name": "test_name",
        "id": 1,
        "products": []
    }


test_create_category()
