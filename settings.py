class Settings:
    """ Class with EAFM settings """

    def __init__(self):

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (220, 220, 220)

        # Warship settings
        self.warship_speed = 1.0
        self.warship_limit = 5

        # Alien settings
        self.alien_speed_factor = 0.8
        self.fleet_drop_speed = 15
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 204, 0, 102
        self.bullets_allowed = 3

        # Super Bullets settings
        self.special_bullet_speed = 1.8
        self.special_bullet_width = 12
        self.special_bullet_height = 15
        self.special_bullet_color = 115, 29, 72
        self.special_bullets_allowed = 1