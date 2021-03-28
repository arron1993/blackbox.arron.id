import time
import os
import datetime
import getpass
import sys

from game.game import Game
from game.pollers import SessionPoller, StintPoller, LapPoller
from blackbox.api import BlackboxApi


def main():
    bbapi = BlackboxApi()

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    resp = bbapi.signin(username, password)

    if not resp.ok:
        print("Invalid username or password")
        sys.exit(1)
    else:
        print("Authentication Successful")

    game = Game(bbapi)
    game.attach('onNewSession',  game.on_new_session)
    game.attach('onNewStint', game.on_new_stint)
    game.attach('onNewSector', game.on_new_sector)

    sep = SessionPoller()
    stp = StintPoller()
    lp = LapPoller()

    sep.start()
    stp.start()
    lp.start()

    quit_ = False
    while not True:
        should_exit = input("type exit to quit: ")
        if should_exit == "exit":
            sys.exit()
    return 0


if __name__ == "__main__":
    main()
