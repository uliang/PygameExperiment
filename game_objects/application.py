import sys
import random


import pygame
import pygame.display as display
import pygame.draw as draw
import pygame.event as event

from rx.core.typing import Observable
from game_objects.application_config import ApplicationConfig
from game_systems.events import NEWTILE


class Application:
    def __init__(self, config: ApplicationConfig, event_stream: Observable):
        self._screen = display.set_mode((config.S_WIDTH, config.S_HEIGHT))
        self.screen.fill(config.S_COLOR)
        display.set_caption(config.S_CAPTION)

        self.event_stream = event_stream

    @property
    def screen(self):
        return self._screen

    def run_forever(self):
        event.post(event.Event(NEWTILE))
        self.event_stream.connect()
