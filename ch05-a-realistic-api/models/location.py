from pydantic import BaseModel
from typing_extensions import Optional


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = "US"
