from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from db.engine import Base

class PackagingType(StrEnum):
    IN_PACKAGE = auto()
    WEIGHT = auto()


class DBCheeseType(Base):
    __tablename__ = "cheese_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(255), nullable=False)


class DBCheese(Base):
    __tablename__ = "cheese"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    price = Column(Integer, nullable=False)
    packaging_type = Column(Enum(PackagingType), nullable=False)
    cheese_type_id = Column(Integer, ForeignKey("cheese_type.id"))

    cheese_type = relationship(DBCheeseType)




# class DBAuthor(Base):
#     __tablename__ = "author"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(255), nullable=False, unique=True)
#     bio = Column(String(255), nullable=False)
#
#     # Один автор может иметь много книг
#     books = relationship("DBBook", back_populates="author")
#
# class DBBook(Base):
#     __tablename__ = "book"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), nullable=False)
#     summary = Column(String(255), nullable=False)
#     packaging_type = Column(DATE, nullable=False)
#     author_id = Column(Integer, ForeignKey("author.id"))
#
#     # Каждая книга связана с одним автором
#     author = relationship("DBAuthor", back_populates="books")