__author__ = 'win8'
from abc import ABCMeta, abstractmethod

class InputHandler():
    __metaclass__ = ABCMeta

    @abstractmethod
    def handleKeyPress(self, symbol, modifiers):
        pass

    @abstractmethod
    def handleKeyRelease(self, symbol, modifiers):
        pass