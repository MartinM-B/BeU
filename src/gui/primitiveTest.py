__author__ = 'florian'

import pyglet
from pyglet.gl import glClearColor
from pyglet.window import Window
from pyglet import gl
from PyPoint import *
from PyRectangle import *
from PyColor import *
from PyLayouter import *


window = pyglet.window.Window(640, 480, caption="collision", visible=False)

point1 = PyPoint(100, 100)
print point1.x
print point1.y

colorTooBig = PyColor(400, 400, -100)
print colorTooBig.r
print colorTooBig.g
print colorTooBig.b

layout = PyLayouter(window)


@window.event()
def on_key_press(symbol, modifiers):
    layout.handleKeyPress(symbol, modifiers)


@window.event()
def on_key_release(symbol, modifiers):
    layout.handleKeyRelease(symbol, modifiers)


@window.event()
def on_draw():
    window.clear()

    color = PyColor(200, 200, 200)
    color2 = PyColor(100, 0, 0)

    color = PyColor(200, 200, 200)
    rect = PyRectangle(point1, 50, 50)

    rect.drawRect(0, color)
    rect.changeColor(color2)

    # gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
    # pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
    #                      ('v2i', (100, 100,
    #                               150, 100,
    #                               150, 150,
    #                               100, 150)),
    #                      ('c3B', (200, 200, 200,
    #                               100, 100, 100,
    #                               0, 0, 0,
    #                               0, 0, 0)))

    # pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
    # ('v2i', (10, 15, 30, 35)),
    # ('c3B', (0, 0, 255, 0, 255, 0))
    # )
    #
    # pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
    # [0, 1, 2, 0, 2, 3],
    # ('v2i', (100, 100,
    # 150, 100,
    #                                   150, 150,
    #                                   100, 150))
    # )


glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()
window.set_visible(True)
pyglet.app.run()
