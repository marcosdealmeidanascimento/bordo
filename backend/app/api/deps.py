from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import models, schemas, repositories
from app.core import security
from app.core.config import settings
from app.db.session import engine

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token")


async def get_db() -> Generator:
    async with AsyncSession(engine) as session:
        yield session


async def get_current_user(db: AsyncSession = Depends(get_db),
                           token: str = Depends(reusable_oauth2)
                           ) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[security.ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
        print("------", payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Could not validate credentials")
    user = await repositories.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return user


async def get_current_active_user(current_user: models.User =
                                  Depends(get_current_user)) -> models.User:
    if not repositories.user.is_active(current_user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Inactive user")
    return current_user


async def get_current_active_superuser(current_user: models.User =
                                       Depends(get_current_user)
                                       ) -> models.User:
    return current_user
