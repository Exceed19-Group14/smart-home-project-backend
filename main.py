from fastapi import FastAPI
from routes.room import router as RoomRouter


app = FastAPI()


app.include_router(RoomRouter)
