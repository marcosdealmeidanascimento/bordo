from typing import List, Optional # noqa: F401, E261
# from datetime import datetime
from pydantic import UUID4, BaseModel, EmailStr


# Shared properties
class CategoryBase(BaseModel):
    name: str = None
    description: Optional[str] = None


# Properties to receive via API on creation
class CategoryCreate(CategoryBase):
    name: str = None
    description: Optional[str] = None


# Properties to receive via API on update
class CategoryUpdate(CategoryBase):
    name: str = None
    description: Optional[str] = None


class CategoryInDBBase(CategoryBase):
    id: int
    # created_at: datetime
    # updated_at: datetime
    class Config:
        orm_mode = True


# Additional properties to return via API
class Category(CategoryInDBBase):
    pass


# Additional properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass
