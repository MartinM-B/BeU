__author__ = 'Martin'

from pyglet.gl import *
from src.states.StateMachine import *
from src.Messenger.PyMessage import *
from src.Messenger.PyMessenger import *
from src.timer.PyTimer import *

pyglet.options['audio'] = ('openal')
pyglet.options['debug_gl'] = False

# create a simple window
window = pyglet.window.Window(caption="collision", visible=False)  # 60x480
# glScalef(1.5, 1.5, 1.5)

timer = PyTimer()
timer.startTimer()

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)
messenger = PyMessenger()

type = 'receiver'
stateMachine = StateMachine(type, batch, background, foreground, window, messenger)

messenger.subscribe(type, stateMachine)

startMessage = PyMessage(type, States.Start)
messenger.send(startMessage)

def update(dt):
    messenger.execute()

@window.event
def on_draw():
    window.clear()
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    batch.draw()

@window.event
def on_update():
    print ''
    #update

@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    stateMachine.handleKeyPress(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    print "a key was released"
    stateMachine.handleKeyRelease(symbol, modifiers)


glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# schedule our update function
pyglet.clock.schedule_interval(update, 1 / 30.0)

# make the window visible
window.set_visible(True)

# and finally, run the app...
pyglet.app.run()
