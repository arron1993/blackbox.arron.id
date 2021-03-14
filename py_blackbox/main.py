import time
import mmap
import os

from background_event_loop.background_event_loop import BackgroundEventLoop
from observer.observer import Observer
from observer.event import Event

from api.game import GameApi
from api.blackbox import BlackboxApi


class Game(Observer):
    def __init__(self):
        self.bbapi = BlackboxApi()
        self.gapi = GameApi()
        Observer.__init__(self)  # Observer's init needs to be called

    def session_changed(self, status):
        print(time.time(), "session changed", 2)
        try:
            if status == 2:
                self.bbapi.create_session(
                    self.gapi.get_session_details()
                )
        except Exception as e:
            print(e)

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
        Event("onSessionChange", session_status)
    while True:
        last_session_status = session_status
        session_status = api.get_session_status()
        if last_session_status != session_status:
            Event("onSessionChange", session_status)
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
    game = Game()
    game.attach('onSessionChange',  game.session_changed)
    game.attach('onNewLap',  game.on_new_lap)
    #
    api = BlackboxApi()

    username = input("Enter username: ")
    password = input("Enter password: ")
    resp = api.signin(username, password)
    if not resp.ok:
        print("Invalid username or password")
        return 1

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
        if quit_:
            for loop in loops:
                loop.thread.join()


if __name__ == "__main__":
    main()
