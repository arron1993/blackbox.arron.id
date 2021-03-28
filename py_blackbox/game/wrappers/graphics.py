import mmap

from game.shm.graphic import SPageFileGraphic
from ctypes import sizeof


class GraphicWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
        data = SPageFileGraphic.from_buffer(buf)
        return getattr(data, attr)
