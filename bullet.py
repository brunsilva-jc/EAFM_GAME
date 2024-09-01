import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ class to manage bullets fired from the warship """

    def __init__(self, eafm_settings, screen, warship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, eafm_settings.bullet_width, eafm_settings.bullet_height)
        self.rect.centerx = warship.rect.centerx
        self.rect.top = warship.rect.top

        self.bullet_position = float(self.rect.y)

        self.color = eafm_settings.bullet_color
        self.bullet_speed = eafm_settings.bullet_speed

    def update(self):
        """ Moving the bullet on the screen """

        self.bullet_position -= self.bullet_speed
        self.rect.y = self.bullet_position

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)