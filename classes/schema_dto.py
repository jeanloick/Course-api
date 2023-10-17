import time
from pydantic import BaseModel
from datetime import datetime



class Recipe(BaseModel):
    
    title: str
    chef: str
    details: str
    difficulties : int
    