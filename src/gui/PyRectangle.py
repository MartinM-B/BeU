__author__ = 'florian'
from pyglet import gl
from pyglet import graphics
from PyColor import *

# Rectangle class with left upper corner and width an height, the points will be in clockwise order


class PyRectangle(object):
    def __init__(self, p1, height, width, batch):
        self.p1 = p1
        self.h = height
        self.w = width
        self.batch = batch
        self.drawRect()

    # mode decides whether the rectangle is filled or not
    def drawRect(self, mode=0, color1=0, color2=0, color3=0, color4=0):
        if color1 == 0:
            color1 = PyColor(0, 0, 0)
        if color2 == 0:
            color2 = PyColor(0, 0, 0)
        if color3 == 0:
            color3 = PyColor(0, 0, 0)
        if color4 == 0:
            color4 = PyColor(0, 0, 0)

        if mode != 0:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_Fill)
        else:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)

        # self.batch.add(4, graphics.GL_QUADS,
        # ('v2i', (self.p1.x, self.p1.y,
        #                        self.p1.x + self.w, self.p1.y,
        #                        self.p1.x + self.w, self.p1.y + self.h,
        #                        self.p1.x, self.p1.y + self.h)),
        #               ('c3B', (color1.r, color1.g, color1.b,
        #                        color2.r, color2.g, color2.b,
        #                        color3.r, color3.g, color3.b,
        #                        color4.r, color4.g, color4.b)))

        self.batch.add(4, gl.GL_QUADS, None,
                       ('v2i', [self.p1.x, self.p1.y,
                                self.p1.x + self.w, self.p1.y,
                                self.p1.x + self.w, self.p1.y + self.h,
                                self.p1.x, self.p1.y + self.h]),
                       ('c4B', [color1.r, color1.g, color1.b, 255] * 4))

    def changeColor(self, c1):
        print 'change color'
        self.drawRect(0, c1, c1, c1, c1);