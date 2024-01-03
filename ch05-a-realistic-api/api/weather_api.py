import fastapi

from fastapi import Depends
from models.location import Location
from typing_extensions import Optional

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    return f"{loc.city},  {loc.state},  {loc.country},  {units}"
