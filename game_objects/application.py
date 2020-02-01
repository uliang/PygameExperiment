import sys
import random
from functools import partial

import pygame
import pygame.display as display
import pygame.event as event
import pygame.sprite as sprite
import pygame.draw as draw
import pygame.mask as mask


from game_objects.application_config import ApplicationConfig
from game_objects.block import block_factory
from game_systems.enums import Directions, States


class Application:
    def __init__(self, config: ApplicationConfig):
        self.setup_screen(config.S_WIDTH, config.S_HEIGHT, 'Tetris',
                          config.S_COLOR)
        self.setup_well(config.W_LEFT, config.W_RIGHT, config.FLOOR)

        background = pygame.Surface(
            (config.S_WIDTH, config.S_HEIGHT)).convert()
        background.fill(config.B_COLOR)
        draw.lines(background, config.B_LINE_COLOR, True, config.W_VERTICES)

        block_init_pos = (config.W_CENTER, config.CEIL)
        self.block_gravity = config.GRAVITY
        block_factory_ = partial(block_factory, asset_path=config.ASSET_PATH, background=background, initial_pos=block_init_pos,
                                 h_move_rate=config.H_MOVE_RATE, speed_x=config.TILE_DIM[0], speed_y=config.TILE_DIM[0])
        IBlock = block_factory_(
            image_path='I.png', block_shape=config.I_BLOCK_DIM)
        OBlock = block_factory_(
            image_path='O.png', block_shape=config.O_BLOCK_DIM)
        self.tile_list = [IBlock, OBlock]
        self.tile = None
        self.grounded_tiles = sprite.Group()

        self.clock = pygame.time.Clock()
        self.frame = -1

    def setup_well(self, left_wall, right_wall, floor_depth):
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.floor_depth = floor_depth

    def setup_screen(self, width: int, height: int, caption: str,
                     color: pygame.Color):
        self.screen = display.set_mode(size=(width, height)).convert()
        self.screen.fill(color)
        display.set_caption(caption)

    def run_forever(self):
        while True:
            self.tile = self.maketile()
            self.clock.tick(60)
            self.frame += 1
            for event_ in event.get():
                if event_.type == pygame.QUIT:
                    sys.exit()
                if event_.type == pygame.KEYDOWN and not self.tile.isgrounded():
                    if event_.key == pygame.K_a and not self.collide_left():
                        self.tile.set_state(States.MOVING_LEFT)
                    elif event_.key == pygame.K_d and not self.collide_right():
                        self.tile.set_state(States.MOVING_RIGHT)
                    elif event_.key == pygame.K_s:
                        self.tile.set_state(States.HEAVY)
                    elif event_.key == pygame.K_SPACE:
                        self.tile.rotate(self.floor_depth)
                if event_.type == pygame.KEYUP:
                    self.tile.stop()
                    self.tile.set_block_drop_rate()

            self.droptile()
            self.movetile()
            self.update()
            self.render()

    def droptile(self):
        if self.tile.isheavy():
            self.tile.set_block_drop_rate(self.block_gravity)
        if not self.collide_bottom():
            self.tile.drop(self.frame)
        else:
            self.tile.set_state(States.GROUNDED)
            self.grounded_tiles.add(self.tile)
            self.frame = -1

    def movetile(self):
        if self.tile.ismovingleft() and self.collide_left():
            self.tile.stop()
        if self.tile.ismovingright() and self.collide_right():
            self.tile.stop()
        self.tile.move(self.frame)

    def maketile(self):
        if self.tile is None:
            return random.choice(self.tile_list).send(45)
        if self.tile.isgrounded():
            return random.choice(self.tile_list).send(45)
        return self.tile

    def update(self):
        self.tile.update()
        print(f'{self.tile.state:<20}', end='\r')

    def render(self):
        display.flip()

    def collide_right(self) -> bool:
        self.tile.rect.move_ip(1, 0)
        collide_wall = self.right_wall <= self.tile.rect.right
        collide_sprites = sprite.spritecollideany(
            self.tile, self.grounded_tiles)
        self.tile.rect.move_ip(-1, 0)
        return collide_sprites or collide_wall

    def collide_left(self) -> bool:
        self.tile.rect.move_ip(-1, 0)
        collide_wall = self.left_wall >= self.tile.rect.left
        collide_sprites = sprite.spritecollideany(
            self.tile, self.grounded_tiles)
        self.tile.rect.move_ip(1, 0)
        return collide_sprites or collide_wall

    def collide_bottom(self) -> bool:
        self.tile.rect.move_ip(0, 1)
        collide_wall = self.floor_depth <= self.tile.rect.bottom
        collide_sprites = sprite.spritecollideany(
            self.tile, self.grounded_tiles)
        self.tile.rect.move_ip(0, -1)
        return collide_sprites or collide_wall
