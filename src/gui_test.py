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
        print "" + anID + " was clicked"

window = pyglet.window.Window(caption="gui_test", visible=False, fullscreen=False) #60x480

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
layout = PyLayouter()

button1_res = gui_resources.box
button2_res = gui_resources.box
button1_resActive = gui_resources.box_selected
button2_resActive = gui_resources.box_selected
test_res = gui_resources.win
point1 = PyPoint(50, 50)
point2 = PyPoint(50, 180)
point3 = PyPoint(50, 310)


listener = PyListener()

button1 = PyButton("button1", listener, point1, batch, button1_res, button1_resActive, foreground, "test")
button2 = PyButton("button2", listener, point2, batch, button2_res, button1_resActive, foreground, "test2")
button3 = PyButton("button3", listener, point3, batch, button2_res, button1_resActive, foreground)
# sprite.Sprite(button1_res, point1.x, point1.y, batch=batch, group=foreground)
# pyglet.sprite.Sprite(button1_res, batch=batch)

buttonTest = pyglet.sprite.Sprite(test_res, x=400, y=100, batch=batch)

button1.setActive(True)

layout.addButton(button1)
layout.addButton(button2)
layout.addButton(button3)

@window.event
def on_draw():
        # clear the window
        window.clear()

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        # draw our background and blocks
        batch.draw()
        buttonTest.draw()



@window.event()
def on_key_press(symbol, modifiers):
    layout.handleKeyPress(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    layout.handleKeyRelease(symbol, modifiers)

glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# make the window visible
window.set_visible(True)

# and finally, run the app...
pyglet.app.run()






