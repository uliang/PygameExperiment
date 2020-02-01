import os
from pygame.color import Color


class ApplicationConfig:
    S_HEIGHT = 600
    S_WIDTH = 800
    S_COLOR = Color('white')
    ASSET_PATH = os.path.join(
        os.path.dirname(__file__),
        '..',
        'assets'
    )
    B_COLOR = Color('black')
    B_LINE_COLOR = Color('white')
    CEIL = S_HEIGHT // 8 - 20
    W_CENTER = S_WIDTH // 3
    DROP_HEIGHT = 25
    TILE_DIM = (20, 20)
    W_LEFT = W_CENTER - 6 * TILE_DIM[0]
    W_RIGHT = W_CENTER + 8 * TILE_DIM[0]
    FLOOR = CEIL + DROP_HEIGHT * TILE_DIM[1]
    I_BLOCK_DIM = (4 * TILE_DIM[0], 1 * TILE_DIM[1])
    O_BLOCK_DIM = (2 * TILE_DIM[0], 2 * TILE_DIM[1])
    W_VERTICES = [(W_LEFT-1, CEIL-1), (W_LEFT-1, FLOOR),
                  (W_RIGHT, FLOOR), (W_RIGHT, CEIL-1)]
    H_MOVE_RATE = 5
    GRAVITY = 3
