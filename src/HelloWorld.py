__author__ = 'win8'

import pyglet

from pyglet.window import key

from pyglet.window import mouse
import resources

""" TODO"""

print("Be aware that pyglet requires 32bit version of python!")

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world!', font_name='Times New Roman', font_size=36, x=window.width // 2,
                          y=window.height // 2, anchor_x='center', anchor_y='center')

""" use any picture """
image = resources.image

starLeft = resources.starLeft
starRight = resources.starRight
starLeftEvent= resources.starLeftEvent
starRightEvent = resources.starRightEvent

spritePositionX = window.width / 2
spritePositionY = window.height / 2

starSprite = pyglet.sprite.Sprite(starLeft, spritePositionX, spritePositionY)
#lookLFlag: 0 = animation is running, 1 = left, 2 = right
lookFlag = 1
#moveFlag: 0 = don't move, 1 = move left, 2 = move right
moveFlag = 0
#leftKeyFlag: 0 = left key not pressed, 1 = left key pressed
leftKeyFlag = 0
#rightKeyFlag: 0 = left key not pressed, 1 = left key pressed
rightKeyFlag = 0
#moveFlag: 0 = don't jump, 1-5 = jump up quick, 6-10 = jump up slow, 11-16 = jump down
jumpFlag = 0

danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([starLeft, starLeftEvent, starRight, starRightEvent], 0.5, True)

@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    if symbol == key.LEFT:
        print "left key was pressed"
        global leftKeyFlag
        leftKeyFlag = 1

        global lookFlag
        global moveFlag
        if lookFlag != 1:
            lookFlag = 1

        if moveFlag != 1:
            moveFlag = 1


    if symbol == key.RIGHT:
        print "right key was pressed"
        global rightKeyFlag
        rightKeyFlag = 1


        global lookFlag
        global moveFlag
        if lookFlag != 2:
            lookFlag = 2

        if moveFlag != 2:
            moveFlag = 2



    if symbol == key.UP:
        print "up key was pressed"
        global jumpFlag
        if jumpFlag == 0:
            jumpFlag = 1

    if symbol == key.SPACE:
        print "space was pressed"
        """animation dance"""
        global lookFlag
        global moveFlag
        if(lookFlag != 0):
            lookFlag = 0

        if moveFlag != 0:
            moveFlag = 0


@window.event()
def on_key_release(symbol, modifiers):
    print "a key was released"

    global moveFlag
    if symbol == key.LEFT:
        print "left key was released"

        global leftKeyFlag
        leftKeyFlag = 0

        #if he was walking left stop it
        if moveFlag == 1:
            moveFlag = 0


    if symbol == key.RIGHT:
        print "right key was released"

        global rightKeyFlag
        rightKeyFlag = 0

        #if he was walking right stop it
        if moveFlag == 2:
            moveFlag = 0



@window.event()
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print "left mouse pressed"

    elif button == mouse.RIGHT:
        print "right mouse pressed"


@window.event
def update(dt):
    global lookFlag
    global moveFlag
    global leftKeyFlag
    global rightKeyFlag
    #check keys to see if there is still one pressed that wasn't released
    if moveFlag == 0:
        if leftKeyFlag == 1:
            moveFlag = 1
            lookFlag = 1
        elif rightKeyFlag == 1:
            moveFlag = 2
            lookFlag = 2


    #change sprite according to lookFlag
    if lookFlag == 0:
        starSprite.image = danceAnimation
    elif lookFlag == 1:
        starSprite.image = starLeft
    elif lookFlag == 2:
        starSprite.image = starRight

    #move
    if moveFlag == 1:
        starSprite.x -= 2
        print "move left"
    elif moveFlag == 2:
        starSprite.x += 2
        print "move right"
    else:
        print "don't move"

    global jumpFlag
    if jumpFlag > 0:
        if jumpFlag < 6:
            starSprite.y += 5
        elif jumpFlag < 11:
            starSprite.y += 1
        elif jumpFlag < 17:
            starSprite.y -= 5

        jumpFlag += 1
        if jumpFlag > 16:
            jumpFlag = 0



# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

@window.event
def on_draw():
    window.clear()
    label.draw()
    """image.blit(0, 0)"""

    starSprite.draw()



pyglet.app.run()

# test
