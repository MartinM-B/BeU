__author__ = 'florian'
from pyglet.window import Window
from src.InputHandling.InputHandler import *
from pyglet.window import key
from PyButton import *


# class to handle the inputs to select the buttons and to switch between them


class PyLayouter(InputHandler):

    def __init__(self):
        self.buttons = []

    def addButton(self, button):
        self.buttons.append(button)

    def handleKeyPress(self, symbol, modifiers):
        if symbol == key.DOWN:
            for b in self.buttons:
                if b.active:
                    temp = self.buttons.index(b)
                    if temp - 1 >= 0:
                        b.setActive(False)
                        self.buttons[temp - 1].setActive(True)
                        break

        if symbol == key.UP:
            for b in self.buttons:
                if b.active:
                    temp = self.buttons.index(b)
                    if temp + 1 < len(self.buttons):
                        b.setActive(False)
                        self.buttons[temp + 1].setActive(True)
                        break

        #TODO: find the right key
        if symbol == key.ENTER:
            for b in self.buttons:
                if b.active:
                    b.onClick()

    def handleKeyRelease(self, symbol, modifiers):
        print ''
