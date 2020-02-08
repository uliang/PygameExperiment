import pygame
from pygame.sprite import DirtySprite
from pygame.mask import Mask
from pygame import Color


class Boundary(DirtySprite):
    def __init__(self, rect_dims, *groups):
        super().__init__(*groups)
        self.rect: pygame.Rect = pygame.Rect(rect_dims)
        self.image = pygame.Surface(self.rect.size)
        self.image.fill(Color('white'))
        self.mask: Mask = Mask((self.rect.width, self.rect.height), fill=True)
        self.dirty = 0  # will never be updated
