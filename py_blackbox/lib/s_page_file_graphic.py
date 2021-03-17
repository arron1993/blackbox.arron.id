from ctypes import Structure, sizeof, c_float, c_int32, c_wchar, c_int, c_double
import mmap


class SPageFileGraphic(Structure):
    _fields_ = [
        ("packetId", c_int),
        ("ACC_STATUS", c_int),
        ("ACC_SESSION_TYPE", c_int),
        ("currentTime", c_wchar * 15),
        ("lastTime", c_wchar * 15),
        ("bestTime", c_wchar * 15),
        ("split", c_wchar * 15),
        ("completedLaps", c_int),
        ("position", c_int),
        ("iCurrentTime", c_int),
        ("iDeltaLapTime", c_int),
        ("iLastTime", c_int),
        ("iBestTime", c_int),
        ("sessionTimeLeft", c_float),
        ("distanceTraveled", c_float),
        ("isInPit", c_int),
        ("currentSectorIndex", c_int),
        ("lastSectorTime", c_int),
        ("numberOfLaps", c_int),
        ("tyreCompound", c_wchar * 33),
        ("replayTimeMultiplier", c_float),
        ("normalizedCarPosition", c_float),

        ("activeCars", c_int),
        ("carCoordinates", c_float * 60 * 3),
        ("carID", c_int * 60),
        ("playerCarID", c_int),
        ("penaltyTime", c_float),
        ("flag", c_int),
        ("penalty", c_int),
        ("idealLineOn", c_int),
        ("isInPitLane", c_int),
        ("isValidLap", c_int),
        ("surfaceGrip", c_float),
        ("mandatoryPitDone", c_int),

        ("windSpeed", c_float),
        ("windDirection", c_float),

        ("isSetupMenuVisible", c_int),

        ("mainDisplayIndex", c_int),
        ("secondaryDisplayIndex", c_int),
        ("TC", c_int),
        ("TCCut", c_int),
        ("EngineMap", c_int),
        ("ABS", c_int),
        ("fuelXLap", c_float),
        ("rainLights", c_int),
        ("flashingLights", c_int),
        ("lightsStage", c_int),
        ("exhaustTemperature", c_float),
        ("wiperLV", c_int),
        ("DriverStintTotalTimeLeft", c_int),
        ("DriverStintTimeLeft", c_int),
        ("rainTypes", c_int),
    ]

    def toDict(self):
        return {
            "bestTime": self.bestTime,
            "iBestTime": self.iBestTime,
            "lastTime": self.lastTime,
            "iLastTime": self.iLastTime,
            "sessionTimeLeft": self.sessionTimeLeft,
            "estLapsLeft": self.sessionTimeLeft / (self.iLastTime+1),
            "fuelXLap": self.fuelXLap,
            "numberOfLaps": self.numberOfLaps
        }
