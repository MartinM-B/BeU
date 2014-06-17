from src.InputHandling.InputHandler import InputHandler
from src.gui.PyLayouter import PyLayouter

__author__ = 'florian'
from abc import ABCMeta, abstractmethod

"""abstract state class """


class State(InputHandler):

    __metaclass__ = ABCMeta

    def __init__(self, aBatch, aBackground, aForeground, aWindow, aType, aMessenger):
        self._active = False
        self._layouter = PyLayouter()
        self._window = aWindow
        self._batch = aBatch
        self._background = aBackground
        self._foreground = aForeground
        self._type = aType
        self._messenger = aMessenger

    @abstractmethod
    def onEnter(self):
        pass

    @abstractmethod
    def onExit(self):
        pass

    @property
    def isActive(self):
        return self._active

    def handleKeyPress(self, symbol, modifiers):
        pass

    def handleKeyRelease(self, symbol, modifiers):
        pass