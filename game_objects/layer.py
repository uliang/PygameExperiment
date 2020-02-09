from typing import Tuple

import pygame.sprite as sprite
import pygame.surface as surface
import pygame.mask as mask
from pygame import Surface, Color


class Layer(sprite.Sprite):
    def __init__(self, topleft: Tuple[int, int], size: Tuple[int, int], id_: int,  *groups):
        super().__init__(*groups)
        self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft
        self.mask = mask.from_surface(self.image)
        self.mask.fill()
        self.id = id_

    def __repr__(self):
        return f'<Layer {self.id}>'
