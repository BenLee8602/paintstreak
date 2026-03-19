from fastapi import APIRouter
from sqlalchemy import select
from app.db.db import db_dep
from app.models.user import User

users_router: APIRouter = APIRouter()


@users_router.get("/")
async def read_users(db: db_dep):
    result = await db.execute(select(User))
    return result.scalars().all()


@users_router.get("/{name}")
async def read_users(name: str, db: db_dep):
    stmt = select(User).where(User.username == name)
    result = await db.execute(stmt)
    return result.scalar_one()

