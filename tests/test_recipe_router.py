from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_get_recipe(client):
    response = client.get("/recipe")
    assert response.status_code == 200

def test_get_recipe_id(client):
    response = client.get("/recipe/1")
    assert response.status_code == 200