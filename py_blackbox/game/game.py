from observer.observer import Observer


class Game(Observer):
    def __init__(self, bbapi):
        self.bbapi = bbapi
        self.gapi = GameApi()
        self.session_id = None
        self.stint_id = None
        self.sector_times = {}
        Observer.__init__(self)

    def on_new_session(self, data=None):
        try:
            print(datetime.datetime.now(), "new session")
            new_session = self.bbapi.create_session(
                self.gapi.get_session_details()
            ).json()
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
