from enum import Enum


class PlaceType(str, Enum):
    Ship = 'Ship'
    Base = 'Base'
    Track = 'Track'
    PipeLine = 'PipeLine'
