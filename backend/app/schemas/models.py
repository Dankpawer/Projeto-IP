from pydantic import BaseModel
from typing import List, Optional

class GeolocationData(BaseModel):
    city: str
    region: str
    country: str

class GeolocationResponse(BaseModel):
    type: str = "ip_geolocation"
    status: str
    source: str
    data: Optional[GeolocationData] = None
    accuracy: str
    stored: bool = False

class Source(BaseModel):
    type: str
    content: str

class Conclusion(BaseModel):
    text: str
    confidence: str
    limitations: List[str]

class Scenario(BaseModel):
    scenario_id: str
    profile: str
    sources: List[Source]
    conclusion: Conclusion
