# -*- coding: utf-8 -*-
import ormar
import sqlalchemy
import datetime
from .base import MainMeta
from .writer import Writer
from typing import Optional, Union


class Book(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    writer_id: Union[Writer, int, None] = ormar.ForeignKey(Writer)
    description: str = ormar.String(max_length=500, nullable=True)
    publish_date: datetime.date = ormar.Date(default=datetime.date.today(), timezone=True,
                                             server_default=sqlalchemy.text('(CURRENT_DATE())'))
    rating: int = ormar.Integer(maximum=10)
    cover_file: str = ormar.String(max_length=1000, nullable=True)
    book_file: str = ormar.String(max_length=1000, nullable=True)
    genre: str = ormar.String(max_length=100, nullable=True)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now(), timezone=True,
                                                   server_default=sqlalchemy.text('(CURRENT_TIMESTAMP())'))
