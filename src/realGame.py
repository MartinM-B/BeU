__author__ = 'Martin'

from pyglet.gl import *
from src.states.StateMachine import *
from src.Messenger.PyMessage import *
from src.Messenger.PyMessenger import *
from Tkinter import *
from src.timer.PyTimer import *

pyglet.options['audio'] = ('openal')
pyglet.options['debug_gl'] = False

# create a simple window
window = pyglet.window.Window(caption="collision", visible=False, fullscreen=false) #60x480
glScalef(1.5, 1.5, 1.5)

timer = PyTimer()
timer.startTimer()

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

type = 'receiver'
stateMachine = StateMachine(type, batch, background, foreground, window)

messenger = PyMessenger()
messenger.subscribe(type, stateMachine)

gameMessage = PyMessage(type, States.start)
messenger.send()

@window.event
def on_draw():
        window.clear()

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        batch.draw()

@window.event
def on_update():
    messenger.execute()


# and finally, run the app...
pyglet.app.run()
