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
        self.jumpFlag = value


    def update(self):

        #move
        if self.moveFlag == 1:
            self.moveX(-2)
            print "move left"
        elif self.moveFlag == 2:
            self.moveX(2)
            print "move right"
        else:
            print "don't move"

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


