from pydantic import BaseModel

class Category(BaseModel):
    id: int
    name: str

class Serie(BaseModel):
    title: str
    description: str
    category: Category
