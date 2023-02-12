from pydantic import BaseModel, Field


class Country(BaseModel):
    name: str
    alpha_2: str
    alpha_3: str
    flag: str
    numeric: str


class GetCountriesResponse(BaseModel):
    countries_count: int
    countries: list[Country] = Field([])
