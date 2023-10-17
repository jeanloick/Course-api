from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(
    prefix='/recipe',
    tags=['Recipes']
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
    return recipes

@router.get('/{recipe_id}', response_model=Recipe)
async def get_recipe_id(recipe_id: str):
    for recipe in recipes:
        if recipe.id == recipe_id:
            return recipe
    raise HTTPException(status_code=400, detail="Recipe not found")

@router.post('', response_model=Recipe, status_code=201)
async def create_recipe(given_name: str):
    generated_id = uuid.uuid4()
    new_recipe = Recipe(id=str(generated_id), name=given_name)
    recipes.append(new_recipe)
    return new_recipe

@router.patch('{recipe_id}', status_code=204)
async def modify_recipe_name(recipe_id: str, modified_recipe: Recipe):
    for recipe in recipes:
        if recipe.id == recipe_id:
            recipe.name = modified_recipe.name
            return
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.delete('{recipe_id}', status_code=204)
async def delete_recipe(recipe_id: str, ):
    for recipe in recipe:
        if recipe.id == recipe_id:
            recipes.remove(recipe)
            return
    raise HTTPException(status_code=404, detail="Recipe not found")