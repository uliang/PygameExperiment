import sys
import os

import pygame
import pygame.display as display
import pygame.draw as draw
import pygame.sprite as sprite
import pygame.event as event

import rx.operators as ops
from rx import create
from rx.core.typing import Observer

from game_objects.configuration import Configuration
from game_objects.event_loop import EventLoop
from game_objects.surface_loader import yield_random_surface
from game_objects.tile_factory import TileFactory
from game_objects.brick_factory import brick_factory
from game_objects.tile import Tile
from game_objects.brick import Brick
from game_objects.boundary import Boundary
from game_objects.heap import Heap
from game_objects.event_handlers import *
import game_objects.tile_shapes as tile_shapes

from game_systems.events import NEWTILE
from game_systems.utils import yield_random


def main(cfg=Configuration):
    pygame.init()
    background = display.set_mode((cfg.S_WIDTH, cfg.S_HEIGHT))
    background.fill(cfg.S_COLOR)
    display.set_caption(cfg.S_CAPTION)
    draw.polygon(background, cfg.B_LINE_COLOR,
                 points=cfg.W_VERTICES, width=1)

    event_loop = EventLoop(cfg.FPS)
    event_stream = create(event_loop).pipe(
        ops.publish())

    heap = Heap(background)
    floor = Boundary(cfg.FLOOR_DIM, heap)
    right_wall = Boundary(cfg.W_RIGHT_DIM, heap)
    left_wall = Boundary(cfg.W_LEFT_DIM, heap)

    shapes = yield_random(
        [shpf for shpn, shpf in tile_shapes.__dict__.items() if 'make' in shpn])
    surfaces = yield_random_surface(cfg.ASSET_PATH, [
        path for path in os.listdir('./assets') if 'brick.png' in path],
        brick_dim=cfg.BRICK_DIM)

    tile = Tile(background)
    initial_rect = pygame.Rect(
        (cfg.W_CENTER, cfg.CEIL), cfg.BRICK_DIM)
    bricks = brick_factory(
        surfaces, shapes, cfg.FPS, initial_rect)
    tile_factory: Observer = TileFactory(tile, bricks)

    # convenience variables for collision detection
    left, bottom, right = ((-1, 0), (0, 1), (1, 0))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.QUIT))\
        .subscribe(on_next=lambda x: sys.exit())

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == NEWTILE)) \
        .subscribe(tile_factory)

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == NEWTILE)) \
        .subscribe(on_next=handle_fall(tile, cfg.FALL_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_s)) \
        .subscribe(on_next=handle_fall(tile, cfg.DIVE_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_a),
        ops.map(lambda x: tile),
        ops.filter(lambda x: not heap.did_collide(left)(x)))\
        .subscribe(on_next=handle_move(-cfg.HORIZONTAL_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_d),
        ops.map(lambda x: tile),
        ops.filter(lambda x: not heap.did_collide(right)(x)))\
        .subscribe(on_next=handle_move(cfg.HORIZONTAL_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_SPACE))\
        .subscribe(on_next=handle_rotation((cfg.W_LEFT, cfg.CEIL), cfg.BRICK_WIDTH, tile, heap))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYUP)) \
        .subscribe(on_next=handle_fall(tile, cfg.FALL_SPEED))

    event_stream.pipe(
        ops.map(lambda x: tile),
        ops.filter(heap.did_collide(bottom))) \
        .subscribe(on_next=handle_landing(heap))

    event_stream.pipe(
        ops.map(lambda x: tile),
        ops.filter(heap.did_collide(right)),
        ops.filter(lambda x: x.v_x > 0)) \
        .subscribe(on_next=handle_stop)

    event_stream.pipe(
        ops.map(lambda x: tile),
        ops.filter(heap.did_collide(left)),
        ops.filter(lambda x: x.v_x < 0)) \
        .subscribe(on_next=handle_stop)

    event_stream.pipe(
        ops.map(lambda x: x.frame)) \
        .subscribe(on_next=lambda x: [actor.update(x) for actor in (tile, heap)])

    event_stream.subscribe(on_next=print)

    event.post(event.Event(NEWTILE))
    event_stream.connect()


if __name__ == '__main__':
    main()
