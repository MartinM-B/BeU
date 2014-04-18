__author__ = 'david_000'
from gameEntity import *
import resources

class Player(GameEntity):
    #lookLFlag: 0 = animation is running, 1 = left, 2 = right
    lookFlag = 1
    #moveFlag: 0 = don't move, 1 = move left, 2 = move right
    moveFlag = 0
    #jumpFlag: 0 = don't jump, 1-5 = jump up quick, 6-10 = jump up slow, 11-16 = jump down
    jumpFlag = 0
    moveLeftImage = resources.starLeft
    moveRightImage = resources.starRight
    danceAnimation = pyglet.image.Animation.from_image_sequence\
    ([resources.starLeft, resources.starLeftEvent, resources.starRight, resources.starRightEvent], 0.5, True)

    punchLeft = 0
    punchRight = 0
    kickLeft = 0
    kickRight = 0
    blockLeft = 0
    blockRight = 0
    hitLeft = 0
    hitRight = 0
    duckLeft = 0
    duckRight = 0
    lowPunchLeft = 0
    lowPunchRight = 0
    lowKickLeft = 0
    lowKickRight = 0
    lowBlockLeft = 0
    lowBlockRight = 0
    jumpLeft = 0
    jumpRight = 0

    #initial health and damage
    health = 100
    damage = 5

    #kickFlag: 0 = not kicking, > 0 kicking for x more frames
    kickFlag = 0
    #punchFlag: 0 = not punching, > 0 punching for x more frames
    punchFlag = 0
    #hitFlag: 0 = not hit, > 0 being hit for x more frames
    hitFlag = 0
    #blockFlag: 0 = not blocking, 1 = blocking
    blockFlag = 0

    def __init__(self, batch, group):
        super(Player, self).__init__(image=resources.starLeft, x=0, y=0, batch=batch, group=group)

    @property
    def look(self):
        return self.lookFlag

    @property
    def move(self):
        return self.moveFlag

    @property
    def jump(self):
        return self.jumpFlag

    @property
    def kick(self):
        return self.kickFlag

    @property
    def punch(self):
        return self.punchFlag

    @property
    def block(self):
        return self.blockFlag

    @look.setter
    def look(self, value):
        #check values here for being correct
        self.lookFlag = value
        if self.lookFlag == 0:
            self.changeSpriteImage(self.danceAnimation)
        elif self.lookFlag == 1:
            self.changeSpriteImage(self.moveLeftImage)
        elif self.lookFlag == 2:
            self.changeSpriteImage(self.moveRightImage)

    @move.setter
    def move(self, value):
        self.moveFlag = value

    @jump.setter
    def jump(self, value):
        if self.blockFlag == 0:
            self.jumpFlag = value

    @block.setter
    def block(self, value):
        self.blockFlag = value

    @punch.setter
    def punch(self, value):
         #check values here for being correct
        if self.punchFlag == 0:
            self.punchFlag = value
            if self.punchFlag == 0:
                if self.lookFlag == 1:
                    self.changeSpriteImage(self.moveLeftImage)
                if self.lookFlag == 2:
                    self.changeSpriteImage(self.moveRightImage)
            elif self.punchFlag == 5:
                if self.lookFlag == 1:
                    self.changeSpriteImage(self.punchLeft)
                if self.lookFlag == 2:
                    self.changeSpriteImage(self.punchRight)

    @kick.setter
    def kick(self, value):
        #check values here for being correct
        if self.blockFlag == 0:
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

        #move
        if self.blockFlag == 0: #no moving while blocking
            if self.moveFlag == 1:
                self.moveX(-2)
                print "move left"
            elif self.moveFlag == 2:
                self.moveX(2)
                print "move right"

        if self.jumpFlag > 0:
            if self.jumpFlag < 6:
                self.moveY(5)
            elif self.jumpFlag < 11:
                self.moveY(1)
            elif self.jumpFlag < 17:
                self.moveY(-5)

            self.jumpFlag += 1
            if self.jumpFlag > 16:
                self.jumpFlag = 0


        if self.hitFlag > 0:
            self.hitFlag -= 1
        elif self.kickFlag > 0:
            self.kickFlag -= 1
        elif self.punchFlag > 0:
            self.punchFlag -= 1
        elif self.jumpFlag == 0:
            if self.blockFlag == 0:
                if self.lookFlag == 1:
                    self.changeSpriteImage(self.moveLeftImage)
                if self.lookFlag == 2:
                    self.changeSpriteImage(self.moveRightImage)

            elif self.blockFlag == 1:
                if self.lookFlag == 1:
                    self.changeSpriteImage(self.blockLeft)
                if self.lookFlag == 2:
                    self.changeSpriteImage(self.blockRight)
        elif self.jumpFlag > 0:
            if self.lookFlag == 1:
                self.changeSpriteImage(self.jumpLeft)
            if self.lookFlag == 2:
                self.changeSpriteImage(self.jumpRight)




