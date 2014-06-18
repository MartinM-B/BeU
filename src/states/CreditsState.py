from pyglet.window import key, pyglet
from .. import gui_resources
from ..InputHandling.PlayerOneKeyboardInputHandler import PlayerOneKeyboardInputHandler
from ..Messenger.PyMessage import PyMessage
from ..states.StateEnum import States

__author__ = 'florian'


from State import *

class CreditsState(State):
    
    def onExit(self):
        if self.isActive:
            self._active = False
        self.display_sprite.delete()
        self.background_sprite.delete()

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter CreditState"

        self.inputHandler = PlayerOneKeyboardInputHandler("")
        scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 1.5
        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.creditScreen.width * scaleY) / 2.0)
        self.display_sprite = pyglet.sprite.Sprite(gui_resources.creditScreen, spritePosX, 0, batch=self._batch, group=self._foreground)
        self.display_sprite.scale = scaleY
        self.background_sprite = pyglet.sprite.Sprite(gui_resources.creditBackground, 0, 0, batch=self._batch, group=self._background)
        self.background_sprite.scale = scaleY

    def handleKeyPress(self, symbol, modifiers):
        print 'credit state pressed'

    def handleKeyRelease(self, symbol, modifiers):
        if key.BACKSPACE == symbol:
            startScreen = PyMessage(self._type, States.Start)
            self._messenger.send(startScreen)
