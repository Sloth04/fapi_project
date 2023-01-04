from typing import List
from pydantic import BaseModel
from pydantic.schema import Optional, Dict
from datetime import date


class User(BaseModel):
    id: int
    username: str


class Genres(BaseModel):
    name: str