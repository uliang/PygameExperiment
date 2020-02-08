from typing import Tuple

import pygame.sprite as sprite
import pygame.surface as surface
import pygame.mask as mask
from pygame import Surface, Color

from game_objects.application_config import ApplicationConfig


class Layer(sprite.Sprite):
    def __init__(self, dimensions: Tuple[int], init_pos: Tuple[int], id_, fill: Color,  *groups):
        super().__init__(*groups)
        self.image = Surface(dimensions)
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.image.fill(fill, self.rect)
        self.mask = mask.from_surface(self.image)
        self.mask.fill()
        self.id = id_

    def __repr__(self):
        return f'<Layer {self.id}>'


def layer_factory(config: ApplicationConfig, i: int) -> Layer:
    init_pos = config.W_LEFT, config.CEIL + i*config.TILE_DIM[1]
    return Layer(dimensions=config.L_DIMS, init_pos=init_pos, id_=i, fill=config.B_COLOR)
