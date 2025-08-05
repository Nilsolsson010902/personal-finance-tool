from sqlalchemy import Column, String, Date, Float, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from backend.database.connection  import Base
import uuid

class Category(Base):
    __tablename__ = "categories"
    category_name = Column(String, primary_key=True, nullable=False)
    color = Column(String, nullable=False)