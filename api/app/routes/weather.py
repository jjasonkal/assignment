from fastapi import APIRouter, HTTPException

from .. import db
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


@router.get("/last-hour-weekly-forecast")
async def get_last_hour_weekly_forecast(test=False) -> Weather:
    weather = db.last_hour_weekly_forecast(test)

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather


@router.get("/average-of-last-3-forecasts")
async def get_average_of_last_3_forecasts() -> Weather:
    weather = db.average_of_last_3_forecasts()

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather


@router.get("/top-n-locations-of-each-metric")
async def get_top_n_locations_of_each_metric(n: int) -> Weather:
    weather = db.top_n_locations_of_each_metric(n)

    if not weather:
        raise HTTPException(status_code=404, detail="Item not found")

    return weather