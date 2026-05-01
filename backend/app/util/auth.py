import os
from typing import Annotated
from datetime import datetime, timezone, timedelta
import bcrypt
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer


def hash_pw(pw: str) -> str:
    pw_bytes: bytes = pw.encode("utf-8")
    pw_salt: bytes = bcrypt.gensalt()
    pw_hash: bytes = bcrypt.hashpw(pw_bytes, pw_salt)
    return pw_hash.decode("utf-8")

def check_pw(pw: str, pw_hash: str) -> bool:
    pw_bytes: bytes = pw.encode("utf-8")
    pw_hash_bytes: bytes = pw_hash.encode("utf-8")
    return bcrypt.checkpw(pw_bytes, pw_hash_bytes)


def create_refresh_token(user: str) -> str:
    payload: dict = {
        "sub": user,
        "exp": datetime.now(timezone.utc) + timedelta(days=90)
    }
    secret: str = os.environ["REFRESH_TOKEN_SECRET"]
    return jwt.encode(payload, secret, algorithm="HS256")

def create_access_token(user: str) -> str:
    payload: dict = {
        "sub": user,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=15)
    }
    secret: str = os.environ["ACCESS_TOKEN_SECRET"]
    return jwt.encode(payload, secret, algorithm="HS256")


def _verify_token(token: str, secret: str) -> str | None:
    try:
        payload: dict = jwt.decode(token, secret, algorithms=["HS256"])
        return payload["sub"]
    except jwt.PyJWTError:
        return None

def verify_refresh_token(token: str) -> str | None:
    secret: str = os.environ["REFRESH_TOKEN_SECRET"]
    return _verify_token(token, secret)

def verify_access_token(token: str) -> str | None:
    secret: str = os.environ["ACCESS_TOKEN_SECRET"]
    return _verify_token(token, secret)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def _login_opt(token: str = Depends(oauth2_scheme)) -> str | None:
    return verify_access_token(token) if token else None

def _login_req(user: str = Depends(_login_opt)) -> str:
    if user:
        return user
    raise HTTPException(
        status_code=401,
        detail="missing or invalid access token"
    )

login_opt = Annotated[str | None, Depends(_login_opt)]
login_req = Annotated[str, Depends(_login_req)]

