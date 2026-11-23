from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from typing import Optional
from app.models.base import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.models.chapter import Chapter


class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[Optional[str]] = mapped_column(String(255))
    language: Mapped[str] = mapped_column(String(10))
    chapters: Mapped[list['Chapter']] = relationship(back_populates="book")
    
