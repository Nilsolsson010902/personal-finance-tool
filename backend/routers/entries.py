from typing import List, Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.alchemy_models.entry import Entry
from backend.alchemy_models.budget import Budget
from backend.alchemy_models.category import Category
from backend.pydantics.entry import EntryCreateInBudget, EntryOut, EntryUpdate
from backend.database.resources import (
    get_budget_or_404,
    get_category_or_404,
    get_entry_in_budget_or_404,

router = APIRouter(prefix = "/entries", tags = ["Entries"]
)

BudgetDep = Annotated[Budget, Depends(get_budget_or_404)]
EntryDep  = Annotated[Entry,  Depends(get_entry_in_budget_or_404)]

@router.post('/budgets/{budget_id}',response_model=EntryOut, status_code=201)
def create_entry(budget: BudgetDep, entry: EntryCreateInBudget, db: Session = Depends(get_db)):

    category = db.query(Category).filter(Category.category_name == entry.category_name).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")

    db_entry = Entry(
        entry_name = entry.entry_name,
        amount = entry.amount,
        entry_date = entry.entry_date,
        type = entry.type,
        notes = entry.notes,
        category_name = entry.category_name,
        budget_id = budget_id,
        user_id = budget.user_id
    )

    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@router.get('/budgets/{budget_id}', response_model = List[EntryOut])
def get_all_entries(budget: BudgetDep, db: Session = Depends(get_db)):
   entries = db.query(Entries).filter(Entry.budget_id == budget_id).all()
   return entries


@router.get('/budgets/{budget_id}/{entry_id}', response_model=EntryOut)
def get_entry_in_budget( entry: Entry = Depends(get_entry_in_budget_or_404)):
    return entry

@router.put('/{entry_id}', response_model=EntryOut)
def update_entry(entry_id: UUID, entry: EntryUpdate, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter(Entry.entry_id == entry_id).first()
    if not entry: 
        raise HTTPException(status_code=404, detail= "Entry not found")
    
    if payload.category_name is not None:
        _ = get_category_or_404(entry.category_name, db)

    for k, v in entry.dict(exclude_unset=True).items():
        setattr(entry, k, v)

    db.commit()
    db.refresh(entry)
    return entry

@router.delete("/{entry_id}", status_code=204)
def delete_entry(entry_id: UUID, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter(Entry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found.")
    db.delete(entry)
    db.commit()
    return None