from typing import Any, Dict, Optional, Union, List
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.db.repositories.base import CRUDBase
from app.db.models.post import Post
from app.db.schemas.post import PostCreate, PostUpdate


class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):

    async def create(self, db: AsyncSession, *, obj_in: PostCreate) -> Post:
        db_obj = Post(
            title= obj_in.title,
            description=obj_in.description,
            date=obj_in.date,
            user_id=obj_in.user_id,
            logbook_id=obj_in.logbook_id
        )
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
    
    async def update(self, db: AsyncSession, *, db_obj: Post, obj_in: Union[PostUpdate, Dict[str, any]]) -> Post:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return await super().update(db, db_obj=db_obj, obj_in=update_data)
    
post = CRUDPost(Post)
