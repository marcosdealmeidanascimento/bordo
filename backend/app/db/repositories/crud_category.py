from typing import Any, Dict, Optional, Union, List
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.category import Category
from app.db.schemas.category import CategoryCreate, CategoryUpdate


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: CategoryCreate) -> Category:
        db_obj = Category(
            name=obj_in.name,
            description=obj_in.description,
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def get_by_name(self, db: AsyncSession, *,
                           name: str) -> Optional[Category]:
        stmt = select(self.model).where(self.model.name == name)
        result = await db.execute(stmt)
        return result.scalars().first()
    

    async def update(seld, db: AsyncSession, *, db_obj: Category, obj_in: Union[CategoryUpdate, Dict[str, any]]) -> Category:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)


category = CRUDCategory(Category)
