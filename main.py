from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from application.commands.register_user_command import RegisterUserCommand
from infrastructure.repositories.user_repository import UserRepository
from pydantic import BaseModel, EmailStr, constr
from infrastructure.database.connection import get_db

app = FastAPI()

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50, regex=r'^[a-zA-Z0-9_]+$')
    email: EmailStr

@app.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    command = RegisterUserCommand(repo)
    try:
        new_user = command.handle(user.username, user.email)
        return {"message": "Usuario registrado satisfactoriamente", "user": new_user}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Backend con Arquitectura Hexagonal y CQRS"}
