from src.gui import gui_resources

__author__ = 'florian'
from src.gui.PyLayouter import *
from src.gui.gui_resources import *
from src.gui.PyPoint import *
from src.gui.PyClickListener import *
from gui_resources import *
from pyglet.gl import *


class PyListener(PyClickListener):

    def onClick(self, anID):
        print "" + anID + "was clicked"

window = pyglet.window.Window(caption="collision", visible=False, fullscreen=False) #60x480

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
layout = PyLayouter(window)

button1_res = gui_resources.box
button2_res = gui_resources.box
point1 = PyPoint(100, 100)
point2 = PyPoint(350, 350)
listener = PyListener()

button1 = PyButton("button1", listener, point1, batch, button1_res, foreground)
button2 = PyButton("button1", listener, point2, batch, button2_res, foreground)

layout.addButton(button1)
layout.addButton(button2)

@window.event
def on_draw():
        # clear the window
        window.clear()

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        # draw our background and blocks
        batch.draw()

glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# make the window visible
window.set_visible(True)

# and finally, run the app...
pyglet.app.run()


@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    layout.handleKeyPress(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    print "a key was released"
    layout.handleKeyRelease(symbol, modifiers)



