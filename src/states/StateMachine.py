from src.InputHandling.InputHandler import InputHandler

__author__ = 'florian'

from State import *
from src.Messenger.Receiver import *
from StateEnum import *
from StartState import *
from CreditsState import *
from GameState import *
from CharSelectState import *


class StateMachine(State, Receiver, InputHandler):

    __states = {}
    # _startState = StartState()
    # _creditState = CreditsState()
    # _gameState = GameState()
    # _charSelectState = CharSelectState()

    def __init__(self, type, aBatch, aGroup):
        self._type = type
        self._startState = StartState(aBatch, aGroup)
        self._creditState = StartState(aBatch, aGroup)
        self._gameState = StartState(aBatch, aGroup)
        self._charSelectState = StartState(aBatch, aGroup)

        self.__states = {self._startState, self._creditState, self._gameState, self._charSelectState}

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onReceive(self, message):
        if message.msg == States.Start:
            self.setNotActive()
            self._startState.onEnter()
        elif message.msg == States.Credits:
            self.setNotActive()
            self._creditState.onEnter()
        elif message.msg == States.Game:
            self.setNotActive()
            self._gameState.onEnter()
        elif message.msg == States.CharSelect:
            self.setNotActive()
            self._charSelectState.onEnter()

    def setNotActive(self):
        for states in self.__states:
            states._active = False

    def handleKeyPress(self, symbol, modifiers):
        for state in self.__states:
            if state.isActive:
                state.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        for state in self.__states:
            if state.isActive:
                state.handleKeyRelease(symbol, modifiers)


