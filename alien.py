import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, eafm_settings, screen):
        super(Alien, self).__init__()
        self.x = None
        self.screen = screen
        self.eafm_settings = eafm_settings

        self.image = pygame.image.load('imgs/eafm01.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.alien_position = float(self.rect.x)

    def check_edges(self):
        """ return true if alien hit the screen edge """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += self.eafm_settings.alien_speed_factor * self.eafm_settings.fleet_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)