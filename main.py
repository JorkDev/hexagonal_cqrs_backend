from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel, EmailStr, constr, validator
from infrastructure.database.models import UserModel, Base

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://new_user:new_password@localhost/hexagonal_cqrs_backend"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class UserCreate(BaseModel):
    username: constr(min_length=3, max_length=50, pattern=r'^[a-zA-Z0-9_]+$')
    email: EmailStr

    @validator('username')
    def no_whitespace(cls, value):
        if ' ' in value:
            raise ValueError('Username cannot contain spaces')
        return value

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(UserModel).filter(
        (UserModel.username == user.username) | (UserModel.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists."
        )

    new_user = UserModel(username=user.username, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuario registrado satisfactoriamente", "user": new_user}

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Backend con Arquitectura Hexagonal y CQRS"}
