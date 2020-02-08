from pygame import Rect
from pygame.event import post, Event
from game_systems.events import NEWTILE
from game_objects.tile import Tile
from game_objects.heap import Heap
from game_systems.utils import rotator, grid_centroid


def handle_landing(heap: Heap):
    def callback(tile: Tile):
        tile('land')
        heap.add(*tile.sprites())
        tile.empty()
        post(Event(NEWTILE))
    return callback


def handle_move(speed: int):
    def callback(tile: Tile):
        tile('move', speed)
    return callback


def handle_stop(tile: Tile):
    tile('stop')


def handle_fall(tile, speed):
    def callback(event_object):
        tile('stop')
        tile('fall', speed)
    return callback


def handle_rotation(well_offset, grid_spacing, tile, heap):
    def callback(event_object):
        rotation_center = grid_centroid(
            well_offset, grid_spacing, tile.sprites())
        for brick in iter(tile):
            rotated_vertices = []
            for vertexname in ['topleft', 'topright', 'bottomleft', 'bottomright']:
                vertex = getattr(brick.rect, vertexname)
                rvertex = rotator(rotation_center, vertex)
                rotated_vertices.append(rvertex)

            coord1, coord2 = zip(*rotated_vertices)
            left, top = min(coord1), min(coord2)
            rotated_rect = Rect((left, top), (grid_spacing, grid_spacing))

            # prevent tile from creeping upwards with repeated rotations
            rotated_rect.move_ip((0, grid_spacing))
            brick.rect = rotated_rect

        if heap.did_collide((0, 0))(tile):  # ensure that tiles don't rotate into a heap
            for brick in iter(tile):
                brick.rect.move_ip((0, -grid_spacing))
    return callback
