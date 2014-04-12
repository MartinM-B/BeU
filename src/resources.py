__author__ = 'david_000'
import pyglet
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

""" use any picture """
image = pyglet.resource.image("small_cat.jpg")

starLeft = pyglet.resource.image("walk_left.png")
starRight = pyglet.resource.image("walk_right.png")
starLeftEvent = pyglet.resource.image("catch_left.png")
starRightEvent = pyglet.resource.image("catch_right.png")

block = pyglet.resource.image('block.png')

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
