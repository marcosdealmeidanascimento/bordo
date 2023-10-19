from typing import Any, Dict, Optional, Union, List
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.activity import Activity
from app.db.schemas.activity import ActivityCreate, ActivityUpdate



class CRUDActivity(CRUDBase[Activity, ActivityCreate, ActivityUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: ActivityCreate) -> Activity:
        db_obj = Activity(
            title= obj_in.title,
            description=obj_in.description,
            init_time=obj_in.init_time,
            end_time=obj_in.end_time,
            category_id=obj_in.category_id,
            user_id=obj_in.user_id,
            post_id=obj_in.post_id
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Activity, obj_in: Union[ActivityUpdate, Dict[str, any]]) -> Activity:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)

    async def getByPost(self, db: AsyncSession, *, post_id: int) -> List:
        stmt = select(self.model).where(self.model.post_id == post_id)
        result = await db.execute(stmt)
        return result.scalars().all()

activity = CRUDActivity(Activity)
