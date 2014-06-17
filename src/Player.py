__author__ = 'david_000'
from gameEntity import *
from Enum import *
from abc import ABCMeta, abstractmethod

ActionState = Enum('ActionState', Idle=0, Attacking=1, Blocking=2, Hit=3)
ActionType = Enum('ActionType', Idle=0, Punch=1, Kick=2, LowPunch=3, LowKick=4,
                  Block=5, LowBlock=6, Hit=7, SpecialAttack=8)
MovementState = Enum('MovementState', Standing=0, Dancing=1, Moving=2)
MovementSpeed = Enum('MovementSpeed', Slow=0, Fast=1)
JumpState = Enum('MovementState', NotJumping=0, Jumping=1)
Direction = Enum('Direction', Left=0, Right=1)
DuckState = Enum('DuckState', NotDucking=0, Ducking=1)


class Player(GameEntity):
    #initial health and damage
    health = 100
    damage = 5

    actionState = ActionState.Idle
    movementState = MovementState.Standing
    movementSpeed = MovementSpeed.Slow
    jumpState = JumpState.NotJumping
    duckState = DuckState.NotDucking
    lookDirection = Direction.Left
    actionType = ActionType.Idle
    actionTimer = 0
    jumpTimer = 0
    duckTimer = 0
    fastMoveTimer = 0
    imagesPreloaded = False

    def __init__(self, batch, group):
        super(Player, self).__init__(x=0, y=0, batch=batch, group=group)

    def dance(self):
        self.stopMoving()
        self.stopBlocking()
        self.changeToDanceAnimation()

    def jump(self):
        if checkEnumValueEquals(self.jumpState, JumpState.NotJumping):
            self.jumpState = JumpState.Jumping
            self.jumpTimer = 1
            self.changeToJumpAnimation()
            self.jumpSound.play()

    def duck(self):
        if checkEnumValueEquals(self.duckState, DuckState.NotDucking):
            self.duckState = DuckState.Ducking
            self.duckTimer = 1
            self.duckSound.play()
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
        if self.fastMoveTimer > 0:
            self.movementSpeed = MovementSpeed.Fast
        else:
            self.movementSpeed = MovementSpeed.Slow

        self.fastMoveTimer = 20
        self.movementState = MovementState.Moving
        self.stepSound.play()
        self.changeToMoveAnimation()

    def look(self, direction):
        if checkEnumValueNotEquals(direction, self.lookDirection):
            self.fastMoveTimer = 0

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
            self.kickSound.play()

    def punch(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.Punch
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                self.changeToLowPunchAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                self.changeToPunchAnimation()
            self.actionTimer = 5
            self.punchSound.play()

    def useSpecialAttack(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Attacking
            self.actionType = ActionType.SpecialAttack
            #if checkEnumValueEquals(self.duckState, DuckState.Ducking):
            #    self.changeToSpecialAttackAnimation()
            #elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
            #   self.changeToPunchAnimation()
            self.changeToSpecialAttackAnimation()
            self.actionTimer = 10
            self.punchSound.play()

    def startBlocking(self):
        if checkEnumValueEquals(self.actionState, ActionState.Idle):
            self.actionState = ActionState.Blocking
            print"start blocking"
            self.actionType = ActionType.Block
            if checkEnumValueEquals(self.duckState, DuckState.Ducking):
                print"change to block low animation"
                self.changeToLowBlockAnimation()
            elif checkEnumValueEquals(self.duckState, DuckState.NotDucking):
                print"change to block high animation"
                self.changeToBlockAnimation()
            self.stopMoving()

    def stopBlocking(self):
        if checkEnumValueEquals(self.actionState, ActionState.Blocking):
            print"stop blocking"
            self.actionState = ActionState.Idle
            self.actionType = ActionType.Idle
            if checkEnumValueEquals(self.movementState, MovementState.Moving):
                self.changeToMoveAnimation()
            else:
                self.changeToIdleAnimation()

    def playerHit(self, direction, other):
        if checkEnumValueEquals(self.actionState, ActionState.Blocking):
            if checkEnumValueNotEquals(self.lookDirection, direction): #blocking in wrong direction
                self.handlePlayerHit(direction, other)
                print "block in wrong direction"

            #check blocking mask
            if self.checkHitmask(other): #hit where block isn't effective
                self.handlePlayerHit(direction, other)
                print "hit where block isn't effective"

        else: #not blocking
            self.handlePlayerHit(direction, other)
            print "not blocking"

    def handlePlayerHit(self, direction, other):
        if checkEnumValueNotEquals(self.actionState, ActionState.Hit):
            self.handleHitDamage(other)
            self.actionState = ActionState.Hit
            self.actionType = ActionType.Hit
            self.actionTimer = 5
            self.lookDirection = direction
            self.changeToHitAnimation(direction)

    def handleHitDamage(self, enemy):
        if self.health > 0:
            if checkEnumValueEquals(self.actionType, ActionType.SpecialAttack):
                self.health -= 15
            else:
                if checkEnumValueEquals(enemy.actionType, ActionType.SpecialAttack):
                    self.health -= 10
                else:
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
        self.changeAttackMaskBasedOnDirection(self.punchLeftMask, self.punchRightMask)

    def changeToLowPunchAnimation(self):
        self.changeSpriteBasedOnDirection(self.lowPunchLeft, self.lowPunchRight)
        self.changeAttackMaskBasedOnDirection(self.lowPunchLeftMask, self.lowPunchRightMask)

    def changeToKickAnimation(self):
        self.changeSpriteBasedOnDirection(self.kickLeft, self.kickRight)
        self.changeAttackMaskBasedOnDirection(self.kickLeftMask, self.kickRightMask)

    def changeToLowKickAnimation(self):
        self.changeSpriteBasedOnDirection(self.lowKickLeft, self.lowKickRight)
        self.changeAttackMaskBasedOnDirection(self.lowKickLeftMask, self.lowKickRightMask)

    @abstractmethod
    def adaptSpecialAttackPosition(self):
        pass

    @abstractmethod
    def adaptSpecialAttackPositionBack(self):
        pass

    def changeToSpecialAttackAnimation(self):
        # needed because special attacks are bigger than normal one and would be async otherwise
        if checkEnumValueEquals(self.lookDirection, Direction.Left) and self.imagesPreloaded:
            self.adaptSpecialAttackPosition()
        self.changeSpriteBasedOnDirection(self.specialAnimationRight, self.specialAnimationLeft)
        self.changeAttackMaskBasedOnDirection(self.specialAnimationLeftMask, self.specialAnimationRightMask)

    def changeToBlockAnimation(self):
        print "change to block with mask"
        self.changeSpriteBasedOnDirectionWithMask(self.blockLeft, self.blockLeftMask, self.blockRight, self.blockRightMask)

    def changeToLowBlockAnimation(self):
        print "change to low block with mask"
        self.changeSpriteBasedOnDirectionWithMask(self.lowBlockLeft, self.lowBlockLeftMask, self.lowBlockRight, self.lowBlockRightMask)

    def changeToDanceAnimation(self):
        self.changeSpriteImage(self.danceAnimation)

    def changeSpriteBasedOnDirection(self, leftRes, rightRes):
        if checkEnumValueEquals(self.lookDirection, Direction.Left):
            self.changeSpriteImage(leftRes)
        elif checkEnumValueEquals(self.lookDirection, Direction.Right):
            self.changeSpriteImage(rightRes)

    def changeSpriteBasedOnDirectionWithMask(self, leftRes, leftMask, rightRes, rightMask):
        if checkEnumValueEquals(self.lookDirection, Direction.Left):
            self.changeSpriteImageWithMask(leftRes, leftMask)
        elif checkEnumValueEquals(self.lookDirection, Direction.Right):
            self.changeSpriteImageWithMask(rightRes, rightMask)

    def changeAttackMaskBasedOnDirection(self, leftRes, rightRes):
        if checkEnumValueEquals(self.lookDirection, Direction.Left):
            self.changeAttackmaskImage(leftRes)
        elif checkEnumValueEquals(self.lookDirection, Direction.Right):
            self.changeAttackmaskImage(rightRes)

    def getImagesPreloaded(self):
        return self.imagesPreloaded

    def preloadImages(self):
        self.changeToSpecialAttackAnimation()
        self.cacheCurrentMasks()
        self.changeToHitAnimation(self.lookDirection)
        self.cacheCurrentMasks()
        self.changeToBlockAnimation()
        self.cacheCurrentMasks()
        self.changeToDuckAnimation()
        self.cacheCurrentMasks()
        self.changeToLowBlockAnimation()
        self.cacheCurrentMasks()
        self.changeToLowKickAnimation()
        self.cacheCurrentMasks()
        self.changeToJumpAnimation()
        self.cacheCurrentMasks()
        self.changeToIdleAnimation()
        self.cacheCurrentMasks()
        self.lookDirection = Direction.Right
        self.changeToSpecialAttackAnimation()
        self.cacheCurrentMasks()
        self.changeToHitAnimation(self.lookDirection)
        self.cacheCurrentMasks()
        self.changeToBlockAnimation()
        self.cacheCurrentMasks()
        self.changeToDuckAnimation()
        self.cacheCurrentMasks()
        self.changeToLowBlockAnimation()
        self.cacheCurrentMasks()
        self.changeToLowKickAnimation()
        self.cacheCurrentMasks()
        self.changeToJumpAnimation()
        self.cacheCurrentMasks()
        self.changeToIdleAnimation()
        self.cacheCurrentMasks()
        self.imagesPreloaded = True

    def update(self):
        if checkEnumValueEquals(self.movementState, MovementState.Moving):
            print "movingPlayer"
            print self.duckState
            if checkEnumValueNotEquals(self.duckState, DuckState.Ducking):
                print self.lookDirection
                moveSpeed = 0
                if checkEnumValueEquals(self.movementSpeed, MovementSpeed.Slow):
                    moveSpeed = 2
                else:
                    moveSpeed = 4

                if checkEnumValueEquals(self.lookDirection, Direction.Left):
                    print "movingPlayerX"
                    self.moveX(-moveSpeed)
                elif checkEnumValueEquals(self.lookDirection, Direction.Right):
                    print "movingPlayerX"
                    self.moveX(moveSpeed)
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

        if self.fastMoveTimer > 0:
            self.fastMoveTimer -= 1

        if self.actionTimer > 0:
            self.actionTimer -= 1
        elif self.actionTimer == 0:
            # temporary fix for issue with special attack on the left side
            if checkEnumValueEquals(self.lookDirection, Direction.Left) and checkEnumValueEquals(self.actionType, ActionType.SpecialAttack) and self.imagesPreloaded:
                self.adaptSpecialAttackPositionBack()
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