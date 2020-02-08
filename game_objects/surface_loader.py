from typing import Iterator, Sequence
import os
import random

import pygame
import pygame.image as image
import pygame.transform as transform

from game_objects.application_config import ApplicationConfig


def brick_surface_gen(config: ApplicationConfig, path_arr: Sequence[str]) -> Iterator[pygame.Surface]:
    while True:
        image_path = random.choice(path_arr)
        path_to_image = os.path.join(config.ASSET_PATH, image_path)
        brick_surf = image.load(path_to_image)
        brick_surf = transform.scale(brick_surf, config.BRICK_DIM)
        yield brick_surf
