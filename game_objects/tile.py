from typing import Tuple
from operator import methodcaller

import pygame.sprite as sprite
from pygame import Surface

from game_objects.brick import Brick
from game_systems.events import *
from game_systems.utils import eraser


class Tile(sprite.Group):
    def __init__(self, background: Surface, *sprites):
        super().__init__(*sprites)
        self.background = background

    def __call__(self, action: str, *args, **kwargs):
        act_on = methodcaller(action, *args, **kwargs)
        for brick in iter(self):
            act_on(brick)

    def update(self, frame):
        super().update(frame)
        self.clear(self.background, eraser(self.background.get_at((0, 0))))
        self.draw(self.background)

    def _velocity(self, direction: str):
        return sum(getattr(brick, direction) for brick in iter(self)) / len(self)

    @property
    def v_x(self):
        return self._velocity('v_x')

    @property
    def v_y(self):
        return self._velocity('v_y')
