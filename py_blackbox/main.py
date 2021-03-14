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
        Observer.__init__(self)  # Observer's init needs to be called

    def on_new_session(self, data=None):
        print(time.time(), "on new session")
        try:
            self.bbapi.create_session(
                self.gapi.get_session_details()
            )
        except Exception as e:
            import traceback
            traceback.print_exc(e)

        # create a new session in the backend
        # get a sessionId - assign it to class

    def on_new_lap(self, data):
        print(time.time(), "on new lap", data)
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
        print("Session Status:", session_status)
        if last_session_status != session_status:
            Event("onNewSession", session_status)
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

    #
    bbapi = BlackboxApi()

    username = input("Enter username: ")
    password = input("Enter password: ")
    resp = bbapi.signin(username, password)

    if not resp.ok:
        print("Invalid username or password")
        return 1

    game = Game(bbapi)
    game.attach('onNewSession',  game.on_new_session)
    game.attach('onNewLap',  game.on_new_lap)

    if os.name == 'nt':
        loops = [
            BackgroundEventLoop(session_loop),
            BackgroundEventLoop(lap_loop)
        ]
    else:
        loops = []

    quit_ = False
    while not quit_:
        should_exit = input("type exit to quit: ")
        quit_ = should_exit == "exit"
    return 0


if __name__ == "__main__":
    main()
