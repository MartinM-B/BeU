__author__ = 'win8'

from PlayerInputHandler import PlayerInputHandler
from pyglet.window import key

class PlayerTwoArcadeControllerInputHandler(PlayerInputHandler):
    def checkWalkLeft(self, symbol):
        return key.D == symbol

    def checkWalkRight(self, symbol):
        return key.G == symbol

    def checkDuck(self, symbol):
        return key.F == symbol

    def checkJump(self, symbol):
        return key.R == symbol

    def checkKick(self, symbol):
        return key.A == symbol

    def checkPunch(self, symbol):
        return key.W == symbol

    def checkBlock(self, symbol):
        return key.Q == symbol

    def checkDance(self, symbol):
        return key._4 == symbol