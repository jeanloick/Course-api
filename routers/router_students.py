from fastapi import APIRouter,FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(
    prefix='/students',
    tags=['Students']
)

class Student(BaseModel):
    id: int
    name: str
class StudentNoID(BaseModel):
    name: str

students = [
    Student(id="1", name="adama"),
    Student(id="2", name="adrien"),
    Student(id="3", name="Akbar")
]

#verbs + endpoints

@router.get('', response_model=list[Student])
async def get_student():
    return students

@router.get('/{student_id}', response_model=Student)
async def get_student_id(student_id: str):
  
    for student in students:
        if student.id == student_id:
            return student
        raise HTTPException(status_code=400, detail="student not found")


@router.post('', response_model=Student, status_code=201)
async def create_student(given_name: str):
    generatedId= uuid.uuid4()
    new_student = Student(id=str(generatedId), name=given_name)
    students.append(new_student)
    return new_student


@router.patch('{student_id}', status_code=204)
async def modify_student_name(student_id:str, modifiedStudent: StudentNoID):
    for student in students:
        if student.id == student_id:
            student.name=modifiedStudent.name
            return
    raise HTTPException(status_code= 404, detail="Student not found")

