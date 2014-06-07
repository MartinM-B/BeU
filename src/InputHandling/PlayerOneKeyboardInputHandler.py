__author__ = 'win8'

from PlayerInputHandler import PlayerInputHandler
from pyglet.window import key

class PlayerOneKeyboardInputHandler(PlayerInputHandler):
    def checkWalkLeft(self, symbol):
        return key.LEFT == symbol

    def checkWalkRight(self, symbol):
        return key.RIGHT == symbol

    def checkDuck(self, symbol):
        return key.DOWN == symbol

    def checkJump(self, symbol):
        return key.UP == symbol

    def checkKick(self, symbol):
        return key.K == symbol

    def checkPunch(self, symbol):
        return key.J == symbol

    def checkBlock(self, symbol):
        return key.L == symbol

    def checkDance(self, symbol):
        return key.I == symbol

    def checkSpecialAttack(self, symbols):
        length = len(symbols)
        if(length < 3):
            return False
        if(symbols[length - 1] == key.K and symbols[length - 2] == key.J and symbols[length - 3] == key.K):
            return True
        return False