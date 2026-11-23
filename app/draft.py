from sqlalchemy.orm import configure_mappers
from app.models.book import Book
from app.models.chapter import Chapter



configure_mappers()
print("ORM relationships OK")


print(Book.chapters.property.uselist)
print(Chapter.book.property.uselist)
