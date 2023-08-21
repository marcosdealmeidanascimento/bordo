import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "category"
    """
    Database Model for an application user
    """
    id = Column(
        Integer, primary_key=True
    )
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
