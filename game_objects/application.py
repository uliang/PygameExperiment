import sys 
import pygame 
import pygame.display as display 
import pygame.event as event
import pygame.sprite as sprite 

from game_objects.application_config import ApplicationConfig
from game_objects.block import block_factory
from game_systems.enums import Directions

class Application: 
    def __init__(self, config:ApplicationConfig): 
        self.setup_screen(config.S_WIDTH, config.S_HEIGHT, 'Tetris', 
                            config.S_COLOR)
        background = pygame.Surface((config.S_WIDTH, config.S_HEIGHT)).convert()
        background.fill(config.B_COLOR)
        block_init_pos = (config.S_WIDTH//2, config.CEIL)                             

        IBlock = block_factory(config.ASSET_PATH, 'I.png', background,
                                initial_pos=block_init_pos)
        self.tile = IBlock.send(60)
        self.floor_depth = config.CEIL + self.tile.block.get_height() * config.DROP_HEIGHT
        self.clock = pygame.time.Clock()

    def setup_screen(self, width: int, height: int, caption: str, 
                    color: pygame.Color): 
        self.screen = display.set_mode(size = (width, height)).convert()
        self.screen.fill(color)
        display.set_caption(caption)

    def run_forever(self): 
        while True: 
            self.clock.tick(60)
            for event_ in event.get(): 
                if event_.type == pygame.QUIT: 
                    sys.exit() 
                if event_.type == pygame.KEYDOWN: 
                    if event_.key == pygame.K_a: 
                        self.tile.move(Directions.LEFT)
                    elif event_.key == pygame.K_d: 
                        self.tile.move(Directions.RIGHT)

            self.droptile()
            self.update()
            self.render()

    def droptile(self):
        if self.tile.curr_pos.bottom < self.floor_depth: 
            self.tile.drop()

    def update(self): 
        self.tile.update()

    def render(self): 
        display.flip()