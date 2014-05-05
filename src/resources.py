__author__ = 'david_000'
import pyglet
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()

block = pyglet.resource.image('block.png')

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2
