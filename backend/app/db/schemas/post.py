from typing import List, Optional # noqa: F401, E261
import datetime
from pydantic import UUID4, BaseModel, EmailStr

# Shared properties
class PostBase(BaseModel):
    title: str = None
    description: Optional[str] = None
    date: Optional[datetime.date] = None
    user_id: UUID4 = None
    logbook_id: int = None

# Properties to receive via API on creation
class PostCreate(PostBase):
    title: str = None
    description: Optional[str] = None
    date: Optional[datetime.date] = None
    user_id: UUID4 = None
    logbook_id: int = None

class PostUpdate(PostBase):
    title: str = None
    description: Optional[str] = None
    date: Optional[datetime.date] = None

class PostInDBBase(PostBase):
    id: int
    # created_at: datetime
    # updated_at: datetime
    class Config:
        orm_mode = True


# Additional properties to return via API
class Post(PostInDBBase):
    pass 


# Additional properties stored in DB
class PostInDB(PostInDBBase):
    pass
