__author__ = 'win8'

from PlayerInputHandler import PlayerInputHandler
from pyglet.window import key

class PlayerTwoKeyboardInputHandler(PlayerInputHandler):
    def checkWalkLeft(self, symbol):
        return key.A == symbol

    def checkWalkRight(self, symbol):
        return key.D == symbol

    def checkDuck(self, symbol):
        return key.S == symbol

    def checkJump(self, symbol):
        return key.W == symbol

    def checkKick(self, symbol):
        return key.F == symbol

    def checkPunch(self, symbol):
        return key.G == symbol

    def checkBlock(self, symbol):
        return key.H == symbol

    def checkDance(self, symbol):
        return key.R == symbol

    def checkSpecialAttack(self, symbols):
        length = len(symbols)
        if(length < 4):
            return False
        if(self.checkJump(symbols[length - 1]) and self.checkKick(symbols[length - 2]) and self.checkPunch(symbols[length - 3]) and self.checkKick(symbols[length - 4])):
            return True
        return False