__author__ = 'win8'

from InputHandler import InputHandler
from src.Player import *
from abc import ABCMeta, abstractmethod
from pyglet.window import key

class PlayerInputHandler(InputHandler):
    def __init__(self, player):
        self.player = player

    @abstractmethod
    def checkWalkLeft(self, symbol):
        pass
    @abstractmethod
    def checkWalkRight(self, symbol):
        pass
    @abstractmethod
    def checkDuck(self, symbol):
        pass
    @abstractmethod
    def checkJump(self, symbol):
        pass
    @abstractmethod
    def checkKick(self, symbol):
        pass
    @abstractmethod
    def checkPunch(self, symbol):
        pass
    @abstractmethod
    def checkBlock(self, symbol):
        pass
    @abstractmethod
    def checkDance(self, symbol):
        pass

    def handleKeyPress(self, symbol, modifiers):
        if self.checkWalkLeft(symbol):
            self.player.look(Direction.Left)
            self.player.startMoving()

        if self.checkWalkRight(symbol):
            self.player.look(Direction.Right)
            self.player.startMoving()

        if self.checkJump(symbol):
            self.player.jump()

        if self.checkDance(symbol):
            self.player.dance()

        if self.checkKick(symbol):
            self.player.kick()

        if self.checkPunch(symbol):
            self.player.punch()

        if self.checkBlock(symbol):
            self.player.startBlocking()

        if self.checkDuck(symbol):
            self.player.duck()

    def handleKeyRelease(self, symbol, modifiers):
        #global moveFlag
        if self.checkWalkLeft(symbol):
            self.player.stopMoving()

        if self.checkWalkRight(symbol):
            self.player.stopMoving()

        if self.checkBlock(symbol):
            self.player.stopBlocking()

        if self.checkDuck(symbol):
            self.player.stopDucking()