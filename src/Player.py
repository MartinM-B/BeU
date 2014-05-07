__author__ = 'david_000'
from gameEntity import *
import resources
from Enum import *

ActionState = Enum('ActionState', Idle=0, Attacking=1, Blocking=2, Hit=3)
ActionType = Enum('ActionType', Idle=0, Punch=1, Kick=2, LowPunch=3, LowKick=4, Block=5, LowBlock=6, Hit=7)
MovementState = Enum('MovementState', Standing=0, Dancing=1, Moving=2)
JumpState = Enum('MovementState', NotJumping=0, Jumping=1)
Direction = Enum('Direction', Left=0, Right=1)
DuckState = Enum('DuckState', NotDucking=0, Ducking=1)

class Player(GameEntity):
    #initial health and damage
    health = 100
    damage = 5

    actionState = ActionState.Idle
    movementState = MovementState.Standing
    jumpState = JumpState.NotJumping
    duckState = DuckState.NotDucking
    lookDirection = Direction.Left
    actionType = ActionType.Idle
    actionTimer = 0
    jumpTimer = 0
    duckTimer = 0

    def __init__(self, batch, group):
        super(Player, self).__init__(image=resources.block, x=0, y=0, batch=batch, group=group)

    def dance(self):
        self.stopMoving()
        self.stopBlocking()
        self.changeToDanceAnimation()

    def jump(self):
        if checkEnumValueEquals(self.jumpState, JumpState.NotJumping):
            self.jumpState = JumpState.Jumping
            self.jumpTimer = 1
            self.changeToJumpAnimation()

    def duck(self):
        if checkEnumValueEquals(self.duckState, DuckState.NotDucking):
            self.duckState = DuckState.Ducking
            self.duckTimer = 1
            self.changeToDuckAnimation()

    def stopDucking(self):
        if checkEnumValueEquals(self.duckState, DuckState.Ducking):
            self.duckState = DuckState.NotDucking
            self.changeToStandingAnimation()

    def stopMoving(self):
        self.movementState = MovementState.Standing
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.changeToIdleAnimation()

    def startMoving(self):
        self.movementState = MovementState.Moving
        self.changeToMoveAnimation()

    def look(self, direction):
        #careful here direction is passed by reference
        if checkEnumValueEquals(direction, Direction.Left):
            self.lookDirection = Direction.Left
        else:
            self.lookDirection = Direction.Right
        self.changeToMoveAnimation()

    def kick(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.Kick
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                self.changeToLowKickAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                self.changeToKickAnimation()
            self.actionTimer = 5

    def punch(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.Punch
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                self.changeToLowPunchAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                self.changeToPunchAnimation()
            self.actionTimer = 5

    def startBlocking(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Blocking
            self.actionType = ActionType.Block
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                self.changeToLowBlockAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                self.changeToBlockAnimation()
            self.stopMoving()

    def stopBlocking(self):
        if checkEnumValueEquals(self.actionState, ActionState.Blocking):
            self.actionState = ActionState.Idle
            self.actionType = ActionType.Idle
            if checkEnumValueEquals(self.movementState, MovementState.Moving):
                self.changeToMoveAnimation()
            else:
                self.changeToIdleAnimation()

    def playerHit(self, direction):
        if checkEnumValueEquals(self.actionState, ActionState.Blocking):
            if checkEnumValueNotEquals(self.lookDirection, direction): #blocking in wrong direction
                self.actionState = ActionState.Hit
                self.actionType = ActionType.Hit
                self.actionTimer = 5
                self.lookDirection = direction
                self.changeToHitAnimation(direction)
        else: #not blocking
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
        print "change to move"
        if checkEnumValueEquals(self.jumpState, JumpState.NotJumping) and checkEnumValueEquals(self.duckState, DuckState.NotDucking):
            self.changeSpriteBasedOnDirection(self.walkAnimationLeft, self.walkAnimationRight)
        elif checkEnumValueEquals(self.duckState, DuckState.Ducking):
            print "ducking"
            self.changeSpriteBasedOnDirection(self.duckLeft, self.duckRight)

    def changeToIdleAnimation(self):
        print "change to move"
        if checkEnumValueEquals(self.jumpState, JumpState.NotJumping) and checkEnumValueEquals(self.duckState, DuckState.NotDucking):
            self.changeSpriteBasedOnDirection(self.idleAnimationLeft, self.idleAnimationRight)
        elif checkEnumValueEquals(self.duckState, DuckState.Ducking):
            print "ducking"
            self.changeSpriteBasedOnDirection(self.duckLeft, self.duckRight)

    def changeToJumpAnimation(self):
        self.changeSpriteBasedOnDirection(self.jumpLeft, self.jumpRight)

    def changeToDuckAnimation(self):
        self.changeSpriteBasedOnDirection(self.duckLeft, self.duckRight)

    def changeToStandingAnimation(self):
        if checkEnumValueEquals(self.movementState, MovementState.Moving):
            self.changeToMoveAnimation()
        else:
            self.changeToIdleAnimation()

    def changeToHitAnimation(self, direction):
        if checkEnumValueEquals(direction, Direction.Left):
            self.changeSpriteImage(self.hitLeft)
        elif checkEnumValueEquals(direction, Direction.Right):
            self.changeSpriteImage(self.hitRight)

    def changeToPunchAnimation(self):
        self.changeSpriteBasedOnDirection(self.punchLeft, self.punchRight)

    def changeToLowPunchAnimation(self):
        self.changeSpriteBasedOnDirection(self.lowPunchLeft, self.lowPunchRight)

    def changeToKickAnimation(self):
        self.changeSpriteBasedOnDirection(self.kickLeft, self.kickRight)

    def changeToLowKickAnimation(self):
        self.changeSpriteBasedOnDirection(self.lowKickLeft, self.lowKickRight)

    def changeToBlockAnimation(self):
        self.changeSpriteBasedOnDirection(self.blockLeft, self.blockRight)

    def changeToLowBlockAnimation(self):
        self.changeSpriteBasedOnDirection(self.lowBlockLeft, self.lowBlockRight)

    def changeToDanceAnimation(self):
        self.changeSpriteImage(self.danceAnimation)

    def changeSpriteBasedOnDirection(self, leftRes, rightRes):
        if checkEnumValueEquals(self.lookDirection, Direction.Left):
            self.changeSpriteImage(leftRes)
        elif checkEnumValueEquals(self.lookDirection, Direction.Right):
            self.changeSpriteImage(rightRes)

    def update(self):
        if checkEnumValueEquals(self.movementState, MovementState.Moving):
            print "movingPlayer"
            print self.duckState
            if checkEnumValueNotEquals(self.duckState, DuckState.Ducking):
                print self.lookDirection
                if checkEnumValueEquals(self.lookDirection, Direction.Left):
                    print "movingPlayerX"
                    self.moveX(-2)
                elif checkEnumValueEquals(self.lookDirection, Direction.Right):
                    print "movingPlayerX"
                    self.moveX(2)
        if checkEnumValueEquals(self.jumpState, JumpState.Jumping):
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

                if checkEnumValueEquals(self.movementState, MovementState.Moving):
                    self.changeToMoveAnimation()
                else:
                    self.changeToIdleAnimation()

        if self.actionTimer > 0:
            self.actionTimer -= 1
        elif self.actionTimer == 0:
            self.actionState = ActionState.Idle
            self.actionType = ActionType.Idle
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                self.changeToDuckAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                if checkEnumValueEquals(self.movementState, MovementState.Moving):
                    self.changeToMoveAnimation()
                else:
                    self.changeToIdleAnimation()
            self.actionTimer = -1