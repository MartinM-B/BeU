__author__ = 'david_000'
from src.collission.collide import *


class EntityCollider:
    def __init__(self, sprite):
         # create a collision structure for this sprite
        self.collision = SpriteCollision(sprite)

    def collides_with(self, other_object):
        return collide(self.collision, other_object.collision)