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
    # Leo todas las categorías
    categories = db.query(models.Category).all()
    # Leo las categorías usando la sintaxis ORM de SQLAlchemy
    cats = [schema.Category(id=id, name=category.name) for id, category in enumerate(categories)]
    return {"categories": cats}

@app.get("/series/{category_str}", response_model=List[schema.Serie])
def series(category_str: str, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter_by(name=category_str).first()

    if category is None:
        return []
    else:
        series_db = db.query(models.Serie).join(models.Category).filter(models.Category.id==category.id).all()
        series = [schema.Serie(title=serie.title, description=serie.description, category=category_str) for serie in series_db]
        print(series)
        return series
