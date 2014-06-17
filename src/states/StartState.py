from src.gui.PyLayouter import PyLayouter

__author__ = 'florian'


from State import *
from src.gui.PyClickListener import *


class StartState(State, PyClickListener):

    def onClick(self, anID):
        if anID == "Button1":
            print 'do something'
        elif anID == "Button2":
            print 'do something else'

    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        self.initalizeState()
        print "onEnter Start"

    def initalizeState(self):
        print 'init all the buttons'
        # make layouter
        # make all the buttons
        # add the buttons to the layouter
        # this state is the listener for all the created buttons in this state
        # react to all the buttons in the onClick
        #self._layouter = PYLAYOUTER()

    def handleKeyPress(self, symbol, modifiers):
        print 'bla'
        #self._layouter.handldeKeyPressed(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'bla'
        #self._layouter.handldeKeyReleased(symbol, modifiers)