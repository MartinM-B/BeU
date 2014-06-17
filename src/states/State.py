from src.gui.PyLayouter import PyLayouter

__author__ = 'florian'
from abc import ABCMeta, abstractmethod

"""abstract state class """


class State(object):

    __metaclass__ = ABCMeta

    def __init__(self, aBatch, aGroup):
        self._active = False
        self._layouter = PyLayouter()

    @abstractmethod
    def onEnter(self):
        pass

    @abstractmethod
    def onExit(self):
        pass

    @property
    def isActive(self):
        return self._active
