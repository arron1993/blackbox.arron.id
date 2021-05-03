import time
import threading
import datetime

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

    def _has_lap_changed(self, last_lap):
        return self.api.get_completed_laps() != last_lap

    def run(self):
        current_sector = self.api.get_current_sector()
        current_lap = self.api.get_completed_laps()
        while True:
            try:
                # to track a lap change we detect when
                # the car leaves sector 2, that way we
                # can record the sector times
                # then create the lap entry
                if self.api.get_session_status() == SessionStatus.LIVE.value:
                    last_lap = current_lap
                    current_lap = self.api.get_completed_laps()
                    # no point doing work if the game isn't running
                    last_sector = current_sector
                    current_sector = self.api.get_current_sector()

                    if current_sector != last_sector:
                        if last_sector == 2 and not self._has_lap_changed(last_lap):
                            # sometimes we cross the last sector
                            # but when we get the lap the data its for
                            # the last last lap
                            # so retry here until we're sure
                            # we're on the next lap
                            for _ in range(5):
                                if self._has_lap_changed(last_lap):
                                    Event("onNewSector", last_sector)
                                    break
                                else:
                                    time.sleep(1)
                        else:
                            Event("onNewSector", last_sector)
            except Exception as e:
                print(datetime.datetime.now(), "Lap Error", e)
            time.sleep(1)
