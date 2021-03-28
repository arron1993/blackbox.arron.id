
class LapPoller():
    def __init__(self):
        self.api = GameApi()

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        current_sector = 0
        while True:
            # to track a lap change we detect when
            # the car leaves sector 2, that way we
            # can record the sector times
            # then create the lap entry
            if self.api.get_session_status() == 2:
                # no point doing work if the game isn't running
                last_sector = current_sector
                current_sector = api.get_current_sector()
                if current_sector != last_sector:
                    Event("onNewSector", last_sector)
            time.sleep(1)
