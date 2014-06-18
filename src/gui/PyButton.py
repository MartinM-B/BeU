__author__ = 'florian'
from pyglet import sprite
import pyglet
from PyRectangle import *
# class which works with a label and rectangle, reacts if called from the layouter


class PyButton(object):
    _scale = 1

    def __init__(self, id, aClickListener, aPyPoint, aBatch, aResource, aResourceActive, aGroup, aString=''):
        self.id = id
        self.point = aPyPoint
        self.batch = aBatch
        self.res = aResource
        self.resActive = aResourceActive
        self.listener = aClickListener
        self.group = aGroup
        self.active = False
        self.string = aString
        # self.rectangle = PyRectangle(self.point, self.res.height, self.res.width, self.batch)
        self.display_sprite = pyglet.sprite.Sprite(self.res, self.point.x, self.point.y, batch=self.batch,
                                                   group=self.group)
        self.label = pyglet.text.Label(text=self.string, font_name='Times New Roman', font_size=24, x=self.point.x + 70,
                                       y=self.point.y + 18,
                                       width=self.display_sprite.width, height=self.display_sprite.height,
                                       anchor_x='left',
                                       anchor_y='center', color=(0, 0, 0, 255), batch=self.batch, halign='right')
        self.display_sprite.scale = self._scale

    def onClick(self):
        self.listener.onClick(self.id)

    def setActive(self, active):
        self.active = active
        if active:
            self.display_sprite = sprite.Sprite(self.resActive, self.point.x, self.point.y, batch=self.batch,
                                                group=self.group)
            self.display_sprite.scale = self._scale
            # red = PyColor(255, 0, 0)
            # self.rectangle.changeColor(red)
        elif not active:
            self.display_sprite = sprite.Sprite(self.res, self.point.x, self.point.y, batch=self.batch,
                                                group=self.group)
            self.display_sprite.scale = self._scale
            # black = PyColor(0, 0, 0)
            # self.rectangle.changeColor(black)

    def delete(self):
        print 'delete'
        self.display_sprite.delete()
        self.label.delete()

    def setScale(self, factor):
        self._scale = factor
        self.setActive(self.active)
