import time
import mmap
import os

from poller.poller import Poller
from observer.observer import Observer
from observer.event import Event

from api.game import GameApi
from api.blackbox import BlackboxApi

class Game(Observer):
    def __init__(self):
        Observer.__init__(self)  # Observer's init needs to be called

    def session_changed(self, data=None):
        print(time.time(), "session changed")
        # create a new session in the backend
        # get a sessionId - assign it to class

    def on_new_lap(self, data):
        print(time.time(), "on new lap", data)
        # register previous lap data against session id in
        # the backend


def session_event_loop():
    api = GameApi()
    session_status = api.get_session_status()

    while True:
        last_session_status = session_status
        session_status = api.get_session_status()

        print(session_status)
        if last_session_status != session_status:
            Event("onSessionChange")
        time.sleep(1)


def lap_event_loop():
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
    # p = Poller(session_event_loop)
    api = BlackboxApi()

    username = input("Enter username: ")
    password = input("Enter password: ")
    api.signin(username, password)
    resp = api.create_session({
        "car": "amr_v12_vantage_gt3",
        "circuit": "silverstone",
        "type": "practice"
    })
    breakpoint()
    while True:
        if os.name == 'nt':
            lap_event_loop()
        # print(api.get_number_of_laps())
        time.sleep(1)


if __name__ == "__main__":
    main()
