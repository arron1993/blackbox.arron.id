class Game(Observer):
    def __init__(self):
        print("Room is ready.")
        Observer.__init__(self)  # Observer's init needs to be called

    def session_changed(self, who):
        print("session changed")


def main():
    room = Room()
    room.attach('onSessionChange',  game.session_changed)
    Event('someone arrived', 'Lenard')


if __name__ == "__main__":
    main()
