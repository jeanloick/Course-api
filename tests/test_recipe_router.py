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
    assert response.status_code == 404 # la recette n'existe pas initialement

def test_get_existing_recipe_by_id():
    # Supposons que vous avez déjà une recette avec cet ID dans votre base de données ou liste
    existing_recipe_id = str(uuid.uuid4())  # Assurez-vous d'utiliser un ID qui existe réellement dans votre système

    response = client.get(f"/recipe/{existing_recipe_id}")

    assert response.status_code == 200  # Assurez-vous que la requête renvoie un code 200 (OK)
    assert response.json() == {"id": existing_recipe_id, "name": "Nom de la recette existante"}  # Assurez-vous que la réponse correspond aux données réelles de la recette


    assert response.status_code == 200  # Assurez-vous que la requête a réussi
    assert response.json() is not None  # Assurez-vous que la réponse contient des données
    assert response.json()["id"] == existing_recipe_id  # Assurez-vous que l'ID dans la réponse correspond à l'ID demandé

def test_create_recipe_failed():
    recipe_data = {
        "given_name": "burger a la tomate"
    }

    response = client.post("/recipe", json=recipe_data)
    assert response.status_code == 422


def test_delete_recipe():
    # Ajoutez une recette à la base de données pour tester
    recipe_id = str(uuid.uuid4())
    response = client.delete(f"/recipe/{recipe_id}")
    assert response.status_code == 404  # En supposant que la recette n'existe pas initialement