# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, TEXT, TIMESTAMP

from .base import Base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlTimestampsMixin,
)


class Book(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "books"

    title = Column("title", VARCHAR(255))
    writer = Column("writer", VARCHAR(255))
    description = Column("description", TEXT())
    publish_date = Column("publish_date", TIMESTAMP())
    rating = Column("writer", VARCHAR(255))
    cover_filename = Column("cover_filename", VARCHAR(255))
    genres = Column("genres", TEXT())
