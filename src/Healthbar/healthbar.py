# this is improved version of animatedsprite which can be found here:
# http://swiftcoder.wordpress.com/2009/04/17/enhanced-animation-code-for-pyglet/

import pyglet
from pyglet.gl import *
from pyglet.text import *

from pyglet import gl
from pyglet import graphics
from src.gui.PyColor import *

from src.gui import gui_resources

class HealthBar(object):
    ''' Sprite subclass providing advanced
            playback controls for animated sprites '''

    def __init__(self, batch, window):
        #self._blend_src = pyglet.gl.GL_SRC_ALPHA
        #self._blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA
        self._color = (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)
        self._batch = batch
        self._health1 = 50
        self._health2 = 50

        self._winWidth = window.width/1.5
        self._winHeight = window.height/1.5

        self.background(batch)
        self.timerPic(batch)
        self.set_bar1()
        self.set_bar2()


    def update(self):
        self.background(self._batch)
        self.timerPic(self._batch)
        self.set_bar1()
        self.set_bar2()


    def background(self, batch):
        orig_img = gui_resources.life_background
        scaling_factor = (self._winWidth*0.4)/orig_img.width
        self._background1 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.05, self._winHeight*0.88, batch=batch, group=pyglet.graphics.OrderedGroup(0))
        self._background1.scale = scaling_factor
        self._background2 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.55, self._winHeight*0.88, batch=batch, group=pyglet.graphics.OrderedGroup(0))
        self._background2.scale = scaling_factor


    def timerPic(self, batch):
        img = gui_resources.timer
        scaling_factor = (self._winWidth*0.175)/img.width
        self._timer = pyglet.sprite.Sprite(img, self._winWidth*0.415, (self._winHeight*0.775), batch=batch, group=pyglet.graphics.OrderedGroup(1))
        self._timer.scale = scaling_factor


    def set_bar1(self):
        bar_width = (self._background1.width*0.9) * (float(self._health1)/float(100))
        bar_height = self._background1.height*0.8

        if self._health1 > 50:
            bar_color = (0, 205, 0, 0, 205, 0, 0, 205, 0, 0, 205, 0)
        elif self._health1 > 25:
            bar_color = (255, 185, 15, 255, 185, 15, 255, 185, 15, 255, 185, 15)
        else:
            bar_color = (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)

        x1 = self._background1.x + self._background1.width*0.05
        y1 = self._background1.y + self._background1.height*0.2
        x2 = self._background1.x + bar_width
        y2 = self._background1.y + bar_height

        glPushMatrix()
        pyglet.graphics.draw(4, gl.GL_QUADS, ('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
                      ('c3B', bar_color))
        glPopMatrix()


    def set_bar2(self):
        bar_width = (self._background1.width*0.85) * (float(self._health2)/float(100))
        bar_height = self._background1.height*0.8

        if self._health2 > 50:
            bar_color = (0, 205, 0, 0, 205, 0, 0, 205, 0, 0, 205, 0)
        elif self._health2 > 25:
            bar_color = (255, 185, 15, 255, 185, 15, 255, 185, 15, 255, 185, 15)
        else:
            bar_color = (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)

        x2 = (self._winWidth*0.5) + self._background1.x + self._background1.width*0.95
        y2 = self._background1.y + self._background1.height*0.2
        x1 = (self._winWidth*0.5)+ self._background1.x + self._background1.width*0.95 - bar_width
        y1 = self._background1.y + bar_height

        glPushMatrix()
        pyglet.graphics.draw(4, gl.GL_QUADS, ('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
                      ('c3B', bar_color))
        glPopMatrix()

    def draw(self):
        self.set_bar1()
        self.set_bar2()

    def set_health1(self, health):
        self._health1 = health

    def set_health2(self, health):
        self._health2 = health



