from pyglet.gl import *

from ChibiUsa import *
from ChibiUsa_blue import *
from InputHandling.PlayerOneKeyboardInputHandler import PlayerOneKeyboardInputHandler
from InputHandling.PlayerTwoKeyboardInputHandler import PlayerTwoKeyboardInputHandler
from Enum import *

# create a simple window
window = pyglet.window.Window(640, 480, caption="collision", visible=False)

label = pyglet.text.Label('Click to create falling objects (collision is pixel perfect but used image not)!', font_name='Times New Roman', font_size=10, x=window.width // 2,
                          y=4 * window.height // 5, anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))

# create the render structures
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

# load our images
block = resources.block

# create the level as an entity
#player = Player(batch, foreground)
player = ChibiUsa(batch, foreground)
player2 = ChibiUsa_blue(batch, foreground)
player2.moveX(40)

playerOneInputController = PlayerOneKeyboardInputHandler(player)
playerTwoInputController = PlayerTwoKeyboardInputHandler(player2)

# create a set to contain the blocks
# a set has a very fast difference operation,
# which we will use in the update function
blocks = set()

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

        # create a new block
        b = GameEntity(block, x, y, batch, background)
        # add it to the set
        blocks.add(b)


fps_display = pyglet.clock.ClockDisplay()

@window.event
def on_draw():
        # clear the window
        window.clear()

        label.draw()
        fps_display.draw()
        # draw our background and blocks
        batch.draw()

def update(dt):
    #change sprite according to lookFlag
    #done in player update
    player.update()
    player2.update()


    if checkEnumValueEquals(player.actionState, ActionState.Attacking) and player.checkCollision(player2):
        print "Player Kollission"
        player2.playerHit(checkEnumValueEquals(player.lookDirection, Direction.Right) and Direction.Left or Direction.Right)
        player2.handleHitDamage()
    if checkEnumValueEquals(player2.actionState, ActionState.Attacking) and player2.checkCollision(player):
        print "Player2 Kollission"
        player.playerHit(checkEnumValueEquals(player2.lookDirection, Direction.Right) and Direction.Left or Direction.Right)
        player.handleHitDamage()

    for b in blocks:
            # don't let block fall out of the window bounds
            if b.y < -5:
                    b.setPosition(b.x, -5)

            # apply gravity
            b.moveY(-8)

            # move the block back upwards if they collide
            while b.checkCollision(player):
                    b.moveY(+1)

glClearColor(1.0, 1.0, 1.0, 1.0)
window.clear()
window.flip()

# make the window visible
window.set_visible(True)

# schedule our update function
pyglet.clock.schedule_interval(update, 1/30.0)

# and finally, run the app...
pyglet.app.run()