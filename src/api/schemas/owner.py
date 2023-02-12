from pydantic import BaseModel, Field


class Owner(BaseModel):
    owner_id: str
    owner_name: str


class GetOwnersResponse(BaseModel):
    owners_count: int
    owners: list[Owner] = Field([])
