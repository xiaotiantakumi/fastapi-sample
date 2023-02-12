import datetime
from typing import Optional

from pydantic import BaseModel, Field

from api.schemas.condition import Condition


class ChangeBase(BaseModel):
    src_place_id: str
    src_tank_id: str
    dest_place_id: str
    dest_tank_id: str
    new_owner_id: str
    hydrogen_state: Condition = Field(Condition.liquid)
    volume: Optional[float] = Field(0)
    target_hydrogen_id: str
    origin_country: str


class ChangeStart(ChangeBase):
    start_datetime: str = Field(datetime.datetime.now(datetime.timezone.utc).isoformat())


class PostChangeStartResponse(ChangeBase):
    order_id: str
    start_datetime: str


class ChangeEnd(BaseModel):
    end_datetime: str


class PutChangeEndResponse(BaseModel):
    hydrogen_id: str
