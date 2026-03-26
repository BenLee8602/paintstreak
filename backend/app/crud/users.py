from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.db import db_dep
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    db_user: User = User(**user.model_dump())

    db.add(db_user)
    await db.commit()

    await db.refresh(db_user)
    return db_user


async def read_user(db: AsyncSession, userid: int):
    stmt = select(User).where(User.userid == userid)
    res = await db.execute(stmt)
    return res.scalar_one_or_none()


async def read_users(db: AsyncSession):
    res = await db.execute(select(User))
    return res.scalars().all()


async def update_user(db: AsyncSession, userid: int, user: UserUpdate) -> User:
    db_user: User = await read_user(db, userid)
    if not db_user:
        return None

    for k, v in user.model_dump(exclude_unset=True).items():
        setattr(db_user, k, v)
    await db.commit()

    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, userid: int) -> bool:
    db_user: User = await read_user(db, userid)
    if not db_user:
        return False

    await db.delete(db_user)
    await db.commit()

    return True

