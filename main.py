from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.database.models import Base, UserModel
from infrastructure.repositories.user_repository import UserRepository
from application.commands.register_user_command import RegisterUserCommand
from application.queries.get_user_query import GetUserQuery
from uuid import UUID
from pydantic import BaseModel, EmailStr, constr, validator
import os

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://new_user:new_password@localhost/hexagonal_cqrs_backend"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

class UserCreate(BaseModel):
    username: constr(pattern=r'^[a-zA-Z_]+$', min_length=3, max_length=50)
    email: EmailStr

    @validator('username', 'email')
    def strip_spaces(cls, value):
        return value.strip()

    @validator('email')
    def lowercase_email(cls, value):
        return value.lower()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Bienvenido al Backend con Arquitectura Hexagonal y CQRS"}

@app.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)

    existing_user = db.query(UserModel).filter(
        (UserModel.username == user.username) | (UserModel.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario y/o email existente"
        )

    command = RegisterUserCommand(repo)
    new_user = command.handle(user.username, user.email)
    return {"message": "Usuario registrado satisfactoriamente", "user": new_user}

@app.get("/user/{user_id}")
def get_user(user_id: UUID, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    query = GetUserQuery(repo)
    user = query.handle(user_id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return user
