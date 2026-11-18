from app.models.base import Base
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional




class Chapter(Base):
    __tablename__ = "chapters"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey('books.id'))
    title: Mapped[Optional[str]] = mapped_column(String(255))
    position: Mapped[int] = mapped_column(Integer, nullable=False)





