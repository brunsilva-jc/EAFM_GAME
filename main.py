import pygame

from button import Button
from settings import Settings
from game_stats import GameStats
from warship import Warship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #initialize game, settings and screen
    pygame.init()
    eafm_settings = Settings()
    screen = pygame.display.set_mode((eafm_settings.screen_width, eafm_settings.screen_height))
    pygame.display.set_caption("EAFM - Evil Aliens From Mars")

    play_button = Button(eafm_settings, screen, "Play EAFM")

    #game stats
    stats = GameStats(eafm_settings)

    warship = Warship(eafm_settings, screen)

    #Bullets group
    bullets = Group()

    special_bullets = Group()

    #EAFM group
    aliens = Group()

    gf.create_fleet(eafm_settings, screen, warship, aliens)

    while True:
        gf.check_events(eafm_settings, screen, warship, bullets, special_bullets, stats, play_button)

        if stats.game_active:
            warship.update()
            bullets.update()
            special_bullets.update()
            gf.update_bullets(eafm_settings, screen, warship, bullets, special_bullets, aliens)
            gf.update_aliens(eafm_settings, warship, aliens, stats, screen, bullets)

        gf.update_screen(eafm_settings,screen,warship, bullets, special_bullets, aliens, stats, play_button)


run_game()