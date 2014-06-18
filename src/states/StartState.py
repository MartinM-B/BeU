import pyglet
from src.Messenger.PyMessage import PyMessage
from .. import gui_resources
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
            settingsMessage = PyMessage(self._type, States.Settings)
            self._messenger.send(settingsMessage)
        elif anID == 'fight':
            print 'do something'
            charMessage = PyMessage(self._type, States.CharSelect)
            self._messenger.send(charMessage)

    def onExit(self):
        print 'onExit'
        if self.isActive:
            self.deleteScreen()
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

        self.background_sprite = pyglet.sprite.Sprite(gui_resources.creditBackground, 0, 0, batch=self._batch, group=self._background)

        self.creditButton = PyButton('credits', self, point1, self._batch, button_res, button_res_active, self._foreground,
                                'Credits')
        self.settingsButton = PyButton('settings', self, point2, self._batch, button_res, button_res_active,
                                  self._foreground, 'Settings')
        self.gameButton = PyButton('fight', self, point3, self._batch, button_res, button_res_active, self._foreground,
                              'Fight')
        self.gameButton.setActive(True)
        layouter.addButton(self.creditButton)
        layouter.addButton(self.settingsButton)
        layouter.addButton(self.gameButton)

        self._layouter = layouter

    def deleteScreen(self):
        self.creditButton.delete()
        self.settingsButton.delete()
        self.gameButton.delete()
        self.background_sprite.delete()

    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)