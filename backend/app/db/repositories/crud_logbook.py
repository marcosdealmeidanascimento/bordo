from typing import Any, Dict, Optional, Union, List
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.logbook import Logbook
from app.db.schemas.logbook import LogbookCreate, LogbookUpdate


class CRUDLogbook(CRUDBase[Logbook, LogbookCreate, LogbookUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: LogbookCreate) -> Logbook:
        db_obj = Logbook(
            name=obj_in.name,
            description=obj_in.description,
            user_id=obj_in.user_id
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def get_by_name(self, db: AsyncSession, *,
                           name: str, user_id: Any) -> Optional[Logbook]:
        stmt = select(self.model).where(self.model.name == name, self.model.user_id == user_id)
        result = await db.execute(stmt)
        return result.scalars().first()
    

    async def update(seld, db: AsyncSession, *, db_obj: Logbook, obj_in: Union[LogbookUpdate, Dict[str, any]]) -> Logbook:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)


logbook = CRUDLogbook(Logbook)
