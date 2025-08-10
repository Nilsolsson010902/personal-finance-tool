from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal
from uuid import UUID
from datetime import date
from backend.pydantics.recurring import RecurringEntryOut
from decimal import Decimal

class EntryCreateInBudget(BaseModel):
    entry_name: str = Field(..., example="Groceries")
    amount: Decimal = Field(..., gt=0, example=120.50)
    entry_date: date = Field(..., example="2025-08-01")
    type: Literal["income", "expense"] = Field(..., example="expense")
    notes: Optional[str] = Field(None, example="Bought at ICA")
    category_name: str = Field(..., example="Food")


class EntryUpdate(BaseModel):
    entry_name: Optional[str] = Field(None, example="Groceries")
    amount: Optional[Decimal] = Field(None, gt=0, example=120.50)
    entry_date: Optional[date] = Field(None, example="2025-08-01")
    type: Optional[Literal["income", "expense"]] = Field(None, example="expense")
    notes: Optional[str] = Field(None, example="Bought at ICA")
    category_name: Optional[str] = Field(None, example="Food")

    model_config = ConfigDict(extra='forbid')


class EntryOut(BaseModel):
    entry_id: UUID
    entry_name: str
    amount: Decimal
    entry_date: date
    type: Literal["income", "expense"]
    notes: Optional[str]
    budget_id: UUID
    category_name: str
    user_id: UUID
    recurring: Optional[RecurringEntryOut]  

    model_config = ConfigDict(from_attributes=True)

