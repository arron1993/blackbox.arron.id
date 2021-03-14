import threading
import time

class BackgroundEventLoop:
    def __init__(self, fn, frequency=1):
        self.thread = threading.Thread(target=fn)
        self.thread.start()

    def __del__(self): 
        self.thread.join()