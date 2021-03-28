import threading
import time

from game.api import GameApi
from observer.event import Event


class SessionPoller():
    def __init__(self):
        self.api = GameApi()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        session_status = self.api.get_session_status()
        if session_status != 0:
            # if we're already running, the create the new session
            Event("onNewSession", session_status)

        while True:
            last_session_status = session_status
            session_status = self.api.get_session_status()
            if (last_session_status != session_status and
                    last_session_status == 0):
                Event("onNewSession", session_status)
            time.sleep(1)
