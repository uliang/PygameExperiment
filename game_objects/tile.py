from typing import Tuple
from functools import partial
from operator import methodcaller

import pygame.sprite as sprite
from pygame.event import post, pump, Event
from pygame import Surface
from pygame.math import Vector2
from pygame import KEYDOWN, K_a, K_s, K_d, K_SPACE, KEYUP

from game_objects.brick import Brick
from game_systems.enums import States
from game_systems.colliders import collision_callback_factory
from game_systems.events import *


class Tile(sprite.Group):
    def __init__(self, background: Surface, *sprites):
        super().__init__(*sprites)
        self.background = background

    def drop(self, speed: int):
        def callback(event_object):
            self('fall', speed)
            self('stop')
        return callback

    def move(self, speed: int):
        def callback(event_object):
            self('move', speed)
        return callback

    def __call__(self, action: str, *args, **kwargs):
        act_on = methodcaller(action, *args, **kwargs)
        for brick in iter(self):
            act_on(brick)

    def update(self, frame):
        super().update(frame)
        self.clear(self.background, self._clear_cbk)
        self.draw(self.background)

    def _clear_cbk(self, surf, rect):
        color = self.background.get_at((0, 0))
        surf.fill(color, rect)

    # @property
    # def collide(self) -> bool:
    #     return sprite.groupcollide(self, self.heap, False, False, self._did_collide)

    # @staticmethod
    # def _did_collide(btile, htile) -> bool:
    #     left, bottom, right = (-1, 0), (0, 1), (1, 0)
    #     return any([self._overlap(btile, direction, htile) for direction in (left, bottom, right)])

    # @staticmethod
    # def _overlap(tile0, tup1, tile1) -> bool:
    #     offset = tile1.rect.move(tup1).topleft - tile0.rect.topleft
    #     return bool(tile0.mask.overlap(tile1.mask, offset))
