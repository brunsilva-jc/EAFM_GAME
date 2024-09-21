import sys

import pygame

from alien import Alien
from bullet import Bullet
from time import sleep

#dict for mapping keys
movement_directions = {
    pygame.K_RIGHT: "right",
    pygame.K_LEFT: "left",
    pygame.K_UP: "up",
    pygame.K_DOWN: "down",
}

# WARSHIP ACTION FUNCTIONS
def check_events(eafm_settings, screen, warship, bullets, special_bullets, stats, button):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                fire_bullets(eafm_settings, screen, warship, bullets)

            elif event.key == pygame.K_RCTRL:
                fire_special_bullets(eafm_settings, screen, warship, special_bullets)

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, button, mouse_x, mouse_y)


def check_play_button(stats, button, mouse_x, mouse_y):
    if button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

# SCREEN FUNCTIONS
def update_screen(eafm_settings, screen, warship, bullets, special_bullets, aliens, stats,  button):

    screen.fill(eafm_settings.bg_color)

    warship.blitme()

    aliens.draw(screen)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    for special_bullet in  special_bullets.sprites():
        special_bullet.draw_bullet()

    if not stats.game_active:
        button.draw_button()

    pygame.display.flip()


# BULLETS FUNCTIONS
def fire_bullets(eafm_settings, screen, warship, bullets):
    if len(bullets) < eafm_settings.bullets_allowed:
        new_bullet = Bullet(
            eafm_settings.bullet_width,
            eafm_settings.bullet_height,
            eafm_settings.bullet_color,
            eafm_settings.bullet_speed,
            screen,
            warship)
        bullets.add(new_bullet)

def fire_special_bullets(eafm_settings, screen, warship, special_bullets):
    if len(special_bullets) < eafm_settings.special_bullets_allowed:
        new_bullet = Bullet(
            eafm_settings.special_bullet_width,
            eafm_settings.special_bullet_height,
            eafm_settings.special_bullet_color,
            eafm_settings.special_bullet_speed,
            screen,
            warship)
        special_bullets.add(new_bullet)


def update_bullets(eafm_settings, screen , warship, bullets, special_bullets, aliens):
    # deleting bullets that disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    for special_bullet in special_bullets.copy():
        if special_bullet.rect.bottom <= 0:
            special_bullets.remove(special_bullet)

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    collisions2 = pygame.sprite.groupcollide(special_bullets, aliens, False, True)

    if len(aliens) == 0:
        bullets.empty()
        special_bullets.empty()
        create_fleet(eafm_settings, screen, warship, aliens)

def get_number_aliens(eafm_settings,alien_width):
    # Determine the available space on screen and the numbers of aliens that fit it
    available_space = eafm_settings.screen_width - 2 * alien_width
    number_aliens = int(available_space / (2.5 * alien_width))
    return number_aliens

def get_number_rows(eafm_settings, warship_height, alien_height):
    available_space_vertical = (eafm_settings.screen_height - (6 * alien_height) - warship_height)
    number_rows = int(available_space_vertical / (2 * alien_height))
    return number_rows


def create_alien(eafm_settings, screen, aliens, alien_number, row_number):
    alien = Alien(eafm_settings, screen)
    alien_width = alien.rect.width

    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


#Functions to create aliens fleet
def create_fleet(eafm_settings, screen, warship, aliens):
    alien = Alien(eafm_settings, screen)
    number_aliens = get_number_aliens(eafm_settings, alien.rect.width)
    number_rows = get_number_rows(eafm_settings, warship.rect.height, alien.rect.height)

    # Create the alien fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            create_alien(eafm_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(eafm_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(eafm_settings, aliens)
            break

def change_fleet_direction(eafm_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += eafm_settings.fleet_drop_speed
    eafm_settings.fleet_direction *= -1

def update_aliens(eafm_settings, warship, aliens, stats, screen, bullets):
    check_fleet_edges(eafm_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(warship, aliens):
        warship_hit(eafm_settings, stats, screen, warship, aliens, bullets)


def warship_hit(eafm_settings, stats, screen, warship, aliens, bullets):
    """ functions that responds to warship collision with aliens """
    if stats.warships_left > 0:
        stats.warships_left -= 1

        aliens.empty()
        bullets.empty()

        warship.center_warship()

        # pause the game to indicate the collision
        sleep(0.5)

    else:
        stats.game_active = False
