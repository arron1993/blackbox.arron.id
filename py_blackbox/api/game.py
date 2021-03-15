from lib.s_page_file_graphic import SPageFileGraphic
from lib.s_page_file_static import SPageFileStatic
from ctypes import sizeof
import mmap

SESSION_TYPE_MAP = {
    "-1": "Unknown",
    "0": "Practice",
    "1": "Qualifying",
    "2": "Race",
    "3": "Hotlap",
    "4": "Time Attack",
    "5": "Drift",
    "6": "Drag",
    "7": "Hot Stint",
    "8": "Super Pole",
}

class GraphicWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
        data = SPageFileGraphic.from_buffer(buf)
        return getattr(data, attr)


class StaticWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFileStatic), u"Local\\acpmf_static")
        data = SPageFileStatic.from_buffer(buf)
        return getattr(data, attr)


class GameApi():
    def __init__(self):
        self.graphic = GraphicWrapper()
        self.static = StaticWrapper()

    def get_session_status(self):
        return self.graphic.ACC_STATUS

    def get_number_of_laps(self):
        return self.graphic.completedLaps

    def get_session_details(self):
        return {
            "type": SESSION_TYPE_MAP[
                str(self.graphic.ACC_SESSION_TYPE)],
            "car": self.static.carModel,
            # # silverstone is "Silverstone" can't be doing with that
            "circuit": self.static.track.lower()
        }

    def get_last_lap_details(self):
        return {
            "number": self.graphic.completedLaps,
            "time": self.graphic.iLastTime,
        }
