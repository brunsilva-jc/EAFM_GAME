import pygame.font


class Button:

    def __init__(self, eafm_settings, screen, message):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (0,255,255)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48, italic=True)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_message(message)

    def prep_message(self, message):
        self.msg_image = self.font.render(message, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)