import mmap

from game.shm.physics import SPageFilePhysics
from ctypes import sizeof


class PhysicsWrapper:
    def __getattr__(self, attr):
        buf = mmap.mmap(-1, sizeof(SPageFilePhysics), u"Local\\acpmf_physic")
        data = SPageFilePhysics.from_buffer(buf)
        return getattr(data, attr)
