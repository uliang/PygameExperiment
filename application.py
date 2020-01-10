import sys
import pygame
from events import *
from lib.manager import Event, Scenes

pygame.init()


class Application:

    def __init__(self):
        self.observable = Event.provide()
        self.clock = pygame.time.Clock()
        self.current_scene = Scenes.provide('splash')

    def run_forever(self):
        if self.observable:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.observable.unsubscribe()
                        sys.exit()
                    elif event.type == TRANS:
                        self.current_scene = Scenes.provide(event.code)
                    else:
                        self.observable.notify(event)
                self.current_scene.render()
                self.clock.tick(60)
        else:
            raise NotImplementedError(
                'Event handler not found. Please subscribe event handler to application instance.')
