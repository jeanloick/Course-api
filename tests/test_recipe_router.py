import json
import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_recipes():
    response = client.get("/recipe")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_recipe_by_id():
    recipe_id = str(uuid.uuid4())
    response = client.get(f"/recipe/{recipe_id}")
    assert response.status_code == 404 

def test_get_existing_recipe_by_id():
    existing_recipe_id = "fb260f8a-0593-4c34-a3bb-943ad6a2447d"
    response = client.get(f"/recipe/{existing_recipe_id}")

    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["id"] == existing_recipe_id
    assert response.json()["name"] == "pizza"


def test_get_nonexistent_recipe_by_id():
    nonexistent_recipe_id = str(uuid.uuid4())
    response = client.get(f"/recipe/{nonexistent_recipe_id}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Recipe not found"}



def test_delete_recipe():
    recipe_id = str(uuid.uuid4())
    response = client.delete(f"/recipe/{recipe_id}")
    assert response.status_code == 404  