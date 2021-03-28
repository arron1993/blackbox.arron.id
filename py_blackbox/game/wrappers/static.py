import mmap

from game.shm.static import SPageFileStatic
from ctypes import sizeof


class StaticWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFileStatic), u"Local\\acpmf_static")
        data = SPageFileStatic.from_buffer(buf)
        return getattr(data, attr)
