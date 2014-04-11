from src import ChibiUsa_resources

__author__ = 'SARAH'

from Player import *


class ChibiUsa(Player):

    moveLeftImage = ChibiUsa_resources.Left
    moveRightImage = ChibiUsa_resources.Right

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

    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([ChibiUsa_resources.Left, ChibiUsa_resources.Right], 0.5, True)

    #initial health and damage
    health = 100
    damage = 5

    #kickFlag: 0 = not kicking, > 0 kicking for x more frames
    kickFlag = 0
    #hitFlag: 0 = not hit, > 0 being hit for x more frames
    hitFlag = 0



    def __init__(self, batch, group):
        super(Player, self).__init__(image=ChibiUsa_resources.Left, x=0, y=0, batch=batch, group=group)

    @property
    def kick(self):
        return self.kickFlag

    @kick.setter
    def kick(self, value):
        #check values here for being correct
        self.kickFlag = value
        if self.kickFlag == 0:
            if self.lookFlag == 1:
                self.changeSpriteImage(self.moveLeftImage)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.moveRightImage)
        elif self.kickFlag == 5:
            if self.lookFlag == 1:
                self.changeSpriteImage(self.kickLeft)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.kickRight)


    def onHit(self):
        if self.health > 0:
            self.health -= 5
            self.hitFlag = 5
            if self.lookFlag == 1:
                self.changeSpriteImage(self.hitLeft)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.hitRight)
        if self.health <= 0:
            print "ChibiUsa loses"
            #TODO do sth. when losing??

    def update(self):
        Player.update(self)
        if self.hitFlag > 0:
            self.hitFlag -= 1
        elif self.kickFlag > 0:
            self.kickFlag -= 1
        elif self.jumpFlag == 0:
            if self.lookFlag == 1:
                self.changeSpriteImage(self.moveLeftImage)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.moveRightImage)
        elif self.jumpFlag > 0:
            if self.lookFlag == 1:
                self.changeSpriteImage(self.jumpLeft)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.jumpRight)



