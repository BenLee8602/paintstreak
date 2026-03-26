from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class User(Base):
    __tablename__: str = "users"

    userid: Mapped[int] = mapped_column(
        Integer,
        primary_key=True)
    username: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True)
    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False)

