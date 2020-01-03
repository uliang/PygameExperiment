import pygame
import itertools
from events import *

pygame.init()


class Splash:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, app):
        self.app = app
        self.setup_title(app)
        self.setup_subtitle(app)
        self.blinker = pygame.Surface(self.subtitle_rect.size)
        self.cycler = itertools.cycle([self.blinker, self.subtitle])

    def setup_title(self, app):
        title_font = pygame.font.SysFont(None, 60)
        self.title = title_font.render(
            "Joe Dever's Lone Wolf", True, self.WHITE, self.BLACK)
        self.title_rect = self.title.get_rect(centerx=app.screen.get_width()/2,
                                              centery=app.screen.get_height()/2)

    def setup_subtitle(self, app):
        subtitle_offset = 50
        subtitle_font = pygame.font.SysFont(None, 30)
        self.subtitle = subtitle_font.render(
            "Press any key", True, self.WHITE, self.BLACK)
        self.subtitle_rect = self.subtitle.get_rect(centerx=app.screen.get_width()/2,
                                                    centery=app.screen.get_height()/2+subtitle_offset)

    def render(self, app):
        for event in pygame.event.get(BLINK):
            surf = next(self.cycler)
            app.background.blit(surf, self.subtitle_rect)
        app.background.blit(self.title, self.title_rect)
        app.screen.blit(app.background, app.TOP_LEFT)
        pygame.display.flip()
