import sys

import pygame

from alien import Alien
from bullet import Bullet

#dict for mapping keys
movement_directions = {
    pygame.K_RIGHT: "right",
    pygame.K_LEFT: "left",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}

# WARSHIP ACTION FUNCTIONS
def check_events(eafm_settings, screen, warship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullets(eafm_settings, screen, warship, bullets)

            else:
                direction = movement_directions.get(event.key)
                if direction:
                    setattr(warship, f"moving_{direction}", True)

        elif event.type == pygame.KEYUP:
            direction = movement_directions.get(event.key)
            if direction:
                setattr(warship, f"moving_{direction}", False)

        elif event.type == pygame.QUIT:
            sys.exit()


# SCREEN FUNCTIONS
def update_screen(eafm_settings, screen, warship, bullets, aliens):
    screen.fill(eafm_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    warship.blitme()

    aliens.draw(screen)

    pygame.display.flip()


# BULLETS FUNCTIONS
def fire_bullets(eafm_settings, screen, warship, bullets):
    if len(bullets) < eafm_settings.bullets_allowed:
        new_bullet = Bullet(eafm_settings, screen, warship)
        bullets.add(new_bullet)


def update_bullets(bullets):
    # deleting bullets that disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)



def create_fleet(eafm_settings, screen, aliens):
    alien = Alien(eafm_settings, screen)
    alien_width = alien.rect.width

    # Determine the available space on screen adn the numbers of aliens that fit it
    available_space = eafm_settings.screen_width - 2 * alien_width
    number_aliens = int(available_space / (2 * alien_width))

    # Create the alien fleet
    for alien_number in range(number_aliens):
        alien = Alien(eafm_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
