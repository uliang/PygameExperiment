import os
from typing import Tuple, Iterator, Optional
import pygame
import pygame.image as image
import pygame.event as event
import pygame.display as display
import pygame.sprite as sprite
import pygame.transform as transform
import pygame.draw as draw
import pygame.mask as mask
from pygame import Color

from game_objects.application_config import ApplicationConfig
from game_systems.enums import Directions, States


class Block(sprite.Sprite):
    def __init__(self, tile_surf: pygame.Surface, background: pygame.Surface,
                 initial_pos: Tuple[int], initial_drop_rate: int, h_move_rate: int,
                 speed_x: int, speed_y: int):
        super().__init__()
        self.background = background

        self.block = tile_surf
        self.rect = self.block.get_rect()
        self.mask = mask.from_surface(tile_surf)
        self.new_pos = None
        self.block_patch = pygame.Surface(tile_surf.get_size()).convert()
        self.block_patch.fill(background.get_at((0, 0)))

        self.rect.topleft = initial_pos
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.initial_drop_rate = initial_drop_rate
        self.drop_rate = initial_drop_rate
        self.h_move_rate = h_move_rate

        self.dir_vector = [0, 0]

        self.state = States.DROPPING

    def render(self):
        self.background.blit(self.block, self.rect)
        screen = display.get_surface()
        screen.blit(self.background, screen.get_rect())

    def update(self):
        self.new_pos = self.rect.move(*self.dir_vector)
        self.background.blit(self.block_patch, self.rect)
        self.rect = self.new_pos
        self.render()
        self.dir_vector = [0, 0]
        event.pump()

    def drop(self, frame_counter: int):
        tick = frame_counter % self.drop_rate
        if tick == 0:
            self.dir_vector[1] += self.speed_y

    def move(self, frame_counter: int):
        tick = frame_counter % self.h_move_rate
        if tick == 0:
            if self.ismovingleft():
                self.dir_vector[0] += -1 * self.speed_x
            elif self.ismovingright():
                self.dir_vector[0] += 1 * self.speed_x

    def rotate(self, max_depth: int):
        self.block = transform.rotate(self.block, 90)
        self.mask = mask.from_surface(self.block)
        x_, y_ = self.rect.topleft
        self.new_pos = self.block.get_rect()
        self.new_pos.move_ip(x_, y_)
        if self.new_pos.bottom >= max_depth:
            dy = max_depth - self.new_pos.bottom
            self.new_pos.move_ip(0, dy)
        self.background.blit(self.block_patch, self.rect)
        self.block_patch = transform.rotate(self.block_patch, 90)
        self.rect = self.new_pos

    def stop(self):
        self.state = States.DROPPING

    def ismovingleft(self) -> bool:
        return self.state == States.MOVING_LEFT

    def ismovingright(self) -> bool:
        return self.state == States.MOVING_RIGHT

    def isgrounded(self) -> bool:
        return self.state == States.GROUNDED

    def isheavy(self) -> bool:
        return self.state == States.HEAVY

    def set_state(self, state: States):
        self.state = state

    def set_block_drop_rate(self, gravity: Optional[int] = None):
        if gravity:
            self.drop_rate = gravity
            return
        self.drop_rate = self.initial_drop_rate


def block_factory(asset_path: str, image_path: str,
                  background: pygame.Surface, initial_pos: Tuple[int],
                  block_shape: Tuple[int], h_move_rate: int, speed_x: int,
                  speed_y: int) -> Optional[Iterator[Block]]:
    def gen_f():
        tile_surf = image.load(os.path.join(asset_path, image_path))
        tile_surf = tile_surf.convert().convert_alpha()
        tile_surf = transform.scale(tile_surf, block_shape)

        block = None
        while True:
            drop_rate = yield block
            if drop_rate:
                block = Block(tile_surf, background, initial_pos,
                              drop_rate, h_move_rate, speed_x, speed_y)
    gen_ = gen_f()
    next(gen_)
    return gen_
