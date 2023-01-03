# -*- coding: utf-8 -*-
import ormar
import databases
import sqlalchemy
from helpers import mysql_connection_string

metadata = sqlalchemy.MetaData()
database = databases.Database(mysql_connection_string())
engine = sqlalchemy.create_engine(mysql_connection_string())


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
