__author__ = 'florian'


from State import *


class CharSelectState(State):
    
    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter Charselect"

    def handleKeyPress(self, symbol, modifiers):
        pass

    def handleKeyRelease(self, symbol, modifiers):
        pass