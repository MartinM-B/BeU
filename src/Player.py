__author__ = 'david_000'
from gameEntity import *
import resources

class Player(GameEntity):
    def __init__(self, batch, group):
        super(Player, self).__init__(image=resources.starLeft, x=0, y=0, batch=batch, group=group)

