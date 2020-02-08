import os
import random
from typing import Sequence

from pygame import Rect
import pygame.image as image

from game_objects.brick import Brick
from game_objects.tile import Tile
from game_objects.application_config import ApplicationConfig


def make_I(rect: Rect, brick_width: int) -> Sequence[Rect]:
    return [rect.move(i*brick_width, 0) for i in range(4)]


def make_O(rect: Rect, brick_width: int) -> Sequence[Rect]:
    rects = []
    for i in range(2):
        for j in range(2):
            r = rect.move(i*brick_width, j*brick_width)
            rects.append(r)
    return rects


def make_L(rect: Rect, brick_width: int) -> Sequence[Rect]:
    rects = [rect]
    rects.extend([rect.move(-i*brick_width, brick_width) for i in range(3)])
    return rects


def make_Lr(rect: Rect, brick_width: int) -> Sequence[Rect]:
    rects = [rect]
    rects.extend([rect.move(i*brick_width, brick_width) for i in range(3)])
    return rects


def make_S(rect: Rect, brick_width: int) -> Sequence[Rect]:
    return [rect, rect.move(-brick_width, 0),
            rect.move(-brick_width, -brick_width), rect.move(-2 *
                                                             brick_width, -brick_width)]


def make_Z(rect: Rect, brick_width: int) -> Sequence[Rect]:
    return [rect, rect.move(brick_width, 0),
            rect.move(brick_width, brick_width), rect.move(
            2*brick_width, brick_width)]


def make_T(rect: Rect, brick_width: int) -> Sequence[Rect]:
    return [rect.move(-brick_width, 0), rect, rect.move(brick_width, 0), rect.move(0, brick_width)]
