from itertools import cycle
from collections import namedtuple

from rx.core.typing import Observer

import pygame.display as display
import pygame.event as event
from pygame.time import Clock

from game_systems.events import IDLE


event_object = namedtuple('EventObject', ['frame', 'event'])


class EventLoop:
    def __init__(self, fps):
        self.fps = fps

    def __call__(self, observer: Observer, scheduler):
        clock = Clock()
        frame_counter = cycle(range(-1, self.fps-1))

        while True:
            clock.tick(self.fps)
            frame = next(frame_counter)
            event_list = event.get()
            if not bool(event_list):
                observer.on_next(event_object(frame, event.Event(IDLE)))
            else:
                for event_ in event_list:
                    observer.on_next(event_object(frame, event_))

            display.flip()
