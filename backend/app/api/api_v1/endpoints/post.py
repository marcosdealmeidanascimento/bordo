from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.Post])
async def read_posts(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Post = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve posts
    """
    posts = await repositories.post.get_multi(db, skip=skip, limit=limit)
    return posts

@router.post("/", response_model=schemas.Post)
async def create_post(
    *,
    db: AsyncSession = Depends(deps.get_db),
    post_in: schemas.PostCreate,
    _: models.Post = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new Post
    """
    post = await repositories.post.create(db, obj_in=post_in)
    return post

@router.get("/{id}", response_model=schemas.Post)
async def read_post_by_id(
    post_id: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.Post = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific post by id.
    """
    post = await repositories.post.get(db, id=post_id)

    return post

@router.put("/{id}", response_model=schemas.Post)
async def update_post(
    *,
    db: AsyncSession = Depends(deps.get_db),
    post_id: int,
    post_in: schemas.PostUpdate,
    _: models.Post = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a post.
    """

    post = await repositories.post.get(db, id=post_id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="The post with this id does not exist in the system",
        )
    post = await repositories.post.update(db, db_obj=post, obj_in=post_in)
    return post

@router.delete("/{id}", response_model=schemas.Post)
async def delete_post(
    db: AsyncSession = Depends(deps.get_db), *, id: int,
) -> Any:
    
    post = await repositories.post.get(db, id=id)
    if not post:
        raise HTTPException(
            status_code=404,
            detail="A post with this id does not exists",
        )
    post = await repositories.post.remove(db=db, id=id)
    return post
