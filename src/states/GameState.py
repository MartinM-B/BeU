import pyglet

from src.Enum import checkEnumValueEquals
from src.Healthbar import healthbar
from src.InputHandling.PlayerOneKeyboardInputHandler import PlayerOneKeyboardInputHandler
from src.InputHandling.PlayerTwoKeyboardInputHandler import PlayerTwoKeyboardInputHandler
from src.Player import ActionState, Direction
from src.Symbiont import Symbiont
from src.Viking import Viking
from src.gui import gui_resources
from src.settings import Settings


__author__ = 'florian'


from State import *


class GameState(State):
    
    def onExit(self):
        if self.isActive:
            self._active = False
            self.deleteScreen()

        pyglet.clock.unschedule(self.update)

    def onEnter(self):
        if not self.isActive:
            self._active = True
        print "onEnter Game"

        settings = Settings()

        self.player = Viking(self._batch, self._foreground) if settings._player1 == 0 else Symbiont(self._batch, self._foreground)
        self.player.preloadImages()
        self.player2 = Viking(self._batch, self._foreground) if settings._player2 == 0 else Symbiont(self._batch, self._foreground)
        #player2 = Viking(batch, foreground)
        self.player2.preloadImages()
        self.player2.moveX(700)
        self.player2.look(Direction.Left)

        # scaleY = (self._window.height / (gui_resources.bg_underground.height * 1.0)) / 1.5
        # spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.bg_underground.width * scaleY) / 2.0)
        # self.background_sprite = pyglet.sprite.Sprite(gui_resources.bg_underground, spritePosX, 0, batch=self._batch,
        #                                               group=self._background)

        imagesLoaded = False

        #player2 = ChibiUsa_blue(batch, foreground)
        #player2.moveX(window.width / 2)
        self.healthbarObject = healthbar.HealthBar(self._batch, self._window, self.player, self.player2, self._messenger)

        #roundcounter = RoundCounter(batch, player, player2, 285, 400, 3)

        self.playerOneInputController = PlayerOneKeyboardInputHandler(self.player)
        self.playerTwoInputController = PlayerTwoKeyboardInputHandler(self.player2)

        pyglet.clock.schedule_interval(self.update, 1/30.0)

    def handleKeyPress(self, symbol, modifiers):
        print "a key was pressed"
        self.playerOneInputController.handleKeyPress(symbol, modifiers)
        self.playerTwoInputController.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print "a key was released"
        self.playerOneInputController.handleKeyRelease(symbol, modifiers)
        self.playerTwoInputController.handleKeyRelease(symbol, modifiers)

    def update(self, dt):
        #change sprite according to lookFlag
        #done in player update

        if self.player.getImagesPreloaded() == False:
            self.player.preloadImages()

        if self.player2.getImagesPreloaded() == False:
            self.player2.preloadImages()

        self.player.update()
        self.player2.update()


        if checkEnumValueEquals(self.player.actionState, ActionState.Attacking) and self.player.checkCollision(self.player2):
            print "Player Kollission"
            self.player2.playerHit(checkEnumValueEquals(self.player.lookDirection, Direction.Right) and Direction.Left or Direction.Right, self.player)

        if checkEnumValueEquals(self.player2.actionState, ActionState.Attacking) and self.player2.checkCollision(self.player):
            print "Player2 Kollission"
            self.player.playerHit(checkEnumValueEquals(self.player2.lookDirection, Direction.Right) and Direction.Left or Direction.Right, self.player2)

        self.healthbarObject.update()

    def deleteScreen(self):
        self.healthbarObject.delete()
        self.player.delete()
        self.player2.delete()
