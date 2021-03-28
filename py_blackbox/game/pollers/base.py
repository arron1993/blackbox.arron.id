import threading
import time


class BackgroundEventLoop:
    def __init__(self, fn):
        self.thread = threading.Thread(target=fn)
        self.thread.daemon = True
        self.thread.start()
