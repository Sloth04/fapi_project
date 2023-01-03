# -*- coding: utf-8 -*-
import ormar
import datetime
from .base import MainMeta
from .writer import Writer
from typing import Optional


class Book(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    writer: Optional[Writer] = ormar.ForeignKey(Writer)
    description: str = ormar.String(max_length=500)
    publish_date = ormar.DateTime(default=datetime.datetime.now())
    rating = ormar.Integer(maximum=10)
    cover_filename: str = ormar.String(max_length=1000)
    genres: str = ormar.String(max_length=1000)
    created_at = ormar.DateTime(default=datetime.datetime.now())
