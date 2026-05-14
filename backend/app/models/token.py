from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Token(Base):
    __tablename__: str = "tokens"
    
    token: Mapped[str] = mapped_column(
        String,
        primary_key=True)
    userid: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.userid", ondelete="CASCADE"),
        nullable=False)
    expires: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False)

