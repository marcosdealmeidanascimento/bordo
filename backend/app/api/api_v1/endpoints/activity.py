from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()

@router.get("/", response_model=List[schemas.Activity])
async def read_activities(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve activities
    """
    activities = await repositories.activity.get_multi(db, skip=skip, limit=limit)
    return activities

@router.post("/", response_model=schemas.Activity)
async def create_activity(
    *,
    db: AsyncSession = Depends(deps.get_db),
    activity_in: schemas.ActivityCreate,
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new Activity
    """
    activity = await repositories.activity.create(db, obj_in=activity_in)
    return activity

@router.get("/{activity_id}", response_model=schemas.Activity)
async def read_activity_by_id(
    activity_id: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific activity by id.
    """
    activity = await repositories.activity.get(db, id=activity_id)

    return activity

@router.get("/post/{post_id}", response_model=List[schemas.Activity])
async def read_activity_by_post(
    post_id: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific activity by id.
    """
    activity = await repositories.activity.getByPost(db, post_id=post_id)

    return activity

@router.post("/user/", response_model=List[schemas.Activity])
async def read_activity_by_user(
    *,
    db: AsyncSession = Depends(deps.get_db),
    activity_in: schemas.ActivityByUser,
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific activity by id.
    """
    activity = await repositories.activity.getByUser(db, user_id=activity_in.user_id)

    return activity

@router.put("/{activity_id}", response_model=schemas.Activity)
async def update_activity(
    *,
    db: AsyncSession = Depends(deps.get_db),
    activity_id: int,
    activity_in: schemas.ActivityUpdate,
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update an activity.
    """
    activity = await repositories.activity.get(db, id=activity_id)
    if not activity:
        raise HTTPException(
            status_code=404,
            detail="The activity with this ID does not exist in the system",
        )
    activity = await repositories.activity.update(db, db_obj=activity, obj_in=activity_in)
    return activity

@router.delete("/{activity_id}", response_model=schemas.Activity)
async def delete_activity(
    db: AsyncSession = Depends(deps.get_db), *, activity_id: int,
    _: models.Activity = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Delete an activity.
    """
    activity = await repositories.activity.get(db, id=activity_id)
    if not activity:
        raise HTTPException(
            status_code=404,
            detail="The activity with this ID does not exist in the system",
        )
    activity = await repositories.activity.remove(db, id=activity_id)
    return activity