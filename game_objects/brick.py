import math
import pygame.sprite as sprite
import pygame.mask as mask
from pygame.math import Vector2
from pygame import Surface, Rect


class Brick(sprite.Sprite):
    def __init__(self, surf: Surface, position: Rect, fps: int, *groups):
        super().__init__(*groups)
        self.image = surf
        self.rect: Rect = position
        self.mask = mask.from_surface(surf)

        self.v_x = 0
        self.v_y = 0
        self.s_x = Vector2(self.rect.width, 0)
        self.s_y = Vector2(0, self.rect.height)
        self.step_size = Vector2(0, 0)

        self.fps = fps

    def fall(self, speed: int):  # speed is in pixels per sec
        self.v_y = speed

    def move(self, speed: int):
        self.v_x = speed

    def stop(self):
        self.v_x = 0

    def land(self):
        self.v_y = 0
        self.v_x = 0

    def update(self, frame: int):
        if self.speed:
            self.step_size = self.tick(self.v_x, frame) * self.s_x \
                + self.tick(self.v_y, frame) * self.s_y
            self.rect.move_ip(*self.step_size)

    def tick(self, v: int, frame: int):
        if not bool(v):
            return 0
        t = int(frame % (self.fps * self.rect.width // v) == 0)
        t = math.copysign(t, v)
        return t

    @property
    def speed(self):
        return bool(self.v_x+self.v_y)
