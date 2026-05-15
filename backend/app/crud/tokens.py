from datetime import datetime, timezone, timedelta
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.token import Token
import app.util.auth as auth


async def create_token(db: AsyncSession, user: int) -> str:
    token: str = auth.create_refresh_token()
    db_token: Token = Token(
        token=auth.hash_refresh_token(token),
        userid=user,
        expires=datetime.now(timezone.utc) + timedelta(days=30)
    )
    db.add(db_token)
    await db.commit()
    return token


async def token_exists(db: AsyncSession, token: str) -> Token | None:
    stmt = select(Token).where(
        Token.token == auth.hash_refresh_token(token),
        Token.expires > datetime.now(timezone.utc)
    )
    res = await db.execute(stmt)
    return res.scalar_one_or_none()


async def revoke_token(db: AsyncSession, token: str) -> bool:
    db_token: Token = await token_exists(db, token)
    if not db_token:
        return False

    await db.delete(db_token)
    await db.commit()

    return True

