from game.api import GameApi
from observer.event import Event


class Session:
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.id = None
        new_session = self.bbapi.create_session(
            self.gapi.get_session_details()
        ).json()

        self.id = new_session["id"]
        self.stint = None
        self.stints = []
        if not self.gapi.get_is_in_pitlane():
            # if we're not starting in the pitlane
            # then start a new stint
            self.new_stint()

    def new_stint(self):
        self.stint = Stint(self.bbapi)
        self.stints.append(stint)
