__author__ = 'SARAH'

from Player import *
from src import ChibiUsa_blue_resources


class ChibiUsa_blue(Player):

    #moveLeftImage = ChibiUsa_blue_resources.Left
    #moveRightImage = ChibiUsa_blue_resources.Right

    idleAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Left, ChibiUsa_blue_resources.Left2], 0.5, True)

    idleAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Right, ChibiUsa_blue_resources.Right2], 0.5, True)

    walkAnimationLeft = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Left, ChibiUsa_blue_resources.WalkLeft], 0.1, True)

    walkAnimationRight = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Right, ChibiUsa_blue_resources.WalkRight], 0.1, True)

    punchLeft = ChibiUsa_blue_resources.PunchLeft
    punchRight = ChibiUsa_blue_resources.PunchRight
    kickLeft = ChibiUsa_blue_resources.KickLeft
    kickRight = ChibiUsa_blue_resources.KickRight
    blockLeft = ChibiUsa_blue_resources.BlockLeft
    blockRight = ChibiUsa_blue_resources.BlockRight
    hitLeft = ChibiUsa_blue_resources.HitLeft
    hitRight = ChibiUsa_blue_resources.HitRight
    duckLeft = ChibiUsa_blue_resources.DuckLeft
    duckRight = ChibiUsa_blue_resources.DuckRight
    lowPunchLeft = ChibiUsa_blue_resources.LowPunchLeft
    lowPunchRight = ChibiUsa_blue_resources.LowPunchRight
    lowKickLeft = ChibiUsa_blue_resources.LowKickLeft
    lowKickRight = ChibiUsa_blue_resources.LowKickRight
    lowBlockLeft = ChibiUsa_blue_resources.LowBlockLeft
    lowBlockRight = ChibiUsa_blue_resources.LowBlockRight
    jumpLeft = ChibiUsa_blue_resources.JumpLeft
    jumpRight = ChibiUsa_blue_resources.JumpRight

    blockLeftMask = ChibiUsa_blue_resources.BlockLeftMask
    blockRightMask = ChibiUsa_blue_resources.BlockRightMask

    lowBlockLeftMask = ChibiUsa_blue_resources.LowBlockLeftMask
    lowBlockRightMask = ChibiUsa_blue_resources.LowBlockRightMask

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Left, ChibiUsa_blue_resources.Right], 0.5, True)

    jumpSound = ChibiUsa_blue_resources.JumpSound
    punchSound = ChibiUsa_blue_resources.PunchSound
    stepSound = ChibiUsa_blue_resources.StepSound
    kickSound = ChibiUsa_blue_resources.KickSound
    blockSound = ChibiUsa_blue_resources.BlockSound
    duckSound = ChibiUsa_blue_resources.DuckSound


    def __init__(self, batch, group):
        super(Player, self).__init__(image=ChibiUsa_blue_resources.Left, x=0, y=0, batch=batch, group=group)