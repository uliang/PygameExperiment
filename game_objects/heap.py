import pygame.sprite as sprite
from pygame.math import Vector2
from pygame.event import post, Event
from game_systems.events import NEWTILE
from game_systems.utils import eraser


class Heap(sprite.Group):
    def __init__(self, background, *sprites):
        super().__init__(*sprites)
        self.background = background

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.clear(self.background, eraser(self.background.get_at((0, 0))))
        self.draw(self.background)

    def did_collide(self, *directions):
        def callback(tile) -> bool:
            collisions = []
            for offset in directions:
                def _collided(sprite1, sprite2):
                    x1, y1 = sprite1.rect.topleft
                    x2, y2 = sprite2.rect.topleft
                    x0, y0 = offset
                    positional_offset = (x2-x1+x0, y2-y1+y0)

                    overlap = sprite1.mask.overlap(
                        sprite2.mask, positional_offset)
                    return bool(overlap)

                collision_dict = sprite.groupcollide(
                    self, tile, False, False, _collided)
                collisions.append(bool(collision_dict))
            return any(collisions)
        return callback
