from typing import Optional

from pydantic import BaseModel, Field


class Trace(BaseModel):
    event_type: str
    event_title: str
    event_datetime: str
    hydrogen_id: str
    before_hydrogen_id: str
    event_contents: list[str] = Field([])


class GetTracesResponse(BaseModel):
    traces_count: int
    traces: Optional[list[Trace]]
