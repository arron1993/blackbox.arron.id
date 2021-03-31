import datetime

from pprint import pprint
from game.api import GameApi


class Lap:
    def __init__(self, bbapi, session_id, stint_id):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.session_id = session_id
        self.stint_id = stint_id
        self.sector_times = {}

    def save(self):
        if len(self.sector_times) == 3:
            details = self.gapi.get_last_lap_details()
            details["sector1"] = self.sector_times.get("sector1", 0)
            details["sector2"] = self.sector_times.get("sector2", 0)
            details["sector3"] = self.sector_times.get("sector3", 0)
            pprint(datetime.datetime.now(), "last lap", details)
            self.bbapi.create_lap(
                self.session_id,
                self.stint_id,
                details
            ).json()
        else:
            pprint(datetime.datetime.now(),
                   "Missing sector times, ignoring lap..")
