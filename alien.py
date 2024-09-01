import pygame.image
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, eafm_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.eafm_settings = eafm_settings

        self.image = pygame.image.load('imgs/alien02.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.alien_position = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image, self.rect)