import time
import threading
import datetime

from observer.event import Event
from game.api import GameApi
from game.models.session_status import SessionStatus


class StintPoller():
    def __init__(self):
        self.api = GameApi()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        is_in_pitlane = self.api.get_is_in_pitlane()
        session_type = self.api.get_session_type()

        while True:
            try:
                last_session_type = session_type
                session_type = self.api.get_session_type()
                session_type_changed = (last_session_type != session_type)

                # if a session is running, and the type hasn't changed
                # start a new stint
                # a new stint can be wrongly created if we're in
                # the pitlane when
                # when a session(qualifying) ends and we're teleported
                # to the formation lap
                if (self.api.get_session_status() != SessionStatus.OFF.value and
                        not session_type_changed):
                    was_in_pitlane = is_in_pitlane
                    is_in_pitlane = self.api.get_is_in_pitlane()
                    if was_in_pitlane == 1 and is_in_pitlane == 0:
                        # was in the pitlane but has now left
                        Event("onNewStint")
            except Exception as e:
                print(datetime.datetime.now(), "Stint Error", e)
            time.sleep(5)
