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
    CEIL = S_HEIGHT // 5 
    DROP_HEIGHT = 10 