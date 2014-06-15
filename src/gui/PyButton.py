__author__ = 'florian'
from pyglet import sprite
from PyRectangle import *
# class which works with a label and rectangle, reacts if called from the layouter


class PyButton(object):
    def __init__(self, id, aClickListener, aPyPoint, aBatch, aResource, aResourceActive, aGroup):
        self.id = id
        self.point = aPyPoint
        self.batch = aBatch
        self.res = aResource
        self.resActive = aResourceActive
        self.listener = aClickListener
        self.group = aGroup
        self.active = False
        #self.rectangle = PyRectangle(self.point, self.res.height, self.res.width, self.batch)
        self.display_sprite = sprite.Sprite(self.res, self.point.x, self.point.y, batch=self.batch, group=self.group)

    def onClick(self):
        self.listener.onClick(self.id)

    def setActive(self, active):
        self.active = active
        if active:
            self.display_sprite = sprite.Sprite(self.resActive, self.point.x, self.point.y, batch=self.batch, group=self.group)
            #red = PyColor(255, 0, 0)
            #self.rectangle.changeColor(red)
        elif not active:
            self.display_sprite = sprite.Sprite(self.res, self.point.x, self.point.y, batch=self.batch, group=self.group)
            #black = PyColor(0, 0, 0)
            #self.rectangle.changeColor(black)
