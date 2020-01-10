import pygame
import lib.manager
pygame.init()


class WindowFactory:
    WIDTH = 640
    HEIGHT = 480
    DEFAULT_COLOR = pygame.Color('black')

    def __init__(self):
        self.setup_screen()
        self.setup_background()

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Joe Dever's Lone Wolf Game Companion")

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.DEFAULT_COLOR)
