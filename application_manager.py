import pygame
import sys
import Views

pygame.init()


class ApplicationManager:
    def __init__(self):
        self.context = None
        self.current_state = self.default
        self.views = {
            self.default.__name__: Views.title
        }

    def __call__(self, context):
        self.context = context

    def dispatch(self, event):
        self.current_state(event)

    def update(self):
        self.views[self.current_state.__name__](self.context)

    def default(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
