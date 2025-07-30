from sqlalchemy import Column, String, Date, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from alchemy_models.base import Base
import uuid

class Budget(Base):
    __tablename__ = "budgets"
    budget_id = Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    budget_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    email = Column(String, nullable=False)
