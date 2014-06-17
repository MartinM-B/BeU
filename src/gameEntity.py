__author__ = 'david_000'
from collission.entityCollider import *
import pyglet


class GameEntity(object):
    def __init__(self, image, x, y, batch, group):
        self.display_sprite = pyglet.sprite.Sprite(image, x, y, batch=batch, group=group)
        self.hitmask_sprite = pyglet.sprite.Sprite(image, x, y)
        self.collider = EntityCollider(self.display_sprite)
        self.hitmask = EntityCollider(self.hitmask_sprite)
        self.attackmask_sprite = pyglet.sprite.Sprite(image, x, y)
        self.attackmask = EntityCollider(self.attackmask_sprite)

    def changeSpriteImage(self, image):
        print "change sprite only"
        self.display_sprite.image = image
        self.hitmask_sprite.image = image
        self.collider = EntityCollider(self.display_sprite)
        self.hitmask = EntityCollider(self.hitmask_sprite)

    def changeSpriteImageWithMask(self, image, hitmask):
        print "change sprite and hitmask"
        self.display_sprite.image = image
        self.hitmask_sprite.image = hitmask
        self.collider = EntityCollider(self.display_sprite)
        self.hitmask = EntityCollider(self.hitmask_sprite)

    def changeHitmaskImage(self, image):
        print "change hitmask only"
        self.hitmask_sprite.image = image
        self.hitmask = EntityCollider(self.hitmask_sprite)

    def changeAttackmaskImage(self, image):
        print "change attackmask only"
        #self.display_sprite.image = image #testing (show attackmask)
        self.attackmask_sprite.image = image
        self.attackmask = EntityCollider(self.attackmask_sprite)

    def setPosition(self, x, y):
        self.display_sprite.set_position(x, y)
        self.hitmask_sprite.set_position(x, y)
        self.attackmask_sprite.set_position(x, y)

    def moveX(self, x):
        self.display_sprite.x += x
        self.hitmask_sprite.x += x
        self.attackmask_sprite.x += x

    def moveY(self, y):
        self.display_sprite.y += y
        self.hitmask_sprite.y += y
        self.attackmask_sprite.y += y

    @property
    def x(self):
        return self.display_sprite.x

    @x.setter
    def x(self, value):
        self.display_sprite.x = value
        self.hitmask_sprite.x = value
        self.attackmask_sprite.x = value
        """ not working yet don't use """

    @property
    def y(self):
        return self.display_sprite.y

    @y.setter
    def y(self, value):
        self.display_sprite.y = value
        self.hitmask_sprite.y = value
        self.attackmask_sprite.y = value
        """ not working yet don't use """

    def checkCollision(self, other):
        return self.attackmask.collides_with(other.collider)

    def checkHitmask(self, other):
        return self.hitmask.collides_with(other.attackmask)

    def cacheCurrentMasks(self):
        self.collider.cache_collission_image()
        self.hitmask.cache_collission_image()
        self.attackmask.cache_collission_image()