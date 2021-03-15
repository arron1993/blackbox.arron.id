import time
import mmap
import os

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
        Observer.__init__(self)  # Observer's init needs to be called

    def on_new_session(self, data=None):
        print(time.time(), "on new session")
        try:
            new_session = self.bbapi.create_session(
                self.gapi.get_session_details()
            ).json()
            self.session_id = new_session["id"]
            current_lap = self.gapi.get_number_of_laps()
            if current_lap > 0:
                Event("onNewLap", current_lap)
        except Exception as e:
            print(e)

        # create a new session in the backend
        # get a sessionId - assign it to class

    def on_new_stint(self, data):
        print(time.time(), "on new lap", data)
        try:
            new_lap = self.bbapi.create_stint(
                self.session_id
            ).json()
        except Exception as e:
            print(e)

    def on_new_lap(self, data):
        print(time.time(), "on new lap", data)
        try:
            new_lap = self.bbapi.create_lap(
                self.stint_id,
                self.gapi.get_last_lap_details()
            ).json()
        except Exception as e:
            print(e)
        # register previous lap data against session id in
        # the backend


def session_loop():
    api = GameApi()
    session_status = api.get_session_status()
    if session_status == 2:
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
        was_in_pitlane = is_in_pitlane
        is_in_pitlane = api.get_is_in_pitlane()
        if was_in_pitlane == 1 and is_in_pitlane == 0:
            # was in the pitlane but has now left
            Event("onNewStint")
        time.sleep(1)


def lap_loop():
    api = GameApi()
    current_lap = api.get_number_of_laps()

    while True:
        last_lap = current_lap
        current_lap = api.get_number_of_laps()
        if last_lap != current_lap:
            Event("onNewLap", current_lap)
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
        loops = [
            BackgroundEventLoop(session_loop),
            BackgroundEventLoop(lap_loop)
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
