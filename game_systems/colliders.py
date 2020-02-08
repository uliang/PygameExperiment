from pygame.math import Vector2
from pygame.sprite import Sprite


def collision_callback_factory(offset: Vector2):
    def callback(sprite1: Sprite, sprite2: Sprite):
        sprite_pos1 = Vector2(*sprite1.rect.topleft)
        sprite_pos2 = Vector2(*sprite2.rect.topleft)
        positional_offset = sprite_pos2 - sprite_pos1
        positional_offset += offset
        overlap = sprite1.mask.overlap(sprite2.mask, positional_offset)
        return bool(overlap)
    return callback
