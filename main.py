from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from infrastructure.database.models import Base, UserModel

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://new_user:new_password@localhost/hexagonal_cqrs_backend"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/")
def register_user(username: str, email: str, db: Session = Depends(get_db)):
    new_user = UserModel(username=username, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuario registrado satisfactoriamente", "user": new_user}

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Backend con Arquitectura Hexagonal y CQRS"}

Base.metadata.create_all(bind=engine)
