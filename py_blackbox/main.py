import time
import os
import datetime

from game.game import Game
from game.pollers import SessionPoller
from blackbox.api import BlackboxApi

def main():
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
    game.attach('onNewStint', game.on_new_stint)
    game.attach('onNewSector', game.on_new_sector)

    sp = SessionPoller()
    sp.start()
    # loops = [
    #     BackgroundEventLoop(session_loop),
    #     BackgroundEventLoop(stint_loop),
    #     BackgroundEventLoop(lap_loop),
    # ]
    quit_ = False
    while not quit_:
        should_exit = input("type exit to quit: ")
        quit_ = should_exit == "exit"
    return 0


if __name__ == "__main__":
    main()
