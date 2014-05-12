__author__ = 'SARAH'
import pyglet
pyglet.resource.path = ['../resources/ChibiUsa','../resources/ChibiUsaBlue', '../resources/sounds']
pyglet.resource.reindex()

# Chibi Usa Blue Images

Left = pyglet.resource.image("ChibiUsa_blue_left.png")
Right = pyglet.resource.image("ChibiUsa_blue_right.png")
Left2 = pyglet.resource.image("ChibiUsa_blue_left2.png")
Right2 = pyglet.resource.image("ChibiUsa_blue_right2.png")
WalkLeft = pyglet.resource.image("ChibiUsa_blue_walk_left.png")
WalkRight = pyglet.resource.image("ChibiUsa_blue_walk_right.png")
PunchLeft = pyglet.resource.image("ChibiUsa_blue_punch_left.png")
PunchRight = pyglet.resource.image("ChibiUsa_blue_punch_right.png")
KickLeft = pyglet.resource.image("ChibiUsa_blue_kick_left.png")
KickRight = pyglet.resource.image("ChibiUsa_blue_kick_right.png")
BlockLeft = pyglet.resource.image("ChibiUsa_blue_block_left.png")
BlockRight = pyglet.resource.image("ChibiUsa_blue_block_right.png")
HitLeft = pyglet.resource.image("ChibiUsa_blue_hit_left.png")
HitRight = pyglet.resource.image("ChibiUsa_blue_hit_right.png")
DuckLeft = pyglet.resource.image("ChibiUsa_blue_ducked_left.png")
DuckRight = pyglet.resource.image("ChibiUsa_blue_ducked_right.png")
LowPunchLeft = pyglet.resource.image("ChibiUsa_blue_lowpunch_left.png")
LowPunchRight = pyglet.resource.image("ChibiUsa_blue_lowpunch_right.png")
LowKickLeft = pyglet.resource.image("ChibiUsa_blue_lowkick_left.png")
LowKickRight = pyglet.resource.image("ChibiUsa_blue_lowkick_right.png")
LowBlockLeft = pyglet.resource.image("ChibiUsa_blue_lowblock_left.png")
LowBlockRight = pyglet.resource.image("ChibiUsa_blue_lowblock_right.png")
JumpLeft = pyglet.resource.image("ChibiUsa_blue_jump_left.png")
JumpRight = pyglet.resource.image("ChibiUsa_blue_jump_right.png")

BlockLeftMask = pyglet.resource.image("ChibiUsa_blue_block_left_mask.png")
BlockRightMask = pyglet.resource.image("ChibiUsa_blue_block_right_mask.png")

LowBlockLeftMask = pyglet.resource.image("ChibiUsa_blue_lowblock_left_mask.png")
LowBlockRightMask = pyglet.resource.image("ChibiUsa_blue_lowblock_right_mask.png")

JumpSound = pyglet.resource.media('jumping_teon.wav', streaming=False)
PunchSound = pyglet.resource.media('punch.wav', streaming=False)
StepSound = pyglet.resource.media('step.wav', streaming=False)
KickSound = pyglet.resource.media('kick.wav', streaming=False)
BlockSound = pyglet.resource.media('block.wav', streaming=False)
DuckSound = pyglet.resource.media('duck.wav', streaming=False)

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2