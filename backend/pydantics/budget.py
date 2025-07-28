from pydantic import BaseModel, Field
from typing import Optional, Literal
from uuid import UUID
from datetime import date

class BudgetCreate(BaseModel):
    budget_name: str = Field(..., example="Nils September budget")
    start_date: date = Field(..., example = "2025-09-01")
    end_date: date = Field(..., example = "2025-09-31")

class BudgetUpdate(BaseModel):
    budget_name: Optional[str] = Field(..., example = "Nils oktober budget")
    start_date: Optional[date] = Field(..., example = "2025-10-01")
    start_date: Optional[date] = Field(..., example = "2025-10-30")

    class config:
        extra = "forbid"

class BudgetOut(BaseModel):
    budget_id: UUID
    budget_name: str
    start_date: date
    end_date: date
    user_id: UUID

    class Config:
        orm_mode = True 