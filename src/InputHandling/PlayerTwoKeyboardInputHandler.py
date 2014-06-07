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
        if(length < 3):
            return False
        if(symbols[length - 1] == key.F and symbols[length - 2] == key.G and symbols[length - 3] == key.F):
            return True
        return False