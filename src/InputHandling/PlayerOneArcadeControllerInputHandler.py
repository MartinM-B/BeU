__author__ = 'win8'

from PlayerInputHandler import PlayerInputHandler
from pyglet.window import key

class PlayerOneArcadeControllerInputHandler(PlayerInputHandler):
    def checkWalkLeft(self, symbol):
        return key.LEFT == symbol

    def checkWalkRight(self, symbol):
        return key.RIGHT == symbol

    def checkDuck(self, symbol):
        return key.DOWN == symbol

    def checkJump(self, symbol):
        return key.UP == symbol

    def checkKick(self, symbol):
        return key.LCTRL == symbol

    def checkPunch(self, symbol):
        return key.LSHIFT == symbol

    def checkBlock(self, symbol):
        return key.SPACE == symbol

    def checkDance(self, symbol):
        return key._3 == symbol