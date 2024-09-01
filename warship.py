import pygame.image


class Warship():
    def __init__(self, eafm_settings, screen):
        """ Initialize the ship and set start position """
        self.screen = screen

        #Get the warship speed from settings
        self.warship_speed = eafm_settings.warship_speed

        #load the ship image and get its rect
        self.image = pygame.image.load('imgs/rocket-warship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start warship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.warship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.warship_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.warship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.warship_speed

        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)