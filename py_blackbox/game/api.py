from game.wrappers.graphics import GraphicWrapper
from game.wrappers.static import StaticWrapper


class GameApi():
    def __init__(self):
        self.graphic = GraphicWrapper()
        self.static = StaticWrapper()

    def get_session_status(self):
        return self.graphic.ACC_STATUS

    def get_number_of_laps(self):
        return self.graphic.completedLaps

    def get_last_lap_time(self):
        return self.graphic.iLastTime

    def get_session_type(self):
        return self.graphic.ACC_SESSION_TYPE

    def get_number_of_cars(self):
        return self.static.numCars

    def get_session_details(self):
        return {
            "session_type": self.graphic.ACC_SESSION_TYPE,
            "car": self.static.carModel,
            # # silverstone is "Silverstone" can't be doing with that
            "circuit": self.static.track.lower(),
            "session_length": self.graphic.sessionTimeLeft
        }

    def get_last_lap_details(self):
        return {
            "number": self.graphic.completedLaps,
            "time": self.graphic.iLastTime,
            "fuel_used": self.graphic.fuelXLap,
            "position": self.graphic.position,
            "delta_time": self.graphic.iDeltaLapTime,
            "is_valid": self.graphic.isValidLap,
            "num_cars": self.static.numCars,
        }

    def get_is_in_pitlane(self):
        return self.graphic.isInPitLane

    def get_last_sector_time(self):
        return self.graphic.lastSectorTime

    def get_current_sector(self):
        return self.graphic.currentSectorIndex

    def get_completed_laps(self):
        return self.graphic.completedLaps

    def get_split(self):
        return self.graphic.split
