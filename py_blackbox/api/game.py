from lib.s_page_file_graphic import SPageFileGraphic
from ctypes import sizeof
import mmap


class GraphicWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
        data = SPageFileGraphic.from_buffer(buf)
        return getattr(data, attr)


class GameApi():
    def __init__(self):
        self.graphic = GraphicWrapper()

    def get_session_status(self):
        return self.graphic.AC_STATUS

    def get_number_of_laps(self):
        return self.graphic.completedLaps
