import abc
from abc import ABC


class AbstractView(ABC):

    @abc.abstractmethod
    def render(self):
        """ Implement this method to update screen. This method 
            should return nothing and should call pygame.display.flip
        """


class AbstractManager(ABC):

    @classmethod
    @abc.abstractmethod
    def register(cls, obj):
        """ Implement this method to save instance to static variable 
            of manager. 
        """

    @classmethod
    @abc.abstractmethod
    def provide(cls):
        """ Implement this method to return saved instance. 
        """
