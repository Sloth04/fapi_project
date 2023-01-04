# import aiofiles
import datetime
import shutil
from database.models import Book
from fastapi import UploadFile, BackgroundTasks, HTTPException


async def save_book(
        title: str,
        writer_id: int,
        description: str,
        publish_date: datetime.date,
        rating: int,
        genre: str,
        cover_filename: str,
        cover_file: UploadFile,
        book_file: UploadFile,
        background_tasks: BackgroundTasks):

    if cover_filename is None:
        cover_filename = f'media/covers/{cover_file.filename}'
        cover_file.filename = cover_filename
    else:
        cover_file.filename = f'media/covers/{cover_filename}'

    if cover_file.content_type == 'image/png' or cover_file.content_type == 'image/jpeg':
        background_tasks.add_task(write_item, cover_file)
    else:
        raise HTTPException(status_code=418, detail="Unsupported format, must be .jpg or .png")

    if book_file.content_type == 'application/epub+zip' or book_file.content_type == 'text/plain':
        book_file.filename = f'media/books/{book_file.filename}'
        background_tasks.add_task(write_item, book_file)
    else:
        raise HTTPException(status_code=418, detail="Unsupported format, must be .epub or .txt")

    return await Book.objects.create(title=title,
                                     writer_id=writer_id,
                                     description=description,
                                     publish_date=publish_date,
                                     rating=rating,
                                     cover_file=cover_file.filename,
                                     book_file=book_file.filename,
                                     genre=genre)


def write_item(file: UploadFile):
    # async with aiofiles.open(file_name, "wb") as buffer:
    #     data = await file.read()
    #     await buffer.write(data)
    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
