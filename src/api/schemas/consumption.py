import datetime
from typing import Optional

from pydantic import BaseModel, Field

from api.schemas.condition import Condition


class ConsumptionBase(BaseModel):
    src_place_id: str
    src_tank_id: str
    dest_place_id: str
    dest_tank_id: str
    new_owner_id: str
    hydrogen_state: Condition = Field(Condition.liquid)
    volume: Optional[float] = Field(0)
    target_hydrogen_id: str
    origin_country: str


class ConsumptionStart(ConsumptionBase):
    start_datetime: str = Field(datetime.datetime.now(datetime.timezone.utc).isoformat())


class PostConsumptionStartResponse(ConsumptionBase):
    order_id: str
    start_datetime: str


class ConsumptionEnd(BaseModel):
    end_datetime: str


class PutConsumptionEndResponse(BaseModel):
    hydrogen_ids: list[str] = Field([])
    certificate_id: str
