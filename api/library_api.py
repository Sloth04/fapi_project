import shutil
from typing import Optional
from schemas import GetBook, User
from database.models import Book
from fastapi import APIRouter, UploadFile, File, Form, Request

library_router = APIRouter()


@library_router.get("/book", response_model=GetBook)
async def get_book():
    user = {'id': 225, 'username': 'Sloth'}
    book = {'title': 'TestTitle1', 'writer': 'TestWriter1'}
    return GetBook(user=user, book=book)


@library_router.post("/book", response_model=Book)
async def create_book(book: Book):
    await book.save()
    return book


@library_router.post("/book+cover")
async def create_book_with_cover(title: str = Form(...),
                                 writer: str = Form(...),
                                 description: Optional[str] = Form(None),
                                 publish_date: Optional[str] = Form(None),
                                 rating: Optional[int] = Form(None),
                                 cover_filename: Optional[str] = Form(None),
                                 file: UploadFile = File(...)):
    if cover_filename is None:
        cover_filename = file.filename
    else:
        file.filename = cover_filename
    book_item = Book(title=title,
                     writer=writer,
                     description=description,
                     publish_date=publish_date,
                     rating=rating,
                     cover_filename=cover_filename)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"book_item": book_item}


@library_router.get("/test")
async def get_test(req: Request):
    print(req.base_url)
    return {}
