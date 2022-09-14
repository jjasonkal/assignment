from typing import Optional

from fastapi import FastAPI

from .routes import weather

app = FastAPI()
app.include_router(weather.router)
