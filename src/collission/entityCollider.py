__author__ = 'david_000'
from collide import *


class EntityCollider:
    def __init__(self, sprite):
         # create a collision structure for this sprite
        self.collision = SpriteCollision(sprite)

    def cache_collission_image(self):
        self.collision.cache_images()

    def collides_with(self, other_object):
        return collide(self.collision, other_object.collision)