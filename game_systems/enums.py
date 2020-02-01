import enum


class Directions(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


class States(enum.Enum):
    DROPPING = enum.auto()
    MOVING_LEFT = enum.auto()
    MOVING_RIGHT = enum.auto()
    HEAVY = enum.auto()
    GROUNDED = enum.auto()
