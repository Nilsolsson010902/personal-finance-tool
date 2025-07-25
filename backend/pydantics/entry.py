from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID
from datetime import date


class EntryCreate(BaseModel):
    entry_name: str = Field(..., example="Groceries")
    amount: float = Field(..., gt=0, example=120.50)
    entry_date: date = Field(..., example="2025-08-01")
    type: Literal["income", "expense"] = Field(..., example="expense")
    notes: Optional[str] = Field(None, example="Bought at ICA")
    budget_id: UUID = Field(..., example="b23e9c18-dffc-4bb1-a477-e6c4d9bbf210")
    category_name: str = Field(..., example="Food")



class EntryUpdate(BaseModel):
    entry_name: Optional[str] = Field(None, example="Groceries")
    amount: Optional[float] = Field(None, gt=0, example=120.50)
    entry_date: Optional[date] = Field(None, example="2025-08-01")
    type: Optional[Literal["income", "expense"]] = Field(None, example="expense")
    notes: Optional[str] = Field(None, example="Bought at ICA")
    budget_id: Optional[UUID] = Field(None, example="b23e9c18-dffc-4bb1-a477-e6c4d9bbf210")
    category_name: Optional[str] = Field(None, example="Food")

    class Config:
        extra = "forbid"



class EntryOut(BaseModel):
    entry_id: UUID
    entry_name: str
    amount: float
    entry_date: date
    type: Literal["income", "expense"]
    notes: Optional[str]
    budget_id: UUID
    category_name: str
    user_id: UUID  

    class Config:
        orm_mode = True
