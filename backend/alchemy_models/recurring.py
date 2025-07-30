from sqlalchemy import Column, String, Date, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from alchemy_models.base import Base
import uuid

class Reccuring(Base):
    __tablename__ = "reccuring_entries"
    recurring_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    frequency = Column(Enum('daily', 'weekly', 'monthly', 'yearly', name="frequency_type"), nullable=False)
    entry_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=False)
    