from lib.s_page_file_graphic import SPageFileGraphic

class GameApi():
    def __init__(self):
        self.graphic = SPageFileGraphic()

    def get_session_status(self):
        return self.graphic.AC_STATUS