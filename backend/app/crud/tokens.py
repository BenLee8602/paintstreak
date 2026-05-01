from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.token import Token

async def create_token(db: AsyncSession, token: str) -> None:
    db_token: Token = Token(token=token)
    db.add(db_token)
    await db.commit()

async def token_exists(db: AsyncSession, token: str) -> Token | None:
    stmt = select(Token).where(Token.token == token)
    res = await db.execute(stmt)
    return res.scalar_one_or_none()

async def revoke_token(db: AsyncSession, token: str) -> bool:
    db_token: Token = await token_exists(db, token)
    if not db_token:
        return False

    await db.delete(db_token)
    await db.commit()

    return True

