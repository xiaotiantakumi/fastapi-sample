from typing import Optional

from pydantic import BaseModel, Field

from api.schemas.place_type import PlaceType


class Place(BaseModel):
    place_id: str
    place_name: str
    place_type: PlaceType
    owner_id: str
    place_no: Optional[str] = Field('')
    latitude: Optional[float] = Field(0, ge=-90.0, le=90.0, description='緯度')
    longitude: Optional[float] = Field(0, ge=0.0, le=180.0, description='経度')
    direction: Optional[float] = Field(0, ge=0, lt=360, description='進行方向')
    total_tank_vol: Optional[float] = Field(0, description='全てのタンクの容量の合計')
    total_hydrogen_vol: Optional[float] = Field(
        0, description='全てのタンクに入っている水素量の合計')
    status: Optional[str] = Field('', description='foward/shipping/anchorage')


class Location(BaseModel):
    latitude: float = Field(0, ge=-90.0, le=90.0, description='緯度')
    longitude: float = Field(0, ge=0.0, le=180.0, description='経度')


class PlaceDetail(BaseModel):
    departure_place: str
    destination_place: str
    destination_place_latlon: Location = Field(Location(latitude=0, longitude=0))
    departure_time: str
    arrival_time: str
    speed: float = Field(0)
    area: str = Field('-', description='航海中のエリア、どう設定するかは未定')
    latlons: list[Location] = Field([], description='軌跡のリスト')
    place_id: str


class GetPlacesResponse(BaseModel):
    places_count: int
    places: list[Place] = Field([])


class GetPlaceDetailResponse(PlaceDetail):
    departure_place_alpha_2: str = Field('')
    destination_place_alpha_2: str = Field('')
