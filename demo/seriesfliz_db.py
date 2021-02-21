from fastapi import FastAPI, Path, Depends
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

import models
from database import Session
import schema

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

# Dependency
def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()

@app.get("/categories")
def categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    cats = [schema.Category(id=id, name=category.name) for id, category in enumerate(categories)]
    return {"categories": cats}
