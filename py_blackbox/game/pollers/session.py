import threading
import time
import datetime

from pprint import pprint

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
        session_type = self.api.get_session_type()
        if session_status != 0:
            # if we're already running, the create the new session
            Event("onNewSession", session_status)

        while True:
            try:
                last_session_status = session_status
                last_session_type = session_type

                session_status = self.api.get_session_status()
                session_type = self.api.get_session_type()
                session_status_change = (
                    last_session_status != session_status and
                    last_session_status == 0)

                # the session can change without quitting
                # e.g. qualifying to race
                session_type_changed = (last_session_type != session_type and
                                        session_type != 0)

                if session_status_change or session_type_changed:
                    Event("onNewSession", session_status)
            except Exception as e:
                pprint(datetime.datetime.now(), "Session Error:", e)
            time.sleep(5)
