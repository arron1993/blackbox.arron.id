import datetime

from game.api import GameApi
from game.models.stint import Stint


class Session:
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.id = None
        details = self.gapi.get_session_details()
        print(datetime.datetime.now(), "New Session", details)
        new_session = self.bbapi.create_session(
            details
        ).json()

        self.id = new_session["id"]
        self.stint = None
        self.stints = []
        if not self.gapi.get_is_in_pitlane():
            # if we're not starting in the pitlane
            # then start a nsew stint
            self.new_stint()

    def new_stint(self):
        self.stint = Stint(self.bbapi, self.id)
        self.stints.append(self.stint)
