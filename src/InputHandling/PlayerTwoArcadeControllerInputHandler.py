__author__ = 'win8'

from PlayerInputHandler import PlayerInputHandler
from pyglet.window import key

class PlayerTwoArcadeControllerInputHandler(PlayerInputHandler):
    def checkWalkLeft(self, symbol):
        return key.NUM_4 == symbol

    def checkWalkRight(self, symbol):
        return key.NUM_6 == symbol

    def checkDuck(self, symbol):
        return key.NUM_2 == symbol

    def checkJump(self, symbol):
        return key.NUM_8 == symbol

    def checkKick(self, symbol):
        return key.A == symbol

    def checkPunch(self, symbol):
        return key.W == symbol

    def checkBlock(self, symbol):
        return key.Q == symbol

    def checkDance(self, symbol):
        return key._4 == symbol