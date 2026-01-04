from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Dict, List, Optional

class HotspotRequest(BaseModel):
    planets: Dict[str, float] = Field(
        ...,
        description="Planet longitudes in degrees [0,360). Example: {'sun': 75.2, 'moon': 210.1}"
    )
    start_date: Optional[str] = Field(
        None,
        description="Optional ISO date string (reserved for future use)."
    )
    days: int = Field(
        60,
        ge=1,
        le=365,
        description="Forecast horizon in days (MVP uses 60)."
    )

class Hotspot(BaseModel):
    lat: int
    lon: int
    best_day: int
    score: float

class HotspotResponse(BaseModel):
    settings: dict
    top5: List[Hotspot]
