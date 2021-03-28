
from game.api import GameApi
from observer.event import Event


class Lap:
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.sector_times = {}

    def save(self):
        details = self.gapi.get_last_lap_details()
        details["sector1"] = self.sector_times.get("sector1", 0)
        details["sector2"] = self.sector_times.get("sector2", 0)
        details["sector3"] = self.sector_times.get("sector3", 0)
        print(datetime.datetime.now(), "last lap", details)
        self.bbapi.create_lap(
            self.session_id,
            self.stint_id,
            details
        ).json()
