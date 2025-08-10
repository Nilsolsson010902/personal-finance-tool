from fastapi import FastAPI, APIRouter, Depends, HTTPException
from backend.pydantics.entry import EntryCreate, EntryOut, EntryUpdate
from backend.alchemy_models.entry import Entry, Budget, Category
from sqlalchemy.orm import Session
from database.dependencies import get_db

router = APIRouter(prefix = "/entries", tags = ["Entries"]
)

@router.post('/',response_model=EntryOut, status_code=201)
def create_entry(entry: EntryCreate, db: Session = Depends(get_db)):

    category = db.query(Category).filter(Category.category_name == entry.category_name).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")

    db_entry = Entry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry


@router.get('/')
def get_all_entries(db: Session = Depends(get_db)):
    return db.query(Entry).all()

@router.get('/{entry_id}', status_code=200)
def get_entry(entry_id: str, db: Session = Depends(get_db)):
    entry = db.query(Entry).filter(Entry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return entry