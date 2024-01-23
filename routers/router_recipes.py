from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid
from database.firebase import db

router = APIRouter(
    prefix='/recipe',
    tags=['Recipe']
)

class Recipe(BaseModel):
    id: str
    name: str

recipes = [
    Recipe(id="1", name="Tarte aux pommes"),
    Recipe(id="2", name="Pâtes à pizza"),
    Recipe(id="3", name="Guacamole")
]

#verbs + endpoints

@router.get('', response_model=List[Recipe])
async def get_recipe():
    firebase_object = db.child('recipe').get().val()
    result_array = [value for value in firebase_object.values()]
    return result_array

@router.get('/{recipe_id}', response_model=Recipe)
async def get_recipe_id(recipe_id: str):
    firebase_object = db.child('recipe').child(recipe_id).get().val()
    if firebase_object is not None:
        return Recipe(id=recipe_id, name=firebase_object.get('name'))
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.post('', response_model=Recipe, status_code=201)
async def create_recipe(given_name: str):
    generated_id = uuid.uuid4()
    new_recipe = Recipe(id=str(generated_id), name=given_name)
    recipes.append(new_recipe)
    db.child("recipe").child(generated_id).set(new_recipe.model_dump())
    return new_recipe

@router.patch('/{recipe_id}', status_code=204)
async def modify_recipe_name(recipe_id: str, modified_recipe: Recipe):
    firebase_object = db.child('recipes').child(recipe_id).get().val()
    if firebase_object is not None:
        updated_recipe = Recipe(id= recipe_id, **modified_recipe.model_dump())
        return db.child('recipe').child(recipe_id).update(updated_recipe.model_dump())
    raise HTTPException(status_code=404, detail="Recipe not found")



@router.delete('/{recipe_id}', status_code=204)
async def delete_recipe(recipe_id: str):
    firebase_object = db.child('recipe').child(recipe_id).get().val()
    if firebase_object is not None:
        db.child('recipe').child(recipe_id).remove()
        return
    else:
        raise HTTPException(status_code=404, detail="Recipe not found")