import pygame
from application import Application
from lib.subject import Subject
from lib.window_factory import WindowFactory
import lib.manager
from views import *


def main():
    lib.manager.Scenes.register({
        'splash': Splash,
        'game': Game,
    })
    lib.manager.Event.register(Subject())
    window = WindowFactory()
    lib.manager.Window.register(window.screen, window.background)
    app = Application()
    app.run_forever()


if __name__ == '__main__':
    main()
