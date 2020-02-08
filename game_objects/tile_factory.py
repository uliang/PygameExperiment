import pygame


class TileFactory:
    def __init__(self, container, brick_generator):
        self.container = container
        self.bricks = brick_generator

    def on_next(self, event_object):
        for _ in range(4):
            brick = next(self.bricks)
            brick.add(self.container)

    def on_error(self, error):
        pass

    def on_completed(self):
        pass
