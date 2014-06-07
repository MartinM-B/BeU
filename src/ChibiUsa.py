__author__ = 'SARAH'

from src import ChibiUsa_resources

from Player import *


class ChibiUsa(Player):

    #moveLeftImage = ChibiUsa_resources.Left
    #moveRightImage = ChibiUsa_resources.Right

    idleAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.Left, ChibiUsa_resources.Left2], 0.5, True)

    idleAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.Right, ChibiUsa_resources.Right2], 0.5, True)

    walkAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.WalkLeft, ChibiUsa_resources.Left], 0.3, True)

    walkAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.WalkRight, ChibiUsa_resources.Right], 0.3, True)

    #walkAnimationLeft = ChibiUsa_resources.Left

    #walkAnimationRight = ChibiUsa_resources.Right



    punchLeft = ChibiUsa_resources.PunchLeft
    punchRight = ChibiUsa_resources.PunchRight
    kickLeft = ChibiUsa_resources.KickLeft
    kickRight = ChibiUsa_resources.KickRight
    blockLeft = ChibiUsa_resources.BlockLeft
    blockRight = ChibiUsa_resources.BlockRight
    hitLeft = ChibiUsa_resources.HitLeft
    hitRight = ChibiUsa_resources.HitRight
    duckLeft = ChibiUsa_resources.DuckLeft
    duckRight = ChibiUsa_resources.DuckRight
    lowPunchLeft = ChibiUsa_resources.LowPunchLeft
    lowPunchRight = ChibiUsa_resources.LowPunchRight
    lowKickLeft = ChibiUsa_resources.LowKickLeft
    lowKickRight = ChibiUsa_resources.LowKickRight
    lowBlockLeft = ChibiUsa_resources.LowBlockLeft
    lowBlockRight = ChibiUsa_resources.LowBlockRight
    jumpLeft = ChibiUsa_resources.JumpLeft
    jumpRight = ChibiUsa_resources.JumpRight


    specialAttackLeft = punchLeft
    specialAttackRight = punchRight

    blockLeftMask = ChibiUsa_resources.BlockLeftMask
    blockRightMask = ChibiUsa_resources.BlockRightMask

    lowBlockLeftMask = ChibiUsa_resources.LowBlockLeftMask
    lowBlockRightMask = ChibiUsa_resources.LowBlockRightMask

    punchLeftMask = ChibiUsa_resources.PunchLeftMask
    punchRightMask = ChibiUsa_resources.PunchRightMask
    kickLeftMask = ChibiUsa_resources.KickLeftMask
    kickRightMask = ChibiUsa_resources.KickRightMask

    lowPunchLeftMask = ChibiUsa_resources.LowPunchLeftMask
    lowPunchRightMask = ChibiUsa_resources.LowPunchRightMask
    lowKickLeftMask = ChibiUsa_resources.LowKickLeftMask
    lowKickRightMask = ChibiUsa_resources.LowKickRightMask

    specialAttackLeftMask = punchLeftMask
    specialAttackRightMask = punchRightMask

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.Left, ChibiUsa_resources.Right], 0.5, True)

    jumpSound = ChibiUsa_resources.JumpSound
    punchSound = ChibiUsa_resources.PunchSound
    stepSound = ChibiUsa_resources.StepSound
    kickSound = ChibiUsa_resources.KickSound
    blockSound = ChibiUsa_resources.BlockSound
    duckSound = ChibiUsa_resources.DuckSound

    def __init__(self, batch, group):
        super(Player, self).__init__(image=ChibiUsa_resources.Left, x=0, y=0, batch=batch, group=group)