import sys
import pygame
import Views

pygame.init()

ENTRY = pygame.USEREVENT+0
BLINK = pygame.USEREVENT+1
EXIT = pygame.USEREVENT+2


class ApplicationManager:
    def __init__(self):
        self.context = None
        self.current_state = self.default
        self.wipe = False
        self.alpha_counter = 0
        self.views = {
            self.default.__name__: Views.title
        }

    def __call__(self, context):
        self.context = context
        start_sig = pygame.event.Event(ENTRY)
        pygame.event.post(start_sig)

    def dispatch(self, event):
        self.current_state(event)

    def update(self):
        self.views[self.current_state.__name__](self.context)

    def default(self, event):
        if event.type == ENTRY:
            pygame.time.set_timer(BLINK, 750)
        elif event.type == BLINK:
            self.wipe = not self.wipe
        elif event.type == EXIT:
            pygame.time.set_timer(BLINK, 0)
        elif event.type == pygame.QUIT:
            sys.exit()
