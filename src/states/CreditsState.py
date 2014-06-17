from pyglet.window import key

__author__ = 'florian'


from State import *


class CreditsState(State):
    
    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter CreditState"

    def handleKeyPress(self, symbol, modifiers):
        print 'credit state pressed'

    def handleKeyRelease(self, symbol, modifiers):
        pass