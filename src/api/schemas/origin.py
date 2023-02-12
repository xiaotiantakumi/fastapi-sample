from pydantic import BaseModel, Field


class Origin(BaseModel):
    order_id: str
    origin_country: str = Field('')
    volume: float = Field(0)
    emission: float = Field(0)
    go_file_path: str = Field('')
