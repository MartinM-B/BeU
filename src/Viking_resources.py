__author__ = 'SARAH'
import pyglet
pyglet.resource.path = ['../resources/ChibiUsa','../resources/ChibiUsaBlue', '../resources/sounds','../resources/Viking/halfsize','../resources/Symbiont/halfsize']
pyglet.resource.reindex()

from pyglet.media.riff import *

# Chibi Usa Images

Left1 = pyglet.resource.image("Viking_idle_left_1.png")
Right1 = pyglet.resource.image("Viking_idle_right_1.png")
Left2 = pyglet.resource.image("Viking_idle_left_2.png")
Right2 = pyglet.resource.image("Viking_idle_right_2.png")
Left3 = pyglet.resource.image("Viking_idle_left_3.png")
Right3 = pyglet.resource.image("Viking_idle_right_3.png")
Left4 = pyglet.resource.image("Viking_idle_left_4.png")
Right4 = pyglet.resource.image("Viking_idle_right_4.png")

WalkLeft1 = pyglet.resource.image("Viking_walk_left_1.png")
WalkRight1 = pyglet.resource.image("Viking_walk_right_1.png")
WalkLeft2 = pyglet.resource.image("Viking_walk_left_2.png")
WalkRight2 = pyglet.resource.image("Viking_walk_right_2.png")
WalkLeft3 = pyglet.resource.image("Viking_walk_left_3.png")
WalkRight3 = pyglet.resource.image("Viking_walk_right_3.png")
WalkLeft4 = pyglet.resource.image("Viking_walk_left_4.png")
WalkRight4 = pyglet.resource.image("Viking_walk_right_4.png")

PunchLeft = pyglet.resource.image("Viking_punch_left.png")
PunchRight = pyglet.resource.image("Viking_punch_right.png")
KickLeft = pyglet.resource.image("Viking_kick_left.png")
KickRight = pyglet.resource.image("Viking_kick_right.png")
BlockLeft = pyglet.resource.image("Viking_block_left.png")
BlockRight = pyglet.resource.image("Viking_block_right.png")
HitLeft = pyglet.resource.image("Viking_hit_left.png")
HitRight = pyglet.resource.image("Viking_hit_right.png")
DuckLeft = pyglet.resource.image("Viking_ducked_left.png")
DuckRight = pyglet.resource.image("Viking_ducked_right.png")
LowPunchLeft = pyglet.resource.image("Viking_lowpunch_left.png")
LowPunchRight = pyglet.resource.image("Viking_lowpunch_right.png")
LowKickLeft = pyglet.resource.image("Viking_lowkick_left.png")
LowKickRight = pyglet.resource.image("Viking_lowkick_right.png")
LowBlockLeft = pyglet.resource.image("Viking_lowblock_left.png")
LowBlockRight = pyglet.resource.image("Viking_lowblock_right.png")
JumpLeft = pyglet.resource.image("Viking_jump_left.png")
JumpRight = pyglet.resource.image("Viking_jump_right.png")

BlockLeftMask = pyglet.resource.image("Viking_block_left_mask.png")
BlockRightMask = pyglet.resource.image("Viking_block_right_mask.png")

LowBlockLeftMask = pyglet.resource.image("Viking_lowblock_left_mask.png")
LowBlockRightMask = pyglet.resource.image("Viking_lowblock_right_mask.png")

PunchLeftMask = pyglet.resource.image("Viking_punch_left_mask.png")
PunchRightMask = pyglet.resource.image("Viking_punch_right_mask.png")
KickLeftMask = pyglet.resource.image("Viking_kick_left_mask.png")
KickRightMask = pyglet.resource.image("Viking_kick_right_mask.png")

LowPunchLeftMask = pyglet.resource.image("Viking_lowpunch_left_mask.png")
LowPunchRightMask = pyglet.resource.image("Viking_lowpunch_right_mask.png")
LowKickLeftMask = pyglet.resource.image("Viking_lowkick_left_mask.png")
LowKickRightMask = pyglet.resource.image("Viking_lowkick_right_mask.png")

SpezialLeft1 = pyglet.resource.image("Viking_special_left_1.png")
SpezialLeft2 = pyglet.resource.image("Viking_special_left_2.png")
SpezialLeft3 = pyglet.resource.image("Viking_special_left_3.png")
SpezialLeft4 = pyglet.resource.image("Viking_special_left_4.png")
SpezialLeft5 = pyglet.resource.image("Viking_special_left_5.png")
SpezialLeft6 = pyglet.resource.image("Viking_special_left_6.png")

SpezialRight1 = pyglet.resource.image("Viking_special_right_1.png")
SpezialRight2 = pyglet.resource.image("Viking_special_right_2.png")
SpezialRight3 = pyglet.resource.image("Viking_special_right_3.png")
SpezialRight4 = pyglet.resource.image("Viking_special_right_4.png")
SpezialRight5 = pyglet.resource.image("Viking_special_right_5.png")
SpezialRight6 = pyglet.resource.image("Viking_special_right_6.png")

SpezialLeftMask1 = pyglet.resource.image("Viking_special_left_2_mask.png")
SpezialLeftMask2 = pyglet.resource.image("Viking_special_left_3_mask.png")
SpezialLeftMask3 = pyglet.resource.image("Viking_special_left_4_mask.png")
SpezialLeftMask4 = pyglet.resource.image("Viking_special_left_5_mask.png")

SpezialRightMask1 = pyglet.resource.image("Viking_special_right_2_mask.png")
SpezialRightMask2 = pyglet.resource.image("Viking_special_right_3_mask.png")
SpezialRightMask3 = pyglet.resource.image("Viking_special_right_4_mask.png")
SpezialRightMask4 = pyglet.resource.image("Viking_special_right_5_mask.png")

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