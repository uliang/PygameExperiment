import os
from pygame.color import Color


class Configuration:
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
    BRICK_WIDTH = BRICK_DIM[0]
    BRICK_HEIGHT = BRICK_DIM[1]
    FLOOR = CEIL + DROP_HEIGHT * BRICK_DIM[1]
    W_LEFT = W_CENTER - 6 * BRICK_DIM[0]
    W_RIGHT = W_CENTER + 8 * BRICK_DIM[0]
    W_WIDTH = W_RIGHT - W_LEFT
    W_HEIGHT = FLOOR - CEIL
    W_VERTICES = [(W_LEFT-1, CEIL-1), (W_LEFT-1, FLOOR),
                  (W_RIGHT, FLOOR), (W_RIGHT, CEIL-1)]
    HORIZONTAL_SPEED = 220  # pixels per sec
    FALL_SPEED = 20  # pixels per sec
    DIVE_SPEED = 320  # pixels per sec
    L_DIMS = (W_RIGHT-W_LEFT, BRICK_DIM[1])
    L_NUM_BRICKS = L_DIMS[0] // BRICK_DIM[0]
    FPS = 60
    FLOOR_DIM = (W_LEFT, FLOOR, W_WIDTH, 1)
    W_RIGHT_DIM = (W_RIGHT, CEIL, 1, W_HEIGHT)
    W_LEFT_DIM = (W_LEFT-1, CEIL, 1, W_HEIGHT)
