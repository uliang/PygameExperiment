import random
from typing import Sequence, Callable, TypeVar, Iterator
from toolz.functoolz import curry

from game_objects.brick import Brick

T = TypeVar('T')


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
