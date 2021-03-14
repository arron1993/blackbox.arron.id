import time

from poller.poller import Poller
from observer.observer import Observer
from observer.event import Event
from api.game import GameApi


class Game(Observer):
    def __init__(self):
        print("Room is ready.")
        Observer.__init__(self) # Observer's init needs to be called

    def session_changed(self, data=None):
        print("session changed")
        # create a new session in the backend
        # get a sessionId - assign it to class
    
    def on_new_lap(self, data=None):
        print("on new lap")
        # register previous lap data against session id in
        # the backend


def session_event_loop():
    api = GameApi()
    session_status = api.get_session_status()

    while True:
        last_session_status = session_status
        session_status = api.get_status_session()
        if last_session_status != session_status:
            Event("onSessionChange")
        time.sleep(1)

def main():
    game = Game()
    game.attach('onSessionChange',  game.session_changed)
    p = Poller(session_event_loop)

    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()