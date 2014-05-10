# this is improved version of animatedsprite which can be found here:
# http://swiftcoder.wordpress.com/2009/04/17/enhanced-animation-code-for-pyglet/

import pyglet
from pyglet.gl import *
from pyglet.text import *

class HealthBar(object):
    ''' Sprite subclass providing advanced
            playback controls for animated sprites '''

    def __init__(self, batch, x=0, y=0, w=100, h=50):
        self._blend_src = pyglet.gl.GL_SRC_ALPHA
        self._blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA

        self._color = (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)

        self._height = h
        self._width = w
        self._health = 50

        self._x = x
        self._y = y

        self._label = pyglet.text.Label(str(self._health), font_name='Times New Roman', font_size=36, x=60, y=60, anchor_x='center', anchor_y='center')

    def draw(self):
        self.draw_background()
        self.draw_bar_background()
        self.draw_bar()
        self.draw_label()


    def set_size(self, w, h):
        self._height = h
        self._width = w

    def set_position(self, x, y):
        self._x = x
        self._y = y

    def draw_background(self):
        color = (200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200)
        self.draw_rect(self._x, self._y, self._width, self._height, color)

    def draw_bar_background(self):
        bar_width = self._width - 60
        bar_height = self._height - 20

        bar_color = (170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170, 170)
        self.draw_rect(self._x+10, self._y+10, bar_width, bar_height, bar_color)

    def draw_bar(self):
        bar_width = (self._width - 60) * (float(self._health)/float(100))
        bar_height = self._height - 20

        if self._health > 50:
            bar_color = (0, 205, 0, 0, 205, 0, 0, 205, 0, 0, 205, 0)
        elif self._health > 25:
            bar_color = (255, 185, 15, 255, 185, 15, 255, 185, 15, 255, 185, 15)
        else:
            bar_color = (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)

        self.draw_rect(self._x+10, self._y+10, bar_width, bar_height, bar_color)

    def draw_label(self):
        self._label.text = str(self._health)
        self._label._x = self._x + self._width - 25
        self._label._y = self._y + self._height - 22
        self._label.font_size = (self._height-25)/1.33333
        self._label.color = (41, 41, 41, 255)
        self._label.draw()

    def draw_rect(self, x, y, w, h, color=(0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255)):
        glPushMatrix()
        x1 = x
        y1 = y
        y2 = y1 + h
        x2 = x1 + w
        pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                             ('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
                             ('c3B', color))
        glPopMatrix()

    def set_health(self, percent):
        if percent > 100:
            self._health = 100
        elif percent < 0:
            self._health = 0
        else:
            self._health = percent







