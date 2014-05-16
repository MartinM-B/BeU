__author__ = 'florian'

from State import *
from src.Messenger.receiver import *


class StateMachine(State, Receiver):

    __states = {}

    def onEnter(self):
        pass

    def onReceive(self):
        pass

    def onExit(self):
        pass