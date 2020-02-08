import pygame

from game_objects.application_config import ApplicationConfig


class TileFactory:
    def __init__(self, config: ApplicationConfig, surface_generator, shape_generator, tile_container, brick_constructor):
        self.config = config
        self.surfaces = surface_generator
        self.shapes = shape_generator
        self.container = tile_container
        self.constructor = brick_constructor

    def on_next(self, event_object):
        shape_function = next(self.shapes)
        surf = next(self.surfaces)
        initial_rect = pygame.Rect(
            (self.config.W_CENTER, self.config.CEIL), self.config.BRICK_DIM)
        for shape in shape_function(initial_rect, self.config.BRICK_DIM[0]):
            brick = self.constructor(
                surf, shape, self.config.FPS, self.container)

    def on_error(self, error):
        pass

    def on_completed(self):
        pass
