__author__ = 'florian'

from src.Messenger.PyMessage import PyMessage
from src.gui import gui_resources
from src.gui.PyButton import PyButton
from src.gui.PyLayouter import PyLayouter
from src.gui.PyPoint import PyPoint
from src.states.StateEnum import States
from State import *
from src.gui.PyClickListener import *
from src.settings import *
from pyglet.gl import *
from .. import gui_resources
from ..InputHandling.PlayerOneKeyboardInputHandler import PlayerOneKeyboardInputHandler
from ..InputHandling.PlayerTwoKeyboardInputHandler import PlayerTwoKeyboardInputHandler
from pyglet.window import key

class CharSelectState(State, PyClickListener):

    def onClick(self, anID):
        s1 = Settings()
        #print id(s1), s1.spam()
        if anID == 'player1Viking':
            print 'change player1 to viking in singleton'
            s1.setPlayer1Viking()
            self.finishedPlayer1 = True

        elif anID == 'player1Symbiont':
            print 'change player1 to symbiont in singleton'
            s1.setPlayer1Symbiont()
            self.finishedPlayer1 = True

        elif anID == 'player2Viking':
            print 'change player2 to viking in singleton'
            s1.setPlayer2Viking()
            self.finishedPlayer2 = True

        elif anID == 'player2Symbiont':
            print 'change player2 to symbiont in singleton'
            s1.setPlayer2Symbiont()
            self.finishedPlayer2 = True

        if self.finishedPlayer1 == True:
            if self.finishedPlayer2 == True:
                gameMessage = PyMessage(self._type, States.Game)
                self._messenger.send(gameMessage)

    
    def onExit(self):
        print 'onExit'
        if self.isActive:
            self.deleteScreen()
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True

        self.inputHandler1 = PlayerOneKeyboardInputHandler("")
        self.inputHandler2 = PlayerTwoKeyboardInputHandler("")
        self.initalizeState()
        print 'onEnter Start'

    def initalizeState(self):
        # make layouter
        # make all the buttons
        # add the buttons to the layouter
        # this state is the listener for all the created buttons in this state
        # react to all the buttons in the onClick
        # self._layouter = PYLAYOUTER()
        self.finishedPlayer1 = False
        self.finishedPlayer2 = False

        #background
        scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 2
        self.background_sprite = pyglet.sprite.Sprite(gui_resources.background, 0, 0, batch=self._batch, group=self._background)
        #self.background_sprite.scale = scaleY

        #chains
        self.chain_sprite1 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 2.0/10.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite2 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 4.0/10.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite3 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 6.0/10.0)-(gui_resources.chain.width/2.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite4 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 8.0/10.0)-(gui_resources.chain.width/2.0), 0, batch=self._batch, group=self._background)

        self.chain_sprite1.scale = scaleY
        self.chain_sprite2.scale = scaleY
        self.chain_sprite3.scale = scaleY
        self.chain_sprite4.scale = scaleY

        #title
        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.title_big.width) * scaleY / 2.0)
        spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.title_big.height) / 2.0) * 2.1

        self.title_sprite =  pyglet.sprite.Sprite(gui_resources.title_big, spritePosX, spritePosY, batch=self._batch, group=self._foreground)
        self.title_sprite.scale = scaleY
        self.title_label = pyglet.text.Label(text="Select Your Character", font_name='Times New Roman', font_size=24,
                                       x=spritePosX + self.title_sprite.width/2,y=spritePosY + 18,
                                       width=self.title_sprite.width, height=self.title_sprite.height,
                                       anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')

        #leftbox
        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width*scaleY))*7.0/8.0
        spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_big.height) / 2.0) * 5.5

        self.character_big_left = pyglet.sprite.Sprite(gui_resources.character_big, spritePosX, spritePosY, batch=self._batch, group=self._foreground)
        self.character_big_left.scale = scaleY

        #leftimage

        #Todo add left image

        #leftlabel

        self.character_big_left_label = pyglet.text.Label(text="Viking", font_name='Times New Roman', font_size=24,
                                       x=spritePosX + gui_resources.character_big.width*scaleY -10 ,y=spritePosY + 45,
                                       width=self.character_big_left.width, height=self.character_big_left.height,
                                       anchor_x='right', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')


        #rightbox
        spritePosX = (self._window.width / 1.5 / 2.0) + ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width * scaleY)) *1.0/8.0

        self.character_big_right = pyglet.sprite.Sprite(gui_resources.character_big, spritePosX, spritePosY, batch=self._batch, group=self._foreground)
        self.character_big_right.scale = scaleY

        #rightimage

        #Todo add right image

        #rightlabel

        self.character_big_right_label = pyglet.text.Label(text="Viking", font_name='Times New Roman', font_size=24,
                                       x=spritePosX +10 ,y=spritePosY + 45,
                                       width=self.character_big_right.width, height=self.character_big_right.height,
                                       anchor_x='left', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')

        #buttonbox
        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.character_background.width) *scaleY / 2.0)
        spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_background.height) / 2.0) * 0.2

        self.character_background =  pyglet.sprite.Sprite(gui_resources.character_background, spritePosX, spritePosY, batch=self._batch, group=self._background)
        self.character_background.scale = scaleY

        #buttons

        print 'init all the buttons'
        #layouter = PyLayouter()
        self.button_res = gui_resources.character_small
        self.button_res_active1 = gui_resources.character_small_selected1
        self.button_res_active2 = gui_resources.character_small_selected2

        #self.button_res.scale = scaleY
        #self.button_res_active1.scale = scaleY
        #self.button_res_active2.scale = scaleY

        point1 = PyPoint((self._window.width/1.5 * 2.0/10.0)+(gui_resources.character_small.width/4.0), spritePosY + gui_resources.character_small.height/30.0)
        point2 = PyPoint((self._window.width/1.5 * 3.0/10.0)+(gui_resources.character_small.width/4.0), spritePosY + gui_resources.character_small.height/30.0)
        point3 = PyPoint((self._window.width/1.5 * 6.0/10.0)-(gui_resources.character_small.width/8.0), spritePosY + gui_resources.character_small.height/30.0)
        point4 = PyPoint((self._window.width/1.5 * 7.0/10.0)-(gui_resources.character_small.width/8.0), spritePosY + gui_resources.character_small.height/30.0)
        self.Player1VikingButton = PyButton('player1Viking', self, point1, self._batch, self.button_res, self.button_res_active1, self._foreground,
                                '')
        self.Player1SymbiontButton = PyButton('player1Symbiont', self, point2, self._batch, self.button_res, self.button_res_active1,
                                  self._foreground, '')

        self.Player2VikingButton = PyButton('player2Viking', self, point3, self._batch, self.button_res, self.button_res_active2, self._foreground,
                              '')
        self.Player2SymbiontButton = PyButton('player2Symbiont', self, point4, self._batch, self.button_res, self.button_res_active2, self._foreground,
                              '')

        self.Player1VikingButton.setScale(scaleY)
        self.Player1SymbiontButton.setScale(scaleY)
        self.Player2VikingButton.setScale(scaleY)
        self.Player2SymbiontButton.setScale(scaleY)




        self.Player1VikingButton.setActive(True)
        self.Player2VikingButton.setActive(True)

        #layouter.addButton(self.Player1VikingButton)
        #layouter.addButton(self.Player1SymbiontButton)

        #layouter.addButton(self.Player2VikingButton)
        #layouter.addButton(self.Player2SymbiontButton)

        #self._layouter = layouter

    def deleteScreen(self):
        self.Player1VikingButton.delete()
        self.Player1SymbiontButton.delete()
        self.Player2VikingButton.delete()
        self.Player2SymbiontButton.delete()
        self.background_sprite.delete()
        self.title_sprite.delete()
        self.title_label.delete()
        self.chain_sprite1.delete()
        self.chain_sprite2.delete()
        self.chain_sprite3.delete()
        self.chain_sprite4.delete()
        self.character_background.delete()
        self.character_big_left.delete()
        self.character_big_left_label.delete()
        self.character_big_right.delete()
        self.character_big_right_label.delete()


    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handleKeyPress(symbol, modifiers)

        if symbol == key.ENTER:
            gameMessage = PyMessage(self._type, States.Game)
            self._messenger.send(gameMessage)


    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)

        #handle inputs for player 1
        if self.inputHandler1.checkKick(symbol):
            if self.Player1VikingButton.active == True:
                print 'change player1 to viking in singleton'
                s1.setPlayer1Viking()

                #change picture and label to viking
                self.character_big_left_label.delete()
                scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 2
                spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width*scaleY))*7.0/8.0
                spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_big.height) / 2.0) * 5.5
                self.character_big_left_label = pyglet.text.Label(text="Viking", font_name='Times New Roman', font_size=24,
                                       x=spritePosX + gui_resources.character_big.width*scaleY -10 ,y=spritePosY + 45,
                                       width=self.character_big_left.width, height=self.character_big_left.height,
                                       anchor_x='right', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')

                #self.finishedPlayer1 = True
            elif self.Player1SymbiontButton.active == True:
                print 'change player1 to viking in singleton'
                s1.setPlayer1Symbiont()

                #change picture and label to symbiont
                self.character_big_left_label.delete()
                scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 2
                spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width*scaleY))*7.0/8.0
                spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_big.height) / 2.0) * 5.5
                self.character_big_left_label = pyglet.text.Label(text="Symbiont", font_name='Times New Roman', font_size=24,
                                       x=spritePosX + gui_resources.character_big.width*scaleY -10 ,y=spritePosY + 45,
                                       width=self.character_big_left.width, height=self.character_big_left.height,
                                       anchor_x='right', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')

                #self.finishedPlayer1 = True

            #if self.finishedPlayer2 == True:
            #    gameMessage = PyMessage(self._type, States.Game)
            #    self._messenger.send(gameMessage)


        if self.inputHandler1.checkWalkLeft(symbol):
            self.Player1VikingButton.setActive(True)
            self.Player1SymbiontButton.setActive(False)

        if self.inputHandler1.checkWalkRight(symbol):
            self.Player1VikingButton.setActive(False)
            self.Player1SymbiontButton.setActive(True)

        #handle inputs for player 2
        if self.inputHandler2.checkKick(symbol):
            if self.Player2VikingButton.active == True:
                print 'change player2 to viking in singleton'
                s1.setPlayer2Viking()

                #change picture and label to viking
                self.character_big_right_label.delete()
                scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 2
                spritePosX = (self._window.width / 1.5 / 2.0) + ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width * scaleY)) *1.0/8.0
                spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_big.height) / 2.0) * 5.5
                self.character_big_right_label = pyglet.text.Label(text="Viking", font_name='Times New Roman', font_size=24,
                                       x=spritePosX +10 ,y=spritePosY + 45,
                                       width=self.character_big_right.width, height=self.character_big_right.height,
                                       anchor_x='left', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')


                #self.finishedPlayer2 = True
            elif self.Player2SymbiontButton.active == True:
                print 'change player2 to viking in singleton'
                s1.setPlayer2Symbiont()

                #change picture and label to symbiont
                #change picture and label to viking
                self.character_big_right_label.delete()
                scaleY = (self._window.height / (gui_resources.creditScreen.height * 1.0)) / 2
                spritePosX = (self._window.width / 1.5 / 2.0) + ((self._window.width / 1.5 / 2.0) - (gui_resources.character_big.width * scaleY)) *1.0/8.0
                spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.character_big.height) / 2.0) * 5.5
                self.character_big_right_label = pyglet.text.Label(text="Symbiont", font_name='Times New Roman', font_size=24,
                                       x=spritePosX +10 ,y=spritePosY + 45,
                                       width=self.character_big_right.width, height=self.character_big_right.height,
                                       anchor_x='left', anchor_y='top', color=(0, 0, 0, 255), batch=self._batch, halign='right')

                #self.finishedPlayer2 = True

            #if self.finishedPlayer1 == True:
            #    gameMessage = PyMessage(self._type, States.Game)
            #    self._messenger.send(gameMessage)

        if self.inputHandler2.checkWalkLeft(symbol):
            self.Player2VikingButton.setActive(True)
            self.Player2SymbiontButton.setActive(False)

        if self.inputHandler2.checkWalkRight(symbol):
            self.Player2VikingButton.setActive(False)
            self.Player2SymbiontButton.setActive(True)