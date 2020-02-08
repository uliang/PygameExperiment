import sys
import os

import pygame
import pygame.draw as draw
import pygame.sprite as sprite

from rx import create
import rx.operators as ops

import game_objects.tile_shapes as shapes
from game_objects import Application, event_loop
from game_objects import ApplicationConfig as config
from game_objects.surface_loader import brick_surface_gen
from game_objects.tile_factory import TileFactory
from game_objects.tile import Tile
from game_objects.brick import Brick

from game_systems.events import NEWTILE
from game_systems.utils import yield_random


def main(config=config):
    pygame.init()
    event_stream = create(event_loop).pipe(
        ops.publish()
    )
    app = Application(config, event_stream)

    background = app.screen
    draw.polygon(background, config.B_LINE_COLOR,
                 points=config.W_VERTICES, width=1)

    shape = yield_random(
        [shpf for shpn, shpf in shapes.__dict__.items() if 'make' in shpn])
    brick_surface = brick_surface_gen(config, [
        path for path in os.listdir('./assets') if 'brick.png' in path])

    heap = sprite.Group()
    tile = Tile(background)
    tile_factory = TileFactory(config, brick_surface, shape, tile, Brick)

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.QUIT))\
        .subscribe(on_next=lambda x: sys.exit())

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == NEWTILE)) \
        .subscribe(tile_factory)

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == NEWTILE)) \
        .subscribe(on_next=tile.drop(config.FALL_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_s)) \
        .subscribe(on_next=tile.drop(config.DIVE_SPEED))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_a))\
        .subscribe(on_next=tile.move(-config.H_MOVE_RATE))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYDOWN),
        ops.filter(lambda x: x.event.key == pygame.K_d))\
        .subscribe(on_next=tile.move(config.H_MOVE_RATE))

    event_stream.pipe(
        ops.filter(lambda x: x.event.type == pygame.KEYUP)) \
        .subscribe(on_next=tile.drop(config.FALL_SPEED))

    event_stream.pipe(
        ops.map(lambda x: x.frame)) \
        .subscribe(on_next=tile.update)

    event_stream.subscribe(on_next=print)

    app.run_forever()


if __name__ == '__main__':
    main()
