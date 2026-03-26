from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.db.db import db_dep
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.models.user import User
import app.crud.users as usercrud

users_router: APIRouter = APIRouter()


@users_router.post("/", response_model=UserRead)
async def create_user(db: db_dep, user: UserCreate):
    # check for duplicate user
    return await usercrud.create_user(db, user)


@users_router.get("/", response_model=list[UserRead])
async def read_users(db: db_dep):
    return await usercrud.read_users(db)


@users_router.get("/{userid}", response_model=UserRead)
async def read_user(db: db_dep, userid: int):
    res = await usercrud.read_user(db, userid)
    if not res:
        raise HTTPException(status_code=404, detail="user not found")
    return res


@users_router.put("/{userid}", response_model=UserRead)
async def update_user(db: db_dep, userid: int, user: UserUpdate):
    res = await usercrud.update_user(db, userid, user)
    if not res:
        raise HTTPException(status_code=404, detail="user not found")
    return res


@users_router.delete("/{userid}")
async def delete_user(db: db_dep, userid: int):
    res: bool = await usercrud.delete_user(db, userid)
    if not res:
        raise HTTPException(status_code=404, detail="user not found")
    return "user deleted"

