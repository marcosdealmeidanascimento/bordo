from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr
from .user import User


# Shared properties
class LogbookBase(BaseModel):
    name: str = None
    description: Optional[str] = None
    user_id: UUID4 = None


# Properties to receive via API on creation
class LogbookCreate(LogbookBase):
    name: str = None
    description: Optional[str] = None
    user_id: UUID4 = None


# Properties to receive via API on update
class LogbookUpdate(LogbookBase):
    name: Optional[str] = None
    description: Optional[str] = None
    user_id: Optional[UUID4] = None


class LogbookInDBBase(LogbookBase):
    id: int
    user: Optional[User]
    # created_at: datetime
    # updated_at: datetime
    class Config:
        orm_mode = True


# Additional properties to return via API
class Logbook(LogbookInDBBase):
    pass


# Additional properties stored in DB
class LogbookInDB(LogbookInDBBase):
    pass
