from pyglet.gl import *
import resources

from pyglet.window import key
from Player import *

from ChibiUsa import *
from ChibiUsa_blue import *
from Viking import *
from Symbiont import *
from InputHandling.PlayerOneKeyboardInputHandler import PlayerOneKeyboardInputHandler
from InputHandling.PlayerTwoKeyboardInputHandler import PlayerTwoKeyboardInputHandler
from InputHandling.PlayerOneArcadeControllerInputHandler import PlayerOneArcadeControllerInputHandler
from InputHandling.PlayerTwoArcadeControllerInputHandler import PlayerTwoArcadeControllerInputHandler

from Enum import *

from src.Healthbar.healthbar import *
from src.RoundCounter.roundcounter import *
from pyglet.gl import *

import threading


pyglet.options['audio'] = ('openal')
pyglet.options['debug_gl'] = False

# create a simple window
window = pyglet.window.Window(caption="collision", visible=False, fullscreen=True) #60x480
glScalef(1.5, 1.5, 1.5)

label = pyglet.text.Label('Click to create falling objects (collision is pixel perfect but used image not)!', font_name='Times New Roman', font_size=10, x=window.width // 2,
                          y=4 * window.height // 5, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

# create the level as an entity
#player = Player(batch, foreground)

#player = ChibiUsa(batch, foreground)
#TODO resize Viking (downscale)
player = Viking(batch, foreground)
player.preloadImages()
player2 = Symbiont(batch, foreground)
#player2 = Viking(batch, foreground)
player2.preloadImages()

imagesLoaded = False

#player2 = ChibiUsa_blue(batch, foreground)
#player2.moveX(window.width / 2)

healthbar = HealthBar(batch, 50, 400, 200, 50)
healthbar2 = HealthBar(batch, 380, 400, 200, 50)
roundcounter = RoundCounter(batch, player, player2, 285, 400, 3)

playerOneInputController = PlayerOneKeyboardInputHandler(player)
playerTwoInputController = PlayerTwoKeyboardInputHandler(player2)

@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    playerOneInputController.handleKeyPress(symbol, modifiers)
    playerTwoInputController.handleKeyPress(symbol, modifiers)

@window.event()
def on_key_release(symbol, modifiers):
    print "a key was released"
    playerOneInputController.handleKeyRelease(symbol, modifiers)
    playerTwoInputController.handleKeyRelease(symbol, modifiers)

@window.event
def on_mouse_press(x, y, button, modifiers):
        '''Create a new block whenever the user clicks the mouse'''

fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
        # clear the window
        window.clear()

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        # draw our background and blocks
        batch.draw()
        label.draw()
        fps_display.draw()

        healthbar.draw()
        healthbar2.draw()
        roundcounter.draw()

def update(dt):
    #change sprite according to lookFlag
    #done in player update

    if player.getImagesPreloaded() == False:
        player.preloadImages()

    if player2.getImagesPreloaded() == False:
        player2.preloadImages()

    player.update()
    player2.update()

    if checkEnumValueEquals(player.actionState, ActionState.Attacking) and player.checkCollision(player2):
        print "Player Kollission"
        player2.playerHit(checkEnumValueEquals(player.lookDirection, Direction.Right) and Direction.Left or Direction.Right, player)

    if checkEnumValueEquals(player2.actionState, ActionState.Attacking) and player2.checkCollision(player):
        print "Player2 Kollission"
        player.playerHit(checkEnumValueEquals(player2.lookDirection, Direction.Right) and Direction.Left or Direction.Right, player2)

    update_rounds()


def update_rounds():
    healthbar.set_health(player.health)
    healthbar2.set_health(player2.health)
    roundcounter.update()

glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# make the window visible
window.set_visible(True)

# schedule our update function
pyglet.clock.schedule_interval(update, 1/30.0)

# and finally, run the app...
pyglet.app.run()