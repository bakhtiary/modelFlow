
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_creating_a_model_provides_an_id_this_id_can_be_used_to_get_model_details():

    response = client.put("model_template", json={"name": "some_name", "location": "some_location", "docker_image": "the_image"})
    model_id = response.json()["id"]

    get_response = client.get(f"model_template/{model_id}")

    assert get_response.json()["name"] == "some_name"
    assert get_response.json()["location"] == "some_location"
    assert get_response.json()["docker_image"] == "the_image"


def test_calling_a_none_existing_model():
    response = client.get("/models/none_existing_model")
    assert response.status_code == 404
    assert response.json() == {"detail": "model not found"}


def test_creating_a_model():
    response = client.put("/models/dummy_model_a")
    assert response.status_code == 200
    assert response.json() == {"detail": "model added"}




