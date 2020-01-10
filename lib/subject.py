import pygame

pygame.init()


class Subject:

    def __init__(self):
        self.topics = [{} for _ in range(pygame.NUMEVENTS)]

    def notify(self, event):
        observers = self.topics[event.type]
        if bool(observers):
            for observer in observers.values():
                observer(**event.__dict__)

    def subscribe(self, event, callback):
        callback_dict = self.topics[event.type]
        callback_dict[callback.__name__] = callback

    def unsubscribe(self):
        self.topics = [{} for _ in range(pygame.NUMEVENTS)]
