import datetime
from typing import Optional

from pydantic import BaseModel, Field

from api.schemas.condition import Condition


class OrderBase(BaseModel):
    dest_place_id: str
    dest_tank_id: str
    new_owner_id: str
    hydrogen_state: Condition = Field(Condition.liquid)
    origin_country: str
    emission: Optional[float] = Field(0)
    volume: Optional[float] = Field(0)


class OrderStart(OrderBase):
    go_file_name: str = Field('')
    start_datetime: str = Field(datetime.datetime.now(datetime.timezone.utc).isoformat())


class PostOrderStartResponse(OrderBase):
    order_id: str
    start_datetime: str


class GetOrderResponse(OrderBase):
    order_id: str
    start_datetime: str
    user_id: str
    order_content: str
    target_hydrogen_id: str
    end_datetime: str
    go_file_path: str
    go_id: str
    authorizer_id: str
    dest_place_name: str = Field('')
    dest_tank_name: str = Field('')
    new_owner_name: str = Field('')
    src_place_id: str
    src_place_name: str = Field('')
    src_tank_id: str
    src_tank_name: str = Field('')
    origin_country: str = Field('Australia')
    origin_country_alpha_2: str = Field('AU')


class OrderEnd(BaseModel):
    end_datetime: str


class PutOrderEndResponse(BaseModel):
    hydrogen_id: str
