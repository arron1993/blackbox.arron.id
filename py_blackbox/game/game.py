import datetime

from game.api import GameApi
from game.models.session import Session
from observer.observer import Observer


class Game(Observer):
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.session = None

        Observer.__init__(self)

    def on_new_session(self, data=None):
        self.session = Session(self.bbapi)

    def on_new_stint(self, data=None):
        self.session.new_stint()

    def on_new_sector(self, sector):
        """
        Sector times are cumlative, first sector is 10 seconds
        second sector is 25 sec, is 45 seconds.
        Would mean S1 10s, S2 15s, S3 20s - last sector is the total lap time
        """
        print(datetime.datetime.now(), "new sector", sector)

        self.session.stint.update_lap(sector)
