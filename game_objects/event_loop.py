from itertools import cycle
from collections import namedtuple

from rx import create
from rx.operators import publish
from rx.core.typing import Observer

import pygame.display as display
import pygame.event as event
from pygame.time import Clock

from game_objects.application_config import ApplicationConfig as config
from game_systems.events import IDLE

fps = config.FPS
event_object = namedtuple('EventObject', ['frame', 'event'])


def event_loop(observer: Observer, scheduler):
    clock = Clock()
    frame_counter = cycle(range(-1, fps-1))

    while True:
        clock.tick(fps)
        frame = next(frame_counter)
        event_list = event.get()
        if not bool(event_list):
            observer.on_next(event_object(frame, event.Event(IDLE)))
        else:
            for event_ in event_list:
                observer.on_next(event_object(frame, event_))

        display.flip()
