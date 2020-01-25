import os
from typing import Tuple, Iterator, Optional
import pygame 
import pygame.image as image 
import pygame.event as event 
import pygame.display as display 
import pygame.sprite as sprite 
from pygame import Color 

from game_objects.application_config import ApplicationConfig as config
from game_systems.enums import Directions


class Block(sprite.Sprite): 
    def __init__(self, tile_surf: pygame.Surface, background: pygame.Surface,
                 initial_pos: Tuple[int], initial_drop_rate: int): 
        super().__init__()
        self.background = background
        
        self.block = tile_surf 
        self.curr_pos = self.block.get_rect()
        self.block_patch = pygame.Surface(tile_surf.get_size()).convert() 
        self.block_patch.fill(background.get_at((0,0)))
        
        self.curr_pos.center = initial_pos
        self.speed_y = tile_surf.get_rect().height
        self.speed_x = self.speed_y
        self.drop_rate = initial_drop_rate 

        self.frame_counter = 0
        self.newpos = [0, 0]
        
    def update(self): 
        next_pos = self.curr_pos.move(*self.newpos)
        self.background.blit(self.block_patch, self.curr_pos)
        self.curr_pos = next_pos
        self.background.blit(self.block, self.curr_pos)

        screen = display.get_surface()
        screen.blit(self.background, screen.get_rect()) 
        
        self.newpos = [0, 0]
        event.pump() 

    def drop(self): 
        tick = self.frame_counter//self.drop_rate
        if tick == 0: 
            self.frame_counter += 1
            return 
        self.newpos[1] += tick * self.speed_y
        self.frame_counter = 0 
        return 
    
    def move(self, direction: Directions):
        if direction == Directions.LEFT: 
            self.newpos[0] += -1 * self.speed_x
        elif direction == Directions.RIGHT: 
            self.newpos[0] += 1 * self.speed_x

def block_factory(asset_path: str, image_path: str, 
                background: pygame.Surface, initial_pos: Tuple[int]) -> Optional[Iterator[Block]]: 
    def gen_f(): 
        tile_surf = image.load(os.path.join(asset_path, image_path))
        tile_surf = tile_surf.convert().convert_alpha()
        block = None
        while True: 
            drop_rate = yield block
            if drop_rate: 
                block = Block(tile_surf, background,  initial_pos, drop_rate) 
    gen_ = gen_f() 
    next(gen_) 
    return gen_     