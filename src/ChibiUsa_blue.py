__author__ = 'SARAH'

from Player import *
from src import ChibiUsa_blue_resources


class ChibiUsa_blue(Player):

    moveLeftImage = ChibiUsa_blue_resources.Left
    moveRightImage = ChibiUsa_blue_resources.Right

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

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_blue_resources.Left, ChibiUsa_blue_resources.Right], 0.5, True)



    def __init__(self, batch, group):
        super(Player, self).__init__(image=ChibiUsa_blue_resources.Left, x=0, y=0, batch=batch, group=group)