import os
import random
from typing import Sequence

from pygame import Rect
import pygame.image as image

from game_objects.brick import Brick
from game_objects.tile import Tile


def make_I(rect: Rect, bw: int) -> Sequence[Rect]:
    return [rect.move(i*bw, 0) for i in range(4)]


def make_O(rect: Rect, bw: int) -> Sequence[Rect]:
    rects = []
    for i in range(2):
        for j in range(2):
            r = rect.move(i*bw, j*bw)
            rects.append(r)
    return rects


def make_L(rect: Rect, bw: int) -> Sequence[Rect]:
    rects = [rect]
    rects.extend([rect.move(-i*bw, bw) for i in range(3)])
    return rects


def make_Lr(rect: Rect, bw: int) -> Sequence[Rect]:
    rects = [rect]
    rects.extend([rect.move(i*bw, bw) for i in range(3)])
    return rects


def make_S(rect: Rect, bw: int) -> Sequence[Rect]:
    return [rect, rect.move(-bw, 0),
            rect.move(-bw, bw), rect.move(-2 * bw, bw)]


def make_Z(rect: Rect, bw: int) -> Sequence[Rect]:
    return [rect, rect.move(bw, 0),
            rect.move(bw, bw), rect.move(2*bw, bw)]


def make_T(rect: Rect, bw: int) -> Sequence[Rect]:
    return [rect.move(-bw, 0), rect, rect.move(bw, 0), rect.move(0, bw)]
