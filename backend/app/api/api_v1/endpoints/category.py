from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import repositories, models, schemas
from app.api import deps
from app.core.config import settings

router = APIRouter()


@router.get("/", response_model=List[schemas.Category])
async def read_categories(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    _: models.Category = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve categories.
    """
    categories = await repositories.category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.post("/", response_model=schemas.Category)
async def create_category(
    *,
    db: AsyncSession = Depends(deps.get_db),
    category_in: schemas.CategoryCreate,
    _: models.Category = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new category.
    """
    category = await repositories.category.get_by_name(db, name=category_in.name)
    if category:
        raise HTTPException(
            status_code=400,
            detail="The category with this username already exists in the system.",
        )
    category = await repositories.category.create(db, obj_in=category_in)
    return category



@router.get("/{id}", response_model=schemas.Category)
async def read_user_by_id(
    category_id: int,
    db: AsyncSession = Depends(deps.get_db),
    _: models.Category = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get a specific category by id.
    """
    category = await repositories.category.get(db, id=category_id)

    return category


@router.put("/{id}", response_model=schemas.Category)
async def update_category(
    *,
    db: AsyncSession = Depends(deps.get_db),
    category_id: int,
    category_in: schemas.CategoryUpdate,
    _: models.Category = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a category.
    """
    category = await repositories.category.get(db, id=category_id)
    if not category:
        raise HTTPException(
            status_code=404,
            detail="The category with this id does not exist in the system",
        )
    category = await repositories.category.update(db, db_obj=category, obj_in=category_in)
    return category



@router.delete("/{id}", response_model=schemas.Category)
async def delete_category(
    db: AsyncSession = Depends(deps.get_db), *, id: int,
) -> Any:

    category = await repositories.category.remove(db=db, id=id)
    return category
