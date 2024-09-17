from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido al Backend con Arquitectura Hexagonal y CQRS"}