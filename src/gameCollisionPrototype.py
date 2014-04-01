from pyglet.gl import *
import resources

from pyglet.window import key
from Player import *

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
player = Player(batch, foreground)

# create a set to contain the blocks
# a set has a very fast difference operation,
# which we will use in the update function
blocks = set()

#lookLFlag: 0 = animation is running, 1 = left, 2 = right
#lookFlag = 1
#moveFlag: 0 = don't move, 1 = move left, 2 = move right
#moveFlag = 0
#leftKeyFlag: 0 = left key not pressed, 1 = left key pressed
leftKeyFlag = 0
#rightKeyFlag: 0 = left key not pressed, 1 = left key pressed
rightKeyFlag = 0
#jumpFlag: 0 = don't jump, 1-5 = jump up quick, 6-10 = jump up slow, 11-16 = jump down
#jumpFlag = 0

"""danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([resources.starLeft, resources.starLeftEvent, resources.starRight, resources.starRightEvent], 0.5, True)
"""


@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    if symbol == key.LEFT:
        print "left key was pressed"
        global leftKeyFlag
        leftKeyFlag = 1

        #global lookFlag
        #global moveFlag
        if player.look != 1:
            player.look = 1

        if player.move != 1:
            player.move = 1

    if symbol == key.RIGHT:
        print "right key was pressed"
        global rightKeyFlag
        rightKeyFlag = 1

        #global lookFlag
        #global moveFlag
        if player.look != 2:
            player.look = 2

        if player.move != 2:
            player.move = 2

    if symbol == key.UP:
        print "up key was pressed"
        #global jumpFlag
        if player.jump == 0:
            player.jump = 1

    if symbol == key.SPACE:
        print "space was pressed"
        """animation dance"""
        #global lookFlag
        #global moveFlag
        if player.look != 0:
            player.look = 0

        if player.move != 0:
            player.move = 0


@window.event()
def on_key_release(symbol, modifiers):
    print "a key was released"

    #global moveFlag
    if symbol == key.LEFT:
        print "left key was released"

        global leftKeyFlag
        leftKeyFlag = 0

        #if he was walking left stop it
        if player.move == 1:
            player.move = 0


    if symbol == key.RIGHT:
        print "right key was released"

        global rightKeyFlag
        rightKeyFlag = 0

        #if he was walking right stop it
        if player.move == 2:
            player.move = 0

@window.event
def on_mouse_press(x, y, button, modifiers):
        '''Create a new block whenever the user clicks the mouse'''

        # create a new block
        b = GameEntity(block, x, y, batch, background)
        # add it to the set
        blocks.add(b)

@window.event
def on_draw():
        # clear the window
        window.clear()

        label.draw()

        # draw our background and blocks
        batch.draw()

def update(dt):

    #todo refactor sprite image update code

    #global lookFlag
    #global moveFlag
    global leftKeyFlag
    global rightKeyFlag
    #check keys to see if there is still one pressed that wasn't released
    if player.move == 0:
        if leftKeyFlag == 1:
            player.move = 1
            player.look = 1
        elif rightKeyFlag == 1:
            player.move = 2
            player.look = 2

    #change sprite according to lookFlag
    #done in player update
    player.update()
    """
    if lookFlag == 0:
        player.changeSpriteImage(danceAnimation)
    elif lookFlag == 1:
        player.changeSpriteImage(resources.starLeft)
    elif lookFlag == 2:
        player.changeSpriteImage(resources.starRight)

    #move
    if moveFlag == 1:
        player.moveX(-2)
        print "move left"
    elif moveFlag == 2:
        player.moveX(2)
        print "move right"
    else:
        print "don't move"

    global jumpFlag
    if jumpFlag > 0:
        if jumpFlag < 6:
            player.moveY(5)
        elif jumpFlag < 11:
            player.moveY(1)
        elif jumpFlag < 17:
            player.moveY(-5)

        jumpFlag += 1
        if jumpFlag > 16:
            jumpFlag = 0

    """

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