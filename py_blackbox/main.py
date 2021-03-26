import time
import os
import datetime

from background_event_loop.background_event_loop import BackgroundEventLoop
from observer.observer import Observer
from observer.event import Event

from api.game import GameApi
from api.blackbox import BlackboxApi


class Game(Observer):
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.session_id = None
        self.stint_id = None
        self.sector_times = {}
        Observer.__init__(self)  # Observer's init needs to be called

    def on_new_session(self, data=None):
        try:
            print(datetime.datetime.now(), "new session")
            details = self.gapi.get_session_details()
            print(details)
            new_session = self.bbapi.create_session(details).json()
            self.session_id = new_session["id"]
            if not self.gapi.get_is_in_pitlane():
                # if we're not starting in the pitlane
                # then start a new stint
                Event("onNewStint")

        except Exception as e:
            print(e)

        # create a new session in the backend
        # get a sessionId - assign it to class

    def on_new_stint(self, data=None):
        try:
            print(datetime.datetime.now(), "new stint")
            new_stint = self.bbapi.create_stint(
                self.session_id
            ).json()
            self.stint_id = new_stint["id"]
        except Exception as e:
            print(e)

    def on_new_lap(self, data=None):
        try:
            details = self.gapi.get_last_lap_details()
            details["sector1"] = self.sector_times.get("sector1", 0)
            details["sector2"] = self.sector_times.get("sector2", 0)
            details["sector3"] = self.sector_times.get("sector3", 0)
            print(datetime.datetime.now(), "new lap", details)
            # TODO: Add the sector times here
            self.bbapi.create_lap(
                self.session_id,
                self.stint_id,
                details
            ).json()
            print(self.sector_times)
            self.sector_times = {}
        except Exception as e:
            import traceback
            traceback.format_exc(e)
            print(e)

    def on_new_sector(self, sector):
        """
        Sector times are cumlative, first sector is 10 seconds
        second sector is 25 sec, is 45 seconds.
        Would mean S1 10s, S2 15s, S3 20s - last sector is the total lap time
        """
        print(datetime.datetime.now(), "new sector", sector)
        human_readable_sector = sector + 1
        sector_time = self.gapi.get_last_sector_time()
        sector_key = f"sector{human_readable_sector}"

        if sector == 2:
            self.sector_times[sector_key] = self.gapi.get_last_lap_time()
            self.on_new_lap()
        else:
            self.sector_times[sector_key] = sector_time


def session_loop():
    api = GameApi()
    session_status = api.get_session_status()
    if session_status != 0:
        # if we're already running, the create the new session
        Event("onNewSession", session_status)

    while True:
        last_session_status = session_status
        session_status = api.get_session_status()
        if (last_session_status != session_status and
                last_session_status == 0):
            Event("onNewSession", session_status)
        time.sleep(1)


def stint_loop():
    api = GameApi()
    is_in_pitlane = api.get_is_in_pitlane()

    while True:
        if api.get_session_status() == 2:
            was_in_pitlane = is_in_pitlane
            is_in_pitlane = api.get_is_in_pitlane()
            if was_in_pitlane == 1 and is_in_pitlane == 0:
                # was in the pitlane but has now left
                Event("onNewStint")
        time.sleep(1)


def lap_loop():
    api = GameApi()
    current_sector = 0
    while True:
        # to track a lap change we detect when
        # the car leaves sector 2, that way we
        # can record the sector times
        # then create the lap entry
        if api.get_session_status() == 2:
            # no point doing work if the game isn't running
            last_sector = current_sector
            current_sector = api.get_current_sector()
            if current_sector != last_sector:
                Event("onNewSector", last_sector)
        time.sleep(1)


def main():
    bbapi = BlackboxApi()

    username = input("Enter username: ")
    password = input("Enter password: ")
    resp = bbapi.signin(username, password)

    if not resp.ok:
        print("Invalid username or password")
        return 1

    if os.name == 'nt':
        game = Game(bbapi)
        game.attach('onNewSession',  game.on_new_session)
        game.attach('onNewLap',  game.on_new_lap)
        game.attach('onNewStint', game.on_new_stint)
        game.attach('onNewSector', game.on_new_sector)

        loops = [
            BackgroundEventLoop(session_loop),
            BackgroundEventLoop(stint_loop),
            BackgroundEventLoop(lap_loop),
        ]
        quit_ = False
        while not quit_:
            should_exit = input("type exit to quit: ")
            quit_ = should_exit == "exit"
    else:
        def create_session():
            res = bbapi.create_session({
                "type": "practice",
                "circuit": "silverstone",
                "car": "bentley_continental_gt3_2016"
            })

        def create_stint():
            bbapi.create_stint(1)

        def create_lap():
            res = bbapi.create_lap(1, 1, {
                "time": 120 * 1000,
                "number": 1,
                "fuel_used": 2.5,
            })
        create_lap()
    return 0


if __name__ == "__main__":
    main()
