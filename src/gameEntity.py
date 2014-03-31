__author__ = 'david_000'
from src.collission.entityCollider import *
import pyglet


class GameEntity(object):
    def __init__(self, image, x, y, batch, group):
        self.display_sprite = pyglet.sprite.Sprite(image, x, y, batch=batch, group=group)
        self.collider = EntityCollider(self.display_sprite)

    def changeSpriteImage(self, image):
        self.display_sprite.image = image

    def setPosition(self, x, y):
        self.display_sprite.set_position(x, y)


    def moveX(self, x):
        self.display_sprite.x += x

    def moveY(self, y):
        self.display_sprite.y += y

    @property
    def x(self):
        return self.display_sprite.x

    @x.setter
    def x(self, value):
        self.display_sprite.x = value
        """ not working yet don't use """

    @property
    def y(self):
        return self.display_sprite.y

    @y.setter
    def y(self, value):
        self.display_sprite.y = value
        """ not working yet don't use """

    def checkCollision(self, other):
        return self.collider.collides_with(other.collider)