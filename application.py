import sys
import pygame
from application_manager import ApplicationManager

pygame.init()


class Application:
    WIDTH = 640
    HEIGHT = 480
    DEFAULT_COLOR = 0, 0, 0
    TOP_LEFT = (0, 0)

    def __init__(self, manager):
        self.setup_manager(manager)
        self.setup_screen()
        self.setup_background()
        self.clock = pygame.time.Clock()

    def setup_manager(self, manager):
        self.manager = manager
        self.manager(self)

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Joe Dever's Lone Wolf Game Companion")

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.DEFAULT_COLOR)

    def render(self):
        self.manager.update()
        self.screen.blit(self.background, self.TOP_LEFT)
        pygame.display.flip()

    def run_forever(self):
        while True:
            for event in pygame.event.get():
                self.manager.dispatch(event)
            self.render()
            self.clock.tick(60)
