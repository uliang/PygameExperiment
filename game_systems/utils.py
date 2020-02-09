import random
from typing import Sequence, Callable, TypeVar, Iterator, Tuple, Dict
from toolz.functoolz import curry

from game_objects.brick import Brick

T = TypeVar('T')
U = TypeVar('U')


def argwhere(arr: Sequence[T], predicate: Callable[[T], bool]) -> Sequence[int]:
    ''' Returns indices of sequence where predicate is true '''

    return [i for i, x in enumerate(arr) if predicate(x)]


@curry
def isval(val: T, x: T) -> bool:
    return val == x


@curry
def pluck_object(arr: Sequence, index_arr: Sequence[int], key: str):
    ''' Returns list of objects whose key is in index_arr '''
    return [obj for obj in arr if getattr(obj, key) in index_arr]


def yield_random(arr: Sequence[T]) -> Iterator[T]:
    ''' Yields a random object from sequence of of objects '''
    while True:
        yield random.choice(arr)


def eraser(color):
    ''' Callback to use in group.clear method '''
    def callback(surf, rect):
        surf.fill(color, rect)
    return callback


def rotator(center: Tuple[int, int], vertex: Tuple[int, int]) -> Tuple[int, int]:
    ''' Returns coordinates of vertex after being acted upon by: aff(a,b) * rot(90) * aff(-a,-b)'''
    a, b = center
    x, y = vertex
    return (a-b+y, a+b-x)


def grid_centroid(well_offset, grid_spacing, bricks: Sequence[Brick], ) -> Tuple[int, int]:
    ''' Returns nearest grid point to the centroid of tile '''
    left, top = well_offset
    rect1, *other_rects = [brick.rect for brick in bricks]
    tile_rect = rect1.unionall(other_rects)
    xbar, ybar = tile_rect.center
    xbar, ybar = xbar-left, ybar-top
    xbar, ybar = left + (xbar//grid_spacing) * \
        grid_spacing, top + (ybar//grid_spacing)*grid_spacing
    return xbar, ybar


@curry
def reduce_dictionary_by_value(predicate: Callable[[U], bool], dictionary: Dict[T, U]) -> Dict[T, U]:
    ''' Returns only key-value mapping which satisfies predicate(value)'''
    rdict = {}
    for t, u in dictionary.items():
        if predicate(u):
            rdict[t] = u
    return rdict
