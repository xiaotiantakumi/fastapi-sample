import datetime
from pydantic import BaseModel, Field

from api.schemas.condition import Condition


class Certificate(BaseModel):
    hydrogen_id: str
    go_id: str
    condition: Condition
    last_place_id: str
    last_owner_id: str
    volume: float
    emission: float
    emission_rate: float
    certificate_id: str
    origin_country: str = Field('Australia')
    origin_country_alpha_2: str = Field('AU')
    emission_intensity: float


class GetCertificateResponse(Certificate):
    last_place_name: str
    last_owner_name: str
    production_method: str = 'LIGNITE'
    date_of_issue: str = Field(datetime.datetime.now(datetime.timezone.utc).isoformat())
    date_of_use: str = Field(datetime.datetime.now(datetime.timezone.utc).isoformat())
