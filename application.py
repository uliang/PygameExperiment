import sys
import pygame
from application_manager import ApplicationManager
from events import *

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
        self.manager.context = self

    def setup_screen(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Joe Dever's Lone Wolf Game Companion")

    def setup_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.DEFAULT_COLOR)

    def run_forever(self):
        start_sig = pygame.event.Event(ENTRY)
        pygame.event.post(start_sig)
        while True:
            for event in pygame.event.get(pygame.QUIT):
                sys.exit()
            self.manager()
            # for event in pygame.event.get():
            #     pass
            self.clock.tick(60)
