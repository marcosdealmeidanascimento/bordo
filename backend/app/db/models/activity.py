import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, TIME
from sqlalchemy.orm import relationship


class Activity(Base):
    __tablename__ = "activity"
    """
    Database Model for an application user
    """
    id = Column(
        Integer, primary_key=True
    )
    title = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    init_time = Column(TIME, nullable=True)
    end_time = Column(TIME, nullable=True)
    post_id = Column(Integer, ForeignKey("post.id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

