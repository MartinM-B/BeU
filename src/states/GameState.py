__author__ = 'florian'


from State import *


class GameState(State):
    
    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter Game"