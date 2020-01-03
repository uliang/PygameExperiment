import sys
import pygame
import Views
from events import *

pygame.init()


class ApplicationManager:
    def __init__(self):
        self.context = None
        self.current_state = self.default
        self.view = None

    def __call__(self):
        for event in pygame.event.get([ENTRY, EXIT]):
            self.current_state(event)
        if self.view:
            self.view.render(self.context)

    def default(self, event):
        if event.type == ENTRY:
            if self.view is None:
                self.view = Views.Splash(self.context)
            pygame.time.set_timer(BLINK, 1000)
        elif event.type == EXIT:
            pygame.time.set_timer(BLINK, 0)
