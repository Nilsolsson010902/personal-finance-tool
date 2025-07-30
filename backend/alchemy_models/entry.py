from sqlalchemy import Column, String, Date, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from models.base import Base
import uuid

class Entry(Base):
    __tablename__ = "entries"
    entry_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    entry_name = Column(String, nullable=False)
    amount = Column(float, nullable=False)
    entry_date = Column(Date, nullable=False)
    type = Column(Enum("income", "expense", name="entry_type"), nullable=False)
    notes = Column(String)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    category_name = Column(String, ForeignKey("categories.category_name"), nullable=False)
    budget_id = Column(UUID(as_uuid=True), ForeignKey("budgets.budget_id"), nullable=False)