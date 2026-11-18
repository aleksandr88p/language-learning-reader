from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from typing import Optional
from app.models.base import Base




class Book(Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[Optional[str]] = mapped_column(String(255))
    language: Mapped[str] = mapped_column(String(10))
    
