import fastapi

from fastapi import Depends
from typing_extensions import Optional

from models.location import Location
from services import open_weather_service

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    report = open_weather_service.get_report(loc.city,
                                             loc.state,
                                             loc.country,
                                             units)
    return report
