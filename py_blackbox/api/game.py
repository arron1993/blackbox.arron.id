from lib.s_page_file_graphic import SPageFileGraphic
from lib.s_page_file_static import SPageFileStatic
from ctypes import sizeof
import mmap


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
        return self.graphic.AC_STATUS

    def get_number_of_laps(self):
        return self.graphic.completedLaps

    def get_session_details(self):
        return {
            "type": self.graphic.ACC_SESSION_TYPE,
            "car": self.static.carModel,
            "circuit": self.static.track
        }