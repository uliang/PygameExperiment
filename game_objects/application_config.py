import os
from pygame.color import Color


class ApplicationConfig:
    S_CAPTION = 'Tetris'
    S_HEIGHT = 600
    S_WIDTH = 800
    S_COLOR = Color('black')
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
    BRICK_DIM = (20, 20)
    FLOOR = CEIL + DROP_HEIGHT * BRICK_DIM[1]
    W_LEFT = W_CENTER - 6 * BRICK_DIM[0]
    W_RIGHT = W_CENTER + 8 * BRICK_DIM[0]
    W_WIDTH = W_RIGHT - W_LEFT
    W_HEIGHT = FLOOR - CEIL
    TILE_4X1 = (4 * BRICK_DIM[0], 1 * BRICK_DIM[1])
    TILE_2X2 = (2 * BRICK_DIM[0], 2 * BRICK_DIM[1])
    TILE_3X2 = (3 * BRICK_DIM[0], 2 * BRICK_DIM[1])
    W_VERTICES = [(W_LEFT-1, CEIL-1), (W_LEFT-1, FLOOR),
                  (W_RIGHT, FLOOR), (W_RIGHT, CEIL-1)]
    H_MOVE_RATE = 100  # pixels per sec
    FALL_SPEED = 20  # pixels per sec
    DIVE_SPEED = 300  # pixels per sec
    L_DIMS = (W_RIGHT-W_LEFT, BRICK_DIM[1])
    L_NUM_BRICKS = L_DIMS[0] // BRICK_DIM[0]
    FPS = 60
