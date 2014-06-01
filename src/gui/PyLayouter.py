__author__ = 'florian'
from pyglet.window import Window
from src.InputHandling.InputHandler import *


class PyLayouter(InputHandler):

    def __init__(self, window):
        self.window = window

    def handleKeyPress(self, symbol, modifiers):
        print 'key pressed'

    def handleKeyRelease(self, symbol, modifiers):
        print 'key released'
