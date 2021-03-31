import time
import threading
import datetime

from pprint import pprint

from observer.event import Event
from game.api import GameApi
from game.models.session_status import SessionStatus


class LapPoller():
    def __init__(self):
        self.api = GameApi()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        current_sector = self.api.get_current_sector()
        while True:
            try:
                # to track a lap change we detect when
                # the car leaves sector 2, that way we
                # can record the sector times
                # then create the lap entry
                if self.api.get_session_status() == SessionStatus.LIVE:
                    # no point doing work if the game isn't running
                    last_sector = current_sector
                    current_sector = self.api.get_current_sector()
                    if current_sector != last_sector:
                        Event("onNewSector", last_sector)
            except Exception as e:
                pprint(datetime.datetime.now(), "Lap Error", e)
            time.sleep(0.5)
