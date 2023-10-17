from fastapi import APIRouter, FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(
    prefix='/chief',
    tags=['Chiefs']
)

class Chief(BaseModel):
    id: str
    name: str
    last_name: str
    region: str
    specialty: str

chiefs = [
    Chief(id="1", name="John", last_name="Doe", region="Paris", specialty="Patisserie"),
    Chief(id="2", name="Jane", last_name="Smith", region="New York", specialty="Boulangerie"),
    Chief(id="3", name="Alice", last_name="Johnson", region="London", specialty="Restauration")
]

#verbs + endpoints

@router.get('', response_model=List[Chief])
async def get_chief():
    return chiefs

@router.get('/{chief_id}', response_model=Chief)
async def get_chief_id(chief_id: str):
    for chief in chiefs:
        if chief.id == chief_id:
            return chief
    raise HTTPException(status_code=400, detail="Chief not found")

@router.post('', response_model=Chief, status_code=201)
async def create_chief(chief: Chief):
    generated_id = uuid.uuid4()
    new_chief = Chief(id=str(generated_id), name=chief.name, last_name=chief.last_name, region=chief.region, specialty=chief.specialty)
    chiefs.append(new_chief)
    return new_chief

@router.patch('/{chief_id}', status_code=204)
async def modify_chief(chief_id: str, modified_chief: Chief):
    for chief in chiefs:
        if chief.id == chief_id:
            chief.name = modified_chief.name
            chief.last_name = modified_chief.last_name
            chief.region = modified_chief.region
            chief.specialty = modified_chief.specialty
            return
    raise HTTPException(status_code=404, detail="Chief not found")

@router.delete('/{chief_id}', status_code=204)
async def delete_chief(chief_id: str):
    for chief in chiefs:
        if chief.id == chief_id:
            chiefs.remove(chief)
            return
    raise HTTPException(status_code=404, detail="Chief not found")