from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

origins = [
    "http://localhost:8100",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"msg": "Hola a todo el  mundo"}

class Category(str, Enum):
    Comedy = "Comedy"
    Drama = "Drama"
    Musical = "Musical"

@app.get("/categories")
def hello():
    return {"categories": [{'id': 0, 'text': "Comedy"}, {'id': 1, 'text': "Drama"}, {'id': 2, 'text': 'Musical'}]}

@app.get("/categories")
def hello():
    return {"categories": [{'id': 0, 'text': "Comedy"}, {'id': 1, 'text': "Drama"}, {'id': 2, 'text': 'Musical'}]}

class Serie(BaseModel):
    title: str
    description: str
    category: Category

# Comprueba que sea un valor válido
@app.get("/series/{category}", response_model=List[Serie])
def series(category: Category):
    mejor_imposible = Serie(title="Mejor imposible", description="Mejor imposible", category=Category.Comedy)
    print(category)

    if category == Category.Comedy:
        print("Mejor")
        return [mejor_imposible]
    else:
        return []
