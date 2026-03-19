import os
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from fastapi import Depends

DB_URL: str = os.environ.get(
    "DB_URL",
    "postgresql+asyncpg://user:pass@db:5432/paintstreakdb"
)

engine = create_async_engine(DB_URL, echo=True)

async def get_db():
    async with AsyncSession(engine) as session:
        yield session

db_dep = Annotated[AsyncSession, Depends(get_db)]

