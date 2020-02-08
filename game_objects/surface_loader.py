from typing import Iterator, Sequence, Tuple
import os
import random

import pygame
import pygame.image as image
import pygame.transform as transform


def yield_random_surface(asset_path: str, path_arr: Sequence[str], brick_dim: Tuple[int, int]) -> Iterator[pygame.Surface]:
    while True:
        image_path = random.choice(path_arr)
        path_to_image = os.path.join(asset_path, image_path)
        brick_surf = image.load(path_to_image)
        brick_surf = transform.scale(brick_surf, brick_dim)
        yield brick_surf
