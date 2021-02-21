from fastapi import FastAPI, Path
from typing import  Optional
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hola a todo el  mundo"}

@app.get("/hello/{name}")
def  hello(name):
    return {"msg": f"Hola, {name}"}

@app.get("/vota/{puntuacion}")
def hello(puntuacion: int):
    return {"resultado": f"Sumo {puntuacion}"}

@app.get("/hola/{name}")
def  hello(name: Optional[str] = Path("desconocido", min_length=5, max_length=30)):
    return {"msg": f"Hola, {name}"}

@app.get("/vota2/{puntuacion}")
def hello(puntuacion: int = Path(0, gt=0, le=10)):
   return {"resultado": f"Sumo {puntuacion}"}

@app.get("/list/{category}")
def list(category, page=0):
    return {"series": f"series from category {category}, from page {page}"}
