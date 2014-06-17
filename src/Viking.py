__author__ = 'SARAH'

import Viking_resources

from Player import *


class Viking(Player):

    idleAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.Left1, Viking_resources.Left2, Viking_resources.Left3, Viking_resources.Left4], 0.5, True)

    idleAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.Right1, Viking_resources.Right2, Viking_resources.Right3, Viking_resources.Right4], 0.5, True)

    walkAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.WalkLeft1, Viking_resources.WalkLeft2, Viking_resources.WalkLeft3, Viking_resources.WalkLeft4], 0.3, True)

    walkAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.WalkRight1, Viking_resources.WalkRight2, Viking_resources.WalkRight3, Viking_resources.WalkRight4], 0.3, True)


    punchLeft = Viking_resources.PunchLeft
    punchRight = Viking_resources.PunchRight
    kickLeft = Viking_resources.KickLeft
    kickRight = Viking_resources.KickRight
    blockLeft = Viking_resources.BlockLeft
    blockRight = Viking_resources.BlockRight
    hitLeft = Viking_resources.HitLeft
    hitRight = Viking_resources.HitRight
    duckLeft = Viking_resources.DuckLeft
    duckRight = Viking_resources.DuckRight
    lowPunchLeft = Viking_resources.LowPunchLeft
    lowPunchRight = Viking_resources.LowPunchRight
    lowKickLeft = Viking_resources.LowKickLeft
    lowKickRight = Viking_resources.LowKickRight
    lowBlockLeft = Viking_resources.LowBlockLeft
    lowBlockRight = Viking_resources.LowBlockRight
    jumpLeft = Viking_resources.JumpLeft
    jumpRight = Viking_resources.JumpRight

    blockLeftMask = Viking_resources.BlockLeftMask
    blockRightMask = Viking_resources.BlockRightMask

    lowBlockLeftMask = Viking_resources.LowBlockLeftMask
    lowBlockRightMask = Viking_resources.LowBlockRightMask

    punchLeftMask = Viking_resources.PunchLeftMask
    punchRightMask = Viking_resources.PunchRightMask
    kickLeftMask = Viking_resources.KickLeftMask
    kickRightMask = Viking_resources.KickRightMask

    lowPunchLeftMask = Viking_resources.LowPunchLeftMask
    lowPunchRightMask = Viking_resources.LowPunchRightMask
    lowKickLeftMask = Viking_resources.LowKickLeftMask
    lowKickRightMask = Viking_resources.LowKickRightMask

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.Left1, Viking_resources.Right1], 0.5, True)

    specialAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.SpezialLeft1, Viking_resources.SpezialLeft2, Viking_resources.SpezialLeft3,
      Viking_resources.SpezialLeft4, Viking_resources.SpezialLeft5, Viking_resources.SpezialLeft6], 0.1, False)

    specialAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.SpezialRight1, Viking_resources.SpezialRight2, Viking_resources.SpezialRight3,
      Viking_resources.SpezialRight4, Viking_resources.SpezialRight5, Viking_resources.SpezialRight6], 0.1, False)

    specialAnimationLeftMask = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.SpezialLeft1, Viking_resources.SpezialLeftMask2, Viking_resources.SpezialLeftMask3,
      Viking_resources.SpezialLeftMask4, Viking_resources.SpezialLeftMask5, Viking_resources.SpezialLeft6], 0.1, False)

    specialAnimationRightMask = pyglet.image.Animation.from_image_sequence\
    ([Viking_resources.SpezialRight1, Viking_resources.SpezialRightMask2, Viking_resources.SpezialRightMask3,
      Viking_resources.SpezialRightMask4, Viking_resources.SpezialRightMask5, Viking_resources.SpezialRight6], 0.1, False)

    jumpSound = Viking_resources.JumpSound
    punchSound = Viking_resources.PunchSound
    stepSound = Viking_resources.StepSound
    kickSound = Viking_resources.KickSound
    specialSound = Viking_resources.SpecialSound
    hitSound = Viking_resources.HitSound
    blockSound = Viking_resources.BlockSound
    duckSound = Viking_resources.DuckSound

    def __init__(self, batch, group):
        super(Player, self).__init__(image=Viking_resources.Left1, x=0, y=0, batch=batch, group=group)

    def adaptSpecialAttackPosition(self):
        self.moveX(-self.specialAnimationLeft.frames[0].image.width/2)

    def adaptSpecialAttackPositionBack(self):
        self.moveX(self.specialAnimationLeft.frames[0].image.width/2)