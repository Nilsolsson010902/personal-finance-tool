from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import date

class CategoryCreate(BaseModel):
    category_name: str = Field(..., example= "Food")
    color: str = Field(..., example="Green")

class CategoryUpdate(BaseModel):
    color: Optional[str] = Field(..., example="Green")

    class config:
        extra ="forbid"

class CategoryOut(BaseModel):
    category_name: str 
    color: str

    class config:
        orm_mode = True