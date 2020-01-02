import pygame
import sys


pygame.init()


class Application:
    WIDTH = 640
    HEIGHT = 480
    DEFAULT_COLOR = 0, 0, 0

    def __init__(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def run_forever(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.screen.fill(self.DEFAULT_COLOR)
                pygame.display.flip()
