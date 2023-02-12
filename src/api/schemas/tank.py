from pydantic import BaseModel, Field


class Tank(BaseModel):
    tank_name: str
    owner_id: str
    tank_id: str
    place_id: str
    temperature: float = Field(0, description='温度(℃)')
    pressure: float = Field(0, description='圧力(MPa)')
    purity: float = Field(0, description='純度')
    hydrogen_vol: float = Field(0, description='水素量(H2-NM3)')
    tank_vol: float = Field(0, description='タンクの容量(H2-NM3)')


class GetTanksResponse(BaseModel):
    tanks_count: int
    tanks: list[Tank] = Field([])


class TankLog(BaseModel):
    data_datetime: str
    value: float = Field(0)


class GetTankResponse(BaseModel):
    tank_id: str
    volumeLog: list[TankLog] = Field([])
    temperatureLog: list[TankLog] = Field([])
    pressureLog: list[TankLog] = Field([])
