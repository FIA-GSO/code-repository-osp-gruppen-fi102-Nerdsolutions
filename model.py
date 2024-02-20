from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum


class Base(DeclarativeBase):
    pass


DB_FILE = 'test.sqlite'
DB_CONN = 'sqlite:///' + DB_FILE


class Box(Base):
    __tablename__ = 'box'
    guid: Uuid = Column(
        Uuid,
        primary_key=True,
        nullable=False,
        default=lambda: uuid.uuid4())
    location = Column(Enum(Location))


class Article(Base):



class Location(enum.Enum):
    HOME = 1
    TRANSPORT = 2
    DEPLOYMENT = 3
