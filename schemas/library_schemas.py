from typing import List
from pydantic import BaseModel
from pydantic.schema import Optional, Dict
from datetime import date


class User(BaseModel):
    id: int
    username: str


class Genres(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    description: Optional[str] = ''
    publish_date: Optional[date] = date.today()
    rating: Optional[int] = 0
    cover_filename: str
    genres: Optional[List[Genres]] = []


class GetBook(BaseModel):
    user: User
    book: Book
