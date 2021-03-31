from enum import Enum


class SessionStatus(Enum):
    OFF = 0
    REPLAY = 1
    LIVE = 2
    PAUSE = 3
