class GameStats:
    """ EAFM game stats """

    def __init__(self, eafm_settings):
        self.eafm_settings = eafm_settings
        self.reset_stats()
        self.game_active = False


    def reset_stats(self):
        self.warships_left = self.eafm_settings.warship_limit