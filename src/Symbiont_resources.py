__author__ = 'SARAH'
import pyglet
pyglet.resource.path = ['../resources/ChibiUsa','../resources/ChibiUsaBlue', '../resources/sounds','../resources/Symbiont/halfsize','../resources/Symbiont/halfsize']
pyglet.resource.reindex()

from pyglet.media.riff import *

# Chibi Usa Images

Left1 = pyglet.resource.image("Symbiont_idle_left_1.png")
Right1 = pyglet.resource.image("Symbiont_idle_right_1.png")
Left2 = pyglet.resource.image("Symbiont_idle_left_2.png")
Right2 = pyglet.resource.image("Symbiont_idle_right_2.png")

WalkLeft1 = pyglet.resource.image("Symbiont_walk_left_1.png")
WalkRight1 = pyglet.resource.image("Symbiont_walk_right_1.png")
WalkLeft2 = pyglet.resource.image("Symbiont_walk_left_2.png")
WalkRight2 = pyglet.resource.image("Symbiont_walk_right_2.png")
WalkLeft3 = pyglet.resource.image("Symbiont_walk_left_3.png")
WalkRight3 = pyglet.resource.image("Symbiont_walk_right_3.png")

PunchLeft = pyglet.resource.image("Symbiont_punch_left.png")
PunchRight = pyglet.resource.image("Symbiont_punch_right.png")
KickLeft = pyglet.resource.image("Symbiont_kick_left.png")
KickRight = pyglet.resource.image("Symbiont_kick_right.png")
BlockLeft = pyglet.resource.image("Symbiont_block_left.png")
BlockRight = pyglet.resource.image("Symbiont_block_right.png")
HitLeft = pyglet.resource.image("Symbiont_hit_left.png")
HitRight = pyglet.resource.image("Symbiont_hit_right.png")
DuckLeft = pyglet.resource.image("Symbiont_ducked_left.png")
DuckRight = pyglet.resource.image("Symbiont_ducked_right.png")
LowPunchLeft = pyglet.resource.image("Symbiont_lowpunch_left.png")
LowPunchRight = pyglet.resource.image("Symbiont_lowpunch_right.png")
LowKickLeft = pyglet.resource.image("Symbiont_lowkick_left.png")
LowKickRight = pyglet.resource.image("Symbiont_lowkick_right.png")
LowBlockLeft = pyglet.resource.image("Symbiont_lowblock_left.png")
LowBlockRight = pyglet.resource.image("Symbiont_lowblock_right.png")
JumpLeft = pyglet.resource.image("Symbiont_jump_left.png")
JumpRight = pyglet.resource.image("Symbiont_jump_right.png")

BlockLeftMask = pyglet.resource.image("Symbiont_block_left_mask.png")
BlockRightMask = pyglet.resource.image("Symbiont_block_right_mask.png")

LowBlockLeftMask = pyglet.resource.image("Symbiont_lowblock_left_mask.png")
LowBlockRightMask = pyglet.resource.image("Symbiont_lowblock_right_mask.png")

PunchLeftMask = pyglet.resource.image("Symbiont_punch_left_mask.png")
PunchRightMask = pyglet.resource.image("Symbiont_punch_right_mask.png")
KickLeftMask = pyglet.resource.image("Symbiont_kick_left_mask.png")
KickRightMask = pyglet.resource.image("Symbiont_kick_right_mask.png")

LowPunchLeftMask = pyglet.resource.image("Symbiont_lowpunch_left_mask.png")
LowPunchRightMask = pyglet.resource.image("Symbiont_lowpunch_right_mask.png")
LowKickLeftMask = pyglet.resource.image("Symbiont_lowkick_left_mask.png")
LowKickRightMask = pyglet.resource.image("Symbiont_lowkick_right_mask.png")

SpezialLeft1 = pyglet.resource.image("Symbiont_special_left_1.png")
SpezialLeft2 = pyglet.resource.image("Symbiont_special_left_2.png")

SpezialRight1 = pyglet.resource.image("Symbiont_special_right_1.png")
SpezialRight2 = pyglet.resource.image("Symbiont_special_right_2.png")

SpezialLeftMask2 = pyglet.resource.image("Symbiont_special_left_3_mask.png")
SpezialRightMask2 = pyglet.resource.image("Symbiont_special_right_3_mask.png")

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