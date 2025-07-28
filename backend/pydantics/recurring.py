from pydantic import BaseModel
from typing import Literal
from uuid import UUID


class RecurringEntryCreate(BaseModel):
    frequency: Literal["daily", "weekly", "monthly", "yearly"]

class RecurringEntryOut(BaseModel):
    recurring_id: UUID
    entry_id: UUID
    frequency: Literal["daily", "weekly", "monthly", "yearly"]
