import uvicorn
from fastapi import FastAPI
from api import library_router
from database.models.base import database, metadata, engine

app = FastAPI()
metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello its your app"}


app.include_router(library_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, log_level="debug")
