from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class Token(Base):
    __tablename__: str = "tokens"
    
    token: Mapped[str] = mapped_column(
        String,
        primary_key=True)

