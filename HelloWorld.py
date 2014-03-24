__author__ = 'win8'

import pyglet
from pyglet.window import key
from pyglet.window import mouse


print("Be aware that pyglet requires 32bit version of python!")

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world!', font_name='Times New Roman', font_size=36, x=window.width // 2,
                          y=window.height // 2, anchor_x='center', anchor_y='center')

""" use any picture """
image  = pyglet.resource.image("small_cat.jpg")

@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    if symbol== key.LEFT:
        print "left key was pressed"

@window.event()
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print "left mouse pressed"

    elif button == mouse.RIGHT:
        print "right mouse pressed"




@window.event
def on_draw():
    window.clear()
    label.draw()
    image.blit(0, 0)


pyglet.app.run()

