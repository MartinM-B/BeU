__author__ = 'SARAH'
import pyglet
pyglet.resource.path = ['../resources/ChibiUsaBlue']
pyglet.resource.reindex()

# Chibi Usa Images

Left = pyglet.resource.image("ChibiUsa_left.png")
Right = pyglet.resource.image("ChibiUsa_right.png")
PunchLeft = pyglet.resource.image("ChibiUsa_punch_left.png")
PunchRight = pyglet.resource.image("ChibiUsa_punch_right.png")
KickLeft = pyglet.resource.image("ChibiUsa_kick_left.png")
KickRight = pyglet.resource.image("ChibiUsa_kick_right.png")
BlockLeft = pyglet.resource.image("ChibiUsa_block_left.png")
BlockRight = pyglet.resource.image("ChibiUsa_block_right.png")
HitLeft = pyglet.resource.image("ChibiUsa_hit_left.png")
HitRight = pyglet.resource.image("ChibiUsa_hit_right.png")
DuckLeft = pyglet.resource.image("ChibiUsa_ducked_left.png")
DuckRight = pyglet.resource.image("ChibiUsa_ducked_right.png")
LowPunchLeft = pyglet.resource.image("ChibiUsa_lowpunch_left.png")
LowPunchRight = pyglet.resource.image("ChibiUsa_lowpunch_right.png")
LowKickLeft = pyglet.resource.image("ChibiUsa_lowkick_left.png")
LowKickRight = pyglet.resource.image("ChibiUsa_lowkick_right.png")
LowBlockLeft = pyglet.resource.image("ChibiUsa_lowblock_left.png")
LowBlockRight = pyglet.resource.image("ChibiUsa_lowblock_right.png")
JumpLeft = pyglet.resource.image("ChibiUsa_jump_left.png")
JumpRight = pyglet.resource.image("ChibiUsa_jump_right.png")

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2