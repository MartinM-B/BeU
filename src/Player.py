from src.HelloWorld import danceAnimation

__author__ = 'david_000'
from gameEntity import *
import resources
from Enum import Enum

ActionState = Enum('ActionState', Idle=0, Attacking=1, Blocking=2, Hit=3)
ActionType = Enum('ActionType', Idle=0, Punch=1, Kick=2, LowPunch=3, LowKick=4, Block=5, LowBlock=6, Hit=7)
MovementState = Enum('MovementState', Standing=0, Dancing=1, Moving=2)
JumpState = Enum('MovementState', NotJumping=0, Jumping=1)
Direction = Enum('Direction', Left=0, Right=1)

class Player(GameEntity):
    #initial health and damage
    health = 100
    damage = 5

    actionState = ActionState.Idle
    movementState = MovementState.Standing
    jumpState = JumpState.NotJumping
    lookDirection = Direction.Left
    actionType = ActionType.Idle
    actionTimer = 0
    jumpTimer = 0

    def __init__(self, batch, group):
        super(Player, self).__init__(image=resources.starLeft, x=0, y=0, batch=batch, group=group)

    def dance(self):
        self.stopMoving()
        self.stopBlocking()
        self.changeToDanceAnimation()

    def jump(self):
        if self.jumpState == JumpState.NotJumping:
            self.jumpState = JumpState.Jumping
            self.jumpTimer = 1
            self.changeToJumpAnimation()

    def stopMoving(self):
        self.movementState = MovementState.Standing

    def startMoving(self):
        self.movementState = MovementState.Moving

    def look(self, direction):
        self.lookDirection = direction
        self.changeToMoveAnimation()

    def kick(self):
        if self.actionState == ActionState.Idle:
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.Kick
            self.changeToKickAnimation()
            self.actionTimer = 5

    def punch(self):
        if self.actionState == ActionState.Idle:
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.Punch
            self.changeToPunchAnimation()
            self.actionTimer = 5

    def startBlocking(self):
        if self.actionState == ActionState.Idle:
            self.actionState = ActionState.Blocking
            self.actionType = ActionType.Block
            self.changeToBlockAnimation()
            self.stopMoving()

    def stopBlocking(self):
        if self.actionState == ActionState.Blocking:
            self.actionState = ActionState.Idle
            self.actionType = ActionType.Idle
            self.changeToMoveAnimation()

    def playerHit(self, direction):
        self.actionState = ActionState.Hit
        self.actionType = ActionType.Hit
        self.actionTimer = 5
        self.lookDirection = direction
        self.changeToHitAnimation(direction)

    def handleHitDamage(self):
        if self.health > 0:
            self.health -= 5
        if self.health <= 0:
            print "ChibiUsa loses"
            #TODO do sth. when losing??

    def changeToMoveAnimation(self):
        if self.jumpState == JumpState.NotJumping:
            self.changeSpriteBasedOnDirection(self.moveLeftImage, self.moveRightImage)

    def changeToJumpAnimation(self):
        self.changeSpriteBasedOnDirection(self.jumpLeft, self.jumpRight)

    def changeToHitAnimation(self, direction):
        if direction == Direction.Left:
            self.changeSpriteImage(self.hitLeft)
        elif direction == Direction.Right:
            self.changeSpriteImage(self.hitRight)

    def changeToPunchAnimation(self):
        self.changeSpriteBasedOnDirection(self.punchLeft, self.punchRight)

    def changeToKickAnimation(self):
        self.changeSpriteBasedOnDirection(self.kickLeft, self.kickRight)

    def changeToBlockAnimation(self):
        self.changeSpriteBasedOnDirection(self.blockLeft, self.blockRight)

    def changeToDanceAnimation(self):
        self.changeSpriteImage(self.danceAnimation)

    def changeSpriteBasedOnDirection(self, leftRes, rightRes):
        if self.lookDirection == Direction.Left:
            self.changeSpriteImage(leftRes)
        elif self.lookDirection == Direction.Right:
            self.changeSpriteImage(rightRes)

    def update(self):
        if self.movementState == MovementState.Moving:
            if self.lookDirection == Direction.Left:
                self.moveX(-2)
            elif self.lookDirection == Direction.Right:
                self.moveX(2)
        if self.jumpState == JumpState.Jumping:
            if self.jumpTimer < 6:
                self.moveY(5)
            elif self.jumpTimer < 11:
                self.moveY(1)
            elif self.jumpTimer < 17:
                self.moveY(-5)

            self.jumpTimer += 1
            if self.jumpTimer > 16:
                self.jumpTimer = 0
                self.jumpState = JumpState.NotJumping
                self.changeToMoveAnimation()

        if self.actionTimer > 0:
            self.actionTimer -= 1
        elif self.actionTimer == 0:
            self.actionState = ActionState.Idle
            self.actionType = ActionType.Idle
            self.changeToMoveAnimation()
            self.actionTimer = -1