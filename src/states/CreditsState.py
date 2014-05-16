__author__ = 'florian'


from State import *


class CreditsState(State):
    
    def onExit(self):
        if self.isActive:
            self.setActive(False)

    def onEnter(self):
        if not self.isActive:
            self.setActive(True)