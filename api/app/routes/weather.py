from typing import List

from fastapi import APIRouter, HTTPException

from ..lib import db
from ..models.weather import Weather

router = APIRouter(
    prefix="/weather",
    tags=["weather"]
)


@router.get("/latest-weekly-forecast")
async def get_latest_weekly_forecast() -> Weather:
    weather = db.latest_weekly_forecast()

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather


@router.get("/average-of-last-3-forecasts")
async def average_of_last_3_forecasts() -> Weather:
    weather = db.average_of_last_3_forecasts()

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather


@router.get("/top-n-locations-of-each-metric")
async def top_n_locations_of_each_metric(n: int) -> Weather:
    weather = db.top_n_locations_of_each_metric(n)

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather