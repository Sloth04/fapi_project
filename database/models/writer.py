# -*- coding: utf-8 -*-
import ormar
import datetime
import sqlalchemy
from .base import MainMeta


class Writer(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)
    lastname: str = ormar.String(max_length=100)
    created_at: datetime.datetime = ormar.DateTime(default=datetime.datetime.now(), timezone=True,
                                                   server_default=sqlalchemy.text('(CURRENT_TIMESTAMP())'))
