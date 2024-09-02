class Settings():
    """ Class with EAFM settings """

    def __init__(self):

        # Screen settings
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (220, 220, 220)

        # Warship settings
        self.warship_speed = 1.0

        # Bullet settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 204, 0, 102
        self.bullets_allowed = 3

        # Super Bullets settings
        self.super_bullet_speed = 1.8
        self.super_bullet_width = 8
        self.super_bullet_height = 12
        self.super_bullet_color = 204, 0, 102
        self.super_bullets_allowed = 1