from game.api import GameApi
from observer.event import Event


class Stint:
    def __init__(self, bbapi):
        print(datetime.datetime.now(), "new stint")
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.laps = []
        new_stint = self.bbapi.create_stint(
            self.session_id
        ).json()
        self.stint_id = new_stint["id"]
        self.lap = Lap()
        self.laps = []

    def update_lap(self):
        human_readable_sector = sector + 1
        sector_time = self.gapi.get_last_sector_time()
        sector_key = f"sector{human_readable_sector}"
        if sector == 2:
            self.lap.sector_times[sector_key] = self.gapi.get_last_lap_time()
            self.on_new_lap()
        else:
            self.lap.sector_times[sector_key] = sector_time

    def complete_lap(self):
        self.lap.save()
        self.laps.append(lap)
        self.lap = Lap()
