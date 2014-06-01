__author__ = 'florian'
from pyglet.window import Window
from src.InputHandling.InputHandler import *


# class to handle the inputs to select the buttons and to switch between them


class PyLayouter(InputHandler):

    def __init__(self, window):
        self.window = window

    def handleKeyPress(self, symbol, modifiers):
        print 'key pressed'

    def handleKeyRelease(self, symbol, modifiers):
        print 'key released'
