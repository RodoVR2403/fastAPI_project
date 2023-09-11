from fastapi import FastAPI, HTTPException
from typing import List, Optional 
from models import User, Gender, Role, UserUpdateRequest
from uuid import UUID, uuid4
from pydantic import BaseModel



app = FastAPI()
#Here we are adding the DB part that will be showed in localhost:8000/api/v1/users
db: List[User] = [
    User(
        id=UUID("bc9a22e2-bbc0-4203-a559-65e2579985c3"), 
        first_name="Juanita", 
        middle_name="H",
        last_name="Perez",
        gender=Gender.female,
        roles=[Role.student]
    ),
       
    User(
        id=UUID("539671f2-6b98-47ca-9a54-9f0e47e073f1"), 
        first_name="Rodolfo", 
        middle_name="J",
        last_name="Vargas",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Mundo"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

#With this we can register new users
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

#With this one, we can delete a user
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )

@app.put("/api/v1/users/{user_id}", response_model=User)
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user
    # Return a 404 response if the user with the specified ID is not found
    raise HTTPException(
        status_code=404,
        detail=f"User with id {user_id} not found",
    )