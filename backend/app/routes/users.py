from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.db.db import db_dep
from app.schemas.user import UserCreate, UserRead, UserUpdate, Token
import app.crud.users as usercrud
import app.crud.tokens as tokencrud
import app.util.auth as auth


users_router: APIRouter = APIRouter()


@users_router.post("/register", response_model=str)
async def register(db: db_dep, user: UserCreate):
    if await usercrud.read_user_name(db, user.username):
        raise HTTPException(status_code=409, detail="user exists")

    user.password = auth.hash_pw(user.password)
    db_user: User = await usercrud.create_user(db, user)

    token: str = auth.create_refresh_token(db_user.userid)
    await tokencrud.create_token(db, token)

    return token


@users_router.post("/login", response_model=str)
async def login(db: db_dep, cred: UserCreate):
    user: User = await usercrud.read_user_name(db, cred.username)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")

    if not auth.check_pw(cred.password, user.password):
        raise HTTPException(status_code=401, detail="incorrect password")

    token: str = auth.create_refresh_token(user.userid)
    await tokencrud.create_token(db, token)

    return token


@users_router.put("/whoami", response_model=UserRead)
async def whoami(db: db_dep, user: auth.login_req):
    db_user: User | None = await usercrud.read_user_id(db, user)
    if not db_user:
        raise HTTPException(status_code=401, detail="user not found")
    return db_user


@users_router.put("/refresh", response_model=str)
async def refresh(db: db_dep, rt: Token):
    user: int | None = auth.verify_refresh_token(rt.token)
    db_token: bool = await tokencrud.token_exists(db, rt.token)
    if not user or not db_token:
        raise HTTPException(status_code=401, detail="invalid token")
    return auth.create_access_token(user)



@users_router.delete("/logout", response_model=str)
async def logout(db: db_dep, rt: Token):
    if not await tokencrud.revoke_token(db, rt.token):
        raise HTTPException(status_code=404, detail="token not found")
    return "logged out"


@users_router.get("/", response_model=list[UserRead])
async def read_users(db: db_dep):
    return await usercrud.read_users(db)


@users_router.get("/{userid}", response_model=UserRead)
async def read_user(db: db_dep, userid: int):
    res = await usercrud.read_user_id(db, userid)
    if not res:
        raise HTTPException(status_code=404, detail="user not found")
    return res


@users_router.put("/", response_model=UserRead)
async def edit_user(db: db_dep, user: auth.login_req, data: UserUpdate):
    if data.username and await usercrud.read_user_name(db, data.username):
        raise HTTPException(status_code=409, detail="user exists")

    res: User | None = await usercrud.update_user(db, user, data)
    if not res:
        raise HTTPException(status_code=404, detail="user not found")
    return res


@users_router.delete("/")
async def delete_user(db: db_dep, user: auth.login_req):
    if not await usercrud.delete_user(db, user):
        raise HTTPException(status_code=404, detail="user not found")
    return { "ok": True }

