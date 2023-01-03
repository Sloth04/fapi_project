# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR

from .base import Base
from .mixins import (
    MysqlPrimaryKeyMixin,
    MysqlTimestampsMixin,
)


class User(Base, MysqlPrimaryKeyMixin, MysqlTimestampsMixin):
    __tablename__ = "users"

    username = Column("username", VARCHAR(255))
