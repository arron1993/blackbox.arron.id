from ctypes import sizeof

from lib.s_page_file_physics import SPageFilePhysics
from lib.s_page_file_static import SPageFileStatic
from lib.s_page_file_graphic import SPageFileGraphic

import time
import mmap

def read_physics():
	buf = mmap.mmap(-1, sizeof(SPageFilePhysics), u"Local\\acpmf_physics")
	data = SPageFilePhysics.from_buffer(buf)
	return data.__dict__()

def read_static():
	buf = mmap.mmap(-1, sizeof(SPageFileStatic), u"Local\\acpmf_static")
	data = SPageFileStatic.from_buffer(buf)
	return data.toDict()

def read_graphics():
	buf = mmap.mmap(-1, sizeof(SPageFileGraphic), u"Local\\acpmf_graphics")
	data = SPageFileGraphic.from_buffer(buf)
	return data.toDict()

while True:
	print(time.time(), read_graphics())
	print(read_graphics())
	print(read_static())
	time.sleep(1)
# print(read_static())
#print(read_graphics())