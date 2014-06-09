__author__ = 'win8'

from InputHandler import InputHandler
from src.Player import *
from abc import ABCMeta, abstractmethod
import datetime

class PlayerInputHandler(InputHandler):
    def __init__(self, player):
        self.player = player
        self.symbollist = []
        self.lastTime = datetime.datetime.now()

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
    @abstractmethod
    def checkSpecialAttack(self, symbols):
        pass


    def handleKeyPress(self, symbol, modifiers):
        print symbol

        if (datetime.datetime.now() - self.lastTime).microseconds / 1000 > 750:
            self.symbollist = []

        self.lastTime = datetime.datetime.now()

        self.symbollist.append(symbol)

        if self.checkSpecialAttack(self.symbollist):
            self.player.useSpecialAttack()
            self.symbollist = []
            return

        if self.checkWalkLeft(symbol):
            self.player.look(Direction.Left)
            self.player.startMoving()
            return

        if self.checkWalkRight(symbol):
            self.player.look(Direction.Right)
            self.player.startMoving()
            return

        if self.checkJump(symbol):
            self.player.jump()
            return

        if self.checkDance(symbol):
            self.player.dance()
            return

        if self.checkKick(symbol):
            self.player.kick()
            return

        if self.checkPunch(symbol):
            self.player.punch()
            return

        if self.checkBlock(symbol):
            self.player.startBlocking()
            return

        if self.checkDuck(symbol):
            self.player.duck()
            return

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