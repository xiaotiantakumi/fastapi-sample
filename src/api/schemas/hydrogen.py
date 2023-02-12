from pydantic import BaseModel, Field


class Hydrogen(BaseModel):
    hydrogen_id: str
    condition: str
    tank_id: str
    owner_id: str
    volume: float
    emission: float
    before_hydrogen_id: str
    go_id: str
    origin_country: str = Field('')
    origin_country_alpha_2: str = Field('')
    order_id: str = Field('')
    order_content: str = Field('default')
    go_file_name: str = Field('')
    valid_flag: int = Field(1)
    unknown_flag: int = Field(0)
    emission_intensity: float = Field(0)


class GetHydrogensResponse(BaseModel):
    hydrogens_count: int
    hydrogens: list[Hydrogen]
    tank_vol: float = Field(100000)


class GetHydrogenDetailResponse(Hydrogen):
    place_id: str
    place_name: str
    tank_name: str
