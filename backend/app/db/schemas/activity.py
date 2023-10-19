from typing import List, Optional # noqa: F401, E261
import datetime
from pydantic import UUID4, BaseModel, EmailStr

# Shared properties
class ActivityBase(BaseModel):
    title: str = None
    description: Optional[str] = None
    init_time: Optional[datetime.time] = None
    end_time: Optional[datetime.time] = None
    category_id: int = None
    user_id: UUID4 = None
    post_id: int = None

# Properties to receive via API on creation
class ActivityCreate(ActivityBase):
    title: str = None
    description: Optional[str] = None
    init_time: Optional[datetime.time] = None
    end_time: Optional[datetime.time] = None
    category_id: int = None
    user_id: UUID4 = None
    post_id: int = None

class ActivityByUser(BaseModel):
    user_id: UUID4 = None

class ActivityUpdate(ActivityBase):
    title: str = None
    description: Optional[str] = None
    init_time: Optional[datetime.time] = None
    end_time: Optional[datetime.time] = None
    category_id: int = None

class ActivityInDBBase(ActivityBase):
    id: int
    # created_at: datetime
    # updated_at: datetime
    class Config:
        orm_mode = True


# Additional properties to return via API
class Activity(ActivityInDBBase):
    pass 


# Additional properties stored in DB
class ActivityInDB(ActivityInDBBase):
    pass
