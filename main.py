from fastapi import FastAPI
from typing import List
from models import User, Gender, Role 
from uuid import UUID, uuid4


app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Juanita", 
        last_name="Perez",
        gender=Gender.female,
        roles=[Role.student]
    ),
       
    User(
        id=uuid4(), 
        first_name="Rodolfo", 
        last_name="Vargas",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}
