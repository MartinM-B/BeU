from src.Messenger.PyMessage import PyMessage
from src.gui import gui_resources
from src.gui.PyButton import PyButton
from src.gui.PyLayouter import PyLayouter
from src.gui.PyPoint import PyPoint
from src.states.StateEnum import States

__author__ = 'florian'

from State import *
from src.gui.PyClickListener import *


class StartState(State, PyClickListener):
    def onClick(self, anID):
        if anID == 'credits':
            print 'do something'
            creditsMessage = PyMessage(self._type, States.Credits)
            self._messenger.send(creditsMessage)
        elif anID == 'settings':
            print 'do something else'
            # settingsMessage = PyMessage(self._type, States.Settings)
            # self._messenger.send(settingsMessage)
        elif anID == 'fight':
            print 'do something'
            gameMessage = PyMessage(self._type, States.Game)
            self._messenger.send(gameMessage)

    def onExit(self):
        if self.isActive:
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        self.initalizeState()
        print 'onEnter Start'

    def initalizeState(self):
        # make layouter
        # make all the buttons
        # add the buttons to the layouter
        # this state is the listener for all the created buttons in this state
        # react to all the buttons in the onClick
        # self._layouter = PYLAYOUTER()
        print 'init all the buttons'
        layouter = PyLayouter()
        button_res = gui_resources.box
        button_res_active = gui_resources.box_selected
        point1 = PyPoint(50, 50)
        point2 = PyPoint(50, 180)
        point3 = PyPoint(50, 310)
        creditButton = PyButton('credits', self, point1, self._batch, button_res, button_res_active, self._foreground,
                                'Credits')
        settingsButton = PyButton('settings', self, point2, self._batch, button_res, button_res_active,
                                  self._foreground, 'Settings')
        gameButton = PyButton('fight', self, point3, self._batch, button_res, button_res_active, self._foreground,
                              'Fight')
        gameButton.setActive(True)
        layouter.addButton(creditButton)
        layouter.addButton(settingsButton)
        layouter.addButton(gameButton)

    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handldeKeyPressed(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)