__author__ = 'win8'

import pyglet

from pyglet.window import key

from pyglet.window import mouse

""" TODO"""

print("Be aware that pyglet requires 32bit version of python!")

window = pyglet.window.Window()

label = pyglet.text.Label('Hello world!', font_name='Times New Roman', font_size=36, x=window.width // 2,
                          y=window.height // 2, anchor_x='center', anchor_y='center')

""" use any picture """
image = pyglet.resource.image("small_cat.jpg")

starLeft = pyglet.resource.image("walk_left.png")
starRight = pyglet.resource.image("walk_right.png")
starLeftEvent= pyglet.resource.image("catch_left.png")
starRightEvent = pyglet.resource.image("catch_right.png")

spritePositionX = window.width / 2
spritePositionY = window.height / 2

starSprite = pyglet.sprite.Sprite(starLeft, spritePositionX, spritePositionY)
lookLeft = 1

danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([starLeft, starLeftEvent, starRight, starRightEvent], 0.5, True)

@window.event()
def on_key_press(symbol, modifiers):
    print "a key was pressed"
    if symbol == key.LEFT:
        print "left key was pressed"
        starSprite.x -= 5
        if lookLeft != 1:
            global lookLeft
            lookLeft = 1
            starSprite.image = starLeft


    if symbol == key.RIGHT:
        print "right key was pressed"
        starSprite.x += 5
        global lookLeft
        if lookLeft != 0:
            lookLeft = 0
            starSprite.image = starRight

    if symbol == key.SPACE:
        print "space was pressed"
        """animation dance"""
        global lookLeft
        if(lookLeft != 2):
            lookLeft = 2
            starSprite.image = danceAnimation



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
    """image.blit(0, 0)"""
    starSprite.draw()


pyglet.app.run()

# test
