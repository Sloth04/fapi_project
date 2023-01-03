from fastapi import FastAPI
from api import library_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello its your app"}


app.include_router(library_router)
