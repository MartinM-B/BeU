__author__ = 'florian'


from State import *


class StartState(State):

    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter Start"