from collections import namedtuple
from lib.base import AbstractManager


class Event(AbstractManager):
    subject = None

    @classmethod
    def register(cls, subject):
        cls.subject = subject

    @classmethod
    def provide(cls):
        return cls.subject


class Scenes(AbstractManager):
    scene_classes = {}
    scenes = {} 

    @classmethod
    def register(cls, scenes):
        cls.scene_classes.update(dict(scenes))

    @classmethod
    def provide(cls, scene_name):
        scene = cls.scenes.get(scene_name)
        if scene is None:
            scene = cls.scene_classes[scene_name]()
            cls.scenes[scene_name] = scene
        return scene


class Window(AbstractManager):
    _window = namedtuple('window', ['screen', 'background'])
    window = None

    @classmethod
    def register(cls, screen, background):
        cls.window = cls._window(screen, background)

    @classmethod
    def provide(cls):
        return cls.window
