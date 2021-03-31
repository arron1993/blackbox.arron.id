from enum import Enum


class SessionType(Enum):
    UNKNOWN = -1
    PRACTICE = 0
    QUALIFY = 1
    RACE = 2
    HOTLAP = 3
    TIMEATTACK = 4
    DRIFT = 5
    DRAG = 6
    HOTSTINT = 7
    HOTSTINTSUPERPOLE = 8
