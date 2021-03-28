import datetime

from game.api import GameApi
from observer.event import Event

from game.models.lap import Lap


class Stint:
    def __init__(self, bbapi, session_id):
        print(datetime.datetime.now(), "new stint")
        self.session_id = session_id
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.laps = []

        new_stint = self.bbapi.create_stint(session_id).json()

        self.stint_id = new_stint["id"]
        self.lap = Lap(self.bbapi, self.session_id, self.stint_id)
        self.laps = []

    def update_lap(self, sector):
        human_readable_sector = sector + 1
        sector_time = self.gapi.get_last_sector_time()
        sector_key = f"sector{human_readable_sector}"
        if sector == 2:
            self.lap.sector_times[sector_key] = self.gapi.get_last_lap_time()
            if self.gapi.get_completed_laps() > 0:
                self.complete_lap()
        else:
            self.lap.sector_times[sector_key] = sector_time

    def complete_lap(self):
        self.lap.save()
        self.laps.append(self.lap)
        self.lap = Lap(self.bbapi, self.session_id, self.stint_id)
