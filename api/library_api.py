import datetime
from typing import Union, Optional
from database.models import Book
from fastapi import APIRouter, UploadFile, File, Form, Request, BackgroundTasks, HTTPException
from services import save_book

library_router = APIRouter()


@library_router.get("/book/{book_pk}")
async def get_book(book_pk: int):
    return await Book.objects.select_related('writer').get(pk=book_pk)


@library_router.post("/book", response_model=Book)
async def create_book_with_cover(background_tasks: BackgroundTasks,
                                 title: str = Form(...),
                                 writer_id: Optional[int] = Form(default=None),
                                 description: Union[str, None] = Form(default=None),
                                 publish_date: datetime.date = Form(default=datetime.date.today()),
                                 rating: Optional[int] = Form(default=None),
                                 cover_filename: Optional[str] = Form(default=None),
                                 genre: Optional[str] = Form(default=None),
                                 cover_file: Optional[UploadFile] = File(default=None),
                                 book_file: UploadFile = File(...)
                                 ):
    """ Add book """
    return await save_book(title, writer_id, description, publish_date, rating, genre, cover_filename, cover_file,
                           book_file, background_tasks)


@library_router.get("/test")
async def get_test(req: Request):
    print(req.base_url)
    return {}
