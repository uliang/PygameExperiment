import pygame
import itertools
from events import *
from lib.base import AbstractView
from lib.manager import Window, Event

pygame.init()


class Splash(AbstractView):

    def __init__(self):
        self.screen, self.background = Window.provide()
        self.observable = Event.provide()
        self.setup_title()
        self.setup_subtitle()
        self.blinker = pygame.Surface(self.subtitle_rect.size)
        self.cycler = itertools.cycle([self.blinker, self.subtitle])
        self.observable.subscribe(BLINK_SIG, self.blink)
        self.observable.subscribe(MOUSEDOWN_SIG, self.transition)
        self.start_blinking()

    def setup_title(self):
        title_font = pygame.font.SysFont(None, 60)
        self.title = title_font.render(
            "Joe Dever's Lone Wolf", True, pygame.Color('white'), pygame.Color('black'))
        self.title_rect = self.title.get_rect(centerx=self.screen.get_width()/2,
                                              centery=self.screen.get_height()/2)

    def setup_subtitle(self):
        subtitle_offset = 50
        subtitle_font = pygame.font.SysFont(None, 30)
        self.subtitle = subtitle_font.render(
            "Press any key", True, pygame.Color('white'), pygame.Color('black'))
        self.subtitle_rect = self.subtitle.get_rect(centerx=self.screen.get_width()/2,
                                                    centery=self.screen.get_height()/2+subtitle_offset)

    def blink(self, **kwargs):
        self.subtitle = next(self.cycler)

    def render(self):
        self.background.blit(self.subtitle, self.subtitle_rect)
        self.background.blit(self.title, self.title_rect)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def start_blinking(self):
        pygame.time.set_timer(BLINK, 1000)

    def transition(self, **kwargs):
        transition_sig = pygame.event.Event(TRANS, code='game')
        pygame.event.post(transition_sig)


class Game(AbstractView):

    DEFAULT_COLOR = pygame.Color('green')

    def __init__(self):
        self.screen, self.background = Window.provide() 
        self.background.fill(self.DEFAULT_COLOR)

    def render(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()
