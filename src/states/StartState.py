import pyglet
from pyglet.window import key
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

        scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 3

        point1 = PyPoint(170 + 20 * 1/scaleY, 150)
        point2 = PyPoint(170 + 20 * 1/scaleY, 280)
        point3 = PyPoint(170 + 20 * 1/scaleY, 410)

        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.startScreen.width * scaleY) / 2.0)

        self.backgroundBack = pyglet.graphics.OrderedGroup(-1)

        self.background_spriteBack = pyglet.sprite.Sprite(gui_resources.creditBackground, 0, 0, batch=self._batch, group=self.backgroundBack)
        self.background_spriteBack.scale = 1.3

        self.background_sprite = pyglet.sprite.Sprite(gui_resources.startScreen, spritePosX, 0, batch=self._batch,
                                                      group=self._background)
        self.background_sprite.scale = scaleY

        self.creditButton = PyButton('credits', self, point1, self._batch, button_res, button_res_active,
                                     self._foreground,
                                     'Credits')
        self.settingsButton = PyButton('settings', self, point2, self._batch, button_res, button_res_active,
                                       self._foreground, 'Settings')
        self.gameButton = PyButton('fight', self, point3, self._batch, button_res, button_res_active, self._foreground,
                                   'Fight')
        scaleY = 0.7

        self.creditButton.setScale(scaleY)
        self.creditButton._scale = scaleY
        self.settingsButton.setScale(scaleY)
        self.settingsButton._scale = scaleY
        self.gameButton.setScale(scaleY)
        self.gameButton._scale = scaleY
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