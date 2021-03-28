import time
import threading

from observer.event import Event
from game.api import GameApi


class StintPoller():
    def __init__(self):
        self.api = GameApi()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        is_in_pitlane = self.api.get_is_in_pitlane()

        while True:
            if self.api.get_session_status() == 2:
                was_in_pitlane = is_in_pitlane
                is_in_pitlane = self.api.get_is_in_pitlane()
                if was_in_pitlane == 1 and is_in_pitlane == 0:
                    # was in the pitlane but has now left
                    Event("onNewStint")
            time.sleep(1)
