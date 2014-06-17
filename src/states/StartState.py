from src.gui import gui_resources
from src.gui.PyButton import PyButton
from src.gui.PyLayouter import PyLayouter
from src.gui.PyPoint import PyPoint

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
        # make layouter
        # make all the buttons
        # add the buttons to the layouter
        # this state is the listener for all the created buttons in this state
        # react to all the buttons in the onClick
        #self._layouter = PYLAYOUTER()
        print 'init all the buttons'
        layouter = PyLayouter()
        creditButton_res = gui_resources.box
        creditButton_res_active = gui_resources.box_selected
        point1 = PyPoint(50, 50)
        creditButton = PyButton('credits', self, point1, self._batch, creditButton_res, creditButton_res_active, self._foreground)



    def handleKeyPress(self, symbol, modifiers):
        print 'bla'
        #self._layouter.handldeKeyPressed(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'bla'
        #self._layouter.handldeKeyReleased(symbol, modifiers)