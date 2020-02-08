from pygame import Rect
from game_objects.brick import Brick


def brick_factory(surface_generator, shape_generator, fps, rect):
    while True:
        initial_rect = Rect(rect.topleft, rect.size)
        bw = initial_rect.width
        surf = next(surface_generator)
        rects = next(shape_generator)
        for rect_ in rects(initial_rect, bw):
            yield Brick(surf, rect_, fps)
