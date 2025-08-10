# backend/dependencies/resources.py
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from backend.database.dependencies import get_db
from backend.alchemy_models.budget import Budget
from backend.alchemy_models.entry import Entry
from backend.alchemy_models.category import Category

def get_budget_or_404(
    budget_id: UUID,
    db: Session = Depends(get_db),
) -> Budget:
    budget = db.query(Budget).filter(Budget.budget_id == budget_id).first()
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found.")
    return budget

def get_category_or_404(
    category_name: str,
    db: Session = Depends(get_db),
) -> Category:
    cat = db.query(Category).filter(Category.category_name == category_name).first()
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found.")
    return cat

def get_entry_in_budget_or_404(
    budget_id: UUID,
    entry_id: UUID,
    db: Session = Depends(get_db),
) -> Entry:
    entry = (
        db.query(Entry)
        .filter(Entry.entry_id == entry_id, Entry.budget_id == budget_id)
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found in this budget.")
    return entry
