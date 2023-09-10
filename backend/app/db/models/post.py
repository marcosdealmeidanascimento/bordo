import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, Date, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"


    id = Column(
        Integer, primary_key=True
    )
    title =Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    date = Column(Date(), nullable=True)
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
    )
    logbook_id = Column(Integer, ForeignKey("logbook_id", ondelete="CASCADE"), nullable=False )

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )