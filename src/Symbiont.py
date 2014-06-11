__author__ = 'SARAH'

from src import Symbiont_resources

from Player import *


class Symbiont(Player):

    #moveLeftImage = ChibiUsa_resources.Left
    #moveRightImage = ChibiUsa_resources.Right

    idleAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.Left1, Symbiont_resources.Left2], 0.5, True)

    idleAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.Right1, Symbiont_resources.Right2], 0.5, True)

    walkAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.WalkLeft1, Symbiont_resources.WalkLeft2, Symbiont_resources.WalkLeft3], 0.3, True)

    walkAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.WalkRight1, Symbiont_resources.WalkRight2, Symbiont_resources.WalkRight3], 0.3, True)


    punchLeft = Symbiont_resources.PunchLeft
    punchRight = Symbiont_resources.PunchRight
    kickLeft = Symbiont_resources.KickLeft
    kickRight = Symbiont_resources.KickRight
    blockLeft = Symbiont_resources.BlockLeft
    blockRight = Symbiont_resources.BlockRight
    hitLeft = Symbiont_resources.HitLeft
    hitRight = Symbiont_resources.HitRight
    duckLeft = Symbiont_resources.DuckLeft
    duckRight = Symbiont_resources.DuckRight
    lowPunchLeft = Symbiont_resources.LowPunchLeft
    lowPunchRight = Symbiont_resources.LowPunchRight
    lowKickLeft = Symbiont_resources.LowKickLeft
    lowKickRight = Symbiont_resources.LowKickRight
    lowBlockLeft = Symbiont_resources.LowBlockLeft
    lowBlockRight = Symbiont_resources.LowBlockRight
    jumpLeft = Symbiont_resources.JumpLeft
    jumpRight = Symbiont_resources.JumpRight

    blockLeftMask = Symbiont_resources.BlockLeftMask
    blockRightMask = Symbiont_resources.BlockRightMask

    lowBlockLeftMask = Symbiont_resources.LowBlockLeftMask
    lowBlockRightMask = Symbiont_resources.LowBlockRightMask

    punchLeftMask = Symbiont_resources.PunchLeftMask
    punchRightMask = Symbiont_resources.PunchRightMask
    kickLeftMask = Symbiont_resources.KickLeftMask
    kickRightMask = Symbiont_resources.KickRightMask

    lowPunchLeftMask = Symbiont_resources.LowPunchLeftMask
    lowPunchRightMask = Symbiont_resources.LowPunchRightMask
    lowKickLeftMask = Symbiont_resources.LowKickLeftMask
    lowKickRightMask = Symbiont_resources.LowKickRightMask

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.Left1, Symbiont_resources.Right1], 0.5, True)

    specialAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.SpezialLeft1, Symbiont_resources.SpezialLeft2], 0.2, True)

    specialAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.SpezialRight1, Symbiont_resources.SpezialRight2], 0.2, True)

    specialAnimationRightMask = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.SpezialLeft1, Symbiont_resources.SpezialLeftMask2], 0.2, True)

    specialAnimationLeftMask = pyglet.image.Animation.from_image_sequence\
    ([Symbiont_resources.SpezialRight1, Symbiont_resources.SpezialRightMask2], 0.2, True)

    jumpSound = Symbiont_resources.JumpSound
    punchSound = Symbiont_resources.PunchSound
    stepSound = Symbiont_resources.StepSound
    kickSound = Symbiont_resources.KickSound
    blockSound = Symbiont_resources.BlockSound
    duckSound = Symbiont_resources.DuckSound

    def __init__(self, batch, group):
        super(Player, self).__init__(image=Symbiont_resources.Left1, x=0, y=0, batch=batch, group=group)

    def adaptSpecialAttackPosition(self):
        return;

    def adaptSpecialAttackPositionBack(self):
        return;