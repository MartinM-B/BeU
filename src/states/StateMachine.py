__author__ = 'florian'

from State import *
from src.Messenger.Receiver import *
from StateEnum import *
from StartState import *
from CreditsState import *
from GameState import *
from CharSelectState import *


class StateMachine(State, Receiver):

    __states = {}
    _startState = StartState()
    _creditState = CreditsState()
    _gameState = GameState()
    _charSelectState = CharSelectState()

    def __init__(self, type):
        self._type = type
        self.__states = {self._startState, self._creditState, self._gameState, self._charSelectState}

    def onEnter(self):
        pass

    def onExit(self):
        pass

    def onReceive(self, msg):
        if msg.type == States.Start:
            self.setNotActive()
            self._startState.onEnter()
        elif msg.type == States.Credits:
            self.setNotActive()
            self._creditState.onEnter()
        elif msg.type == States.Game:
            self.setNotActive()
            self._gameState.onEnter()
        elif msg.type == States.CharSelect:
            self.setNotActive()
            self._charSelectState.onEnter()

    def setNotActive(self):
        for states in self.__states:
            states.setActive(False)
