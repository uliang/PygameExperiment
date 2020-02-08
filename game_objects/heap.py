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
                    sprite_pos1 = Vector2(sprite1.rect.topleft)
                    sprite_pos2 = Vector2(sprite2.rect.topleft)
                    positional_offset = sprite_pos2 - \
                        sprite_pos1 + Vector2(offset)

                    # arguments to overlap method are list[int, int]
                    x_, y_ = positional_offset
                    positional_offset = [int(x_), int(y_)]

                    overlap = sprite1.mask.overlap(
                        sprite2.mask, positional_offset)
                    return bool(overlap)

                collision_dict = sprite.groupcollide(
                    self, tile, False, False, _collided)
                collisions.append(bool(collision_dict))
            return any(collisions)
        return callback
