__author__ = 'florian'
from pyglet.window import Window
from src.InputHandling.InputHandler import *
from pyglet.window import key
from PyButton import *


# class to handle the inputs to select the buttons and to switch between them


class PyLayouter(InputHandler):

    def __init__(self, window):
        self.window = window
        self.buttons = []

    def addButton(self, button):
        self.buttons.append(button)

    def handleKeyPress(self, symbol, modifiers):
        print 'key pressed'
        if symbol == key.DOWN:
            temp = 0
            for b in self.buttons:
                if b.active:
                    if temp + 1 < len(self.buttons):
                        b.active = False
                        self.buttons[temp + 1].active = True
                elif not b.active:
                    temp += 1

        if symbol == key.UP:
            temp = 0
            for b in self.buttons:
                if b.active:
                    if temp - 1 >= 0:
                        b.active = False
                        self.buttons[temp - 1].active = True
                elif not b.active:
                    temp -= 1

        #TODO: find the right key
        if symbol == key.ENTER:
            for b in self.buttons:
                if b.active:
                    b.onClick()

    def handleKeyRelease(self, symbol, modifiers):
        print 'key released'
