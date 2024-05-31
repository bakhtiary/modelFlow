
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_calling_a_none_existing_model():
    response = client.get("/models/none_existing_model")
    assert response.status_code == 404
    assert response.json() == {"detail": "model not found"}


def test_creating_a_model():
    response = client.put("/models/dummy_model_a")
    assert response.status_code == 200
    assert response.json() == {"detail": "model added"}




