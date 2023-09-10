from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.Logbook])
async def read_logbooks(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Logbook = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve logbooks.
    """
    logbooks = await repositories.logbook.get_multi(db, skip=skip, limit=limit)
    return logbooks


@router.post("/", response_model=schemas.Logbook)
async def create_logbook(
    *,
    db: AsyncSession = Depends(deps.get_db),
    logbook_in: schemas.LogbookCreate,
    _: models.Logbook = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new logbook.
    """
    logbook = await repositories.logbook.get_by_name(db, name=logbook_in.name, user_id=logbook_in.user_id)
    if logbook:
        raise HTTPException(
            status_code=400,
            detail="The logbook with this name already exists in the system.",
        )
    logbook = await repositories.logbook.create(db, obj_in=logbook_in)
    return logbook



@router.get("/{id}", response_model=schemas.Logbook)
async def read_logbook_by_id(
    logbook_id: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.Logbook = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific logbook by id.
    """
    logbook = await repositories.logbook.get(db, id=logbook_id)

    return logbook


@router.put("/{id}", response_model=schemas.Logbook)
async def update_logbook(
    *,
    db: AsyncSession = Depends(deps.get_db),
    logbook_id: int,
    logbook_in: schemas.LogbookUpdate,
    _: models.Logbook = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a logbook.
    """
    logbook = await repositories.logbook.get_by_name(db, name=logbook_in.name, user_id=logbook_in.user_id)
    if logbook:
        raise HTTPException(
            status_code=400,
            detail="The logbook with this name already exists in the system.",
        )
    
    logbook = await repositories.logbook.get(db, id=logbook_id)
    if not logbook:
        raise HTTPException(
            status_code=404,
            detail="The logbook with this id does not exist in the system",
        )
    logbook = await repositories.logbook.update(db, db_obj=logbook, obj_in=logbook_in)
    return logbook



@router.delete("/{id}", response_model=schemas.Logbook)
async def delete_logbook(
    db: AsyncSession = Depends(deps.get_db), *, id: int,
) -> Any:
    
    logbook = await repositories.logbook.get(db, id=id)
    if not logbook:
        raise HTTPException(
            status_code=404,
            detail="A logbook with this id does not exists",
        )
    logbook = await repositories.logbook.remove(db=db, id=id)
    return logbook
