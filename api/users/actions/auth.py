from typing import Union
from jose import jwt
from jose import JWTError
from hashing import Hasher
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from fastapi import status

import settings

from db.dals import UserDAL
from db.models import User
from db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def _get_user_by_email_for_auth(email: str, db: AsyncSession):
    user_dal = UserDAL(db)
    return await user_dal.get_user_by_email(email=email)



async def authenticate_user(
    email: str, password: str, db: AsyncSession
) -> Union[User, None]:
    user = await _get_user_by_email_for_auth(email=email, db=db)
    if user is None:
        return None
    if not Hasher.verify_password(password, user.hashed_password):
        return None
    # Добавляем явное зафиксирование транзакции
    await db.commit()
    return user



async def get_current_user_from_token(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        print("username/email extracted is ", email)
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await _get_user_by_email_for_auth(email=email, db=db)
    if user is None:
        raise credentials_exception
    return user
