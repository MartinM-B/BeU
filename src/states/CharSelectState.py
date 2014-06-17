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

        #add background sprites
        backgroundImage = gui_resources.background
        background1 = pyglet.sprite.Sprite(backgroundImage, x=0,  y=0, batch=self._batch, group=self._foreground)

        chainImage = gui_resources.chain
        chain1 = pyglet.sprite.Sprite(chainImage, x=(self._window.width/1.5/2),  y=0, batch=self._batch, group=self._foreground)
        chain2 = pyglet.sprite.Sprite(chainImage, x=(self._window.width/1.5/2),  y=0, batch=self._batch, group=self._foreground)
        chain3 = pyglet.sprite.Sprite(chainImage, x=(self._window.width/1.5/2),  y=0, batch=self._batch, group=self._foreground)
        chain4 = pyglet.sprite.Sprite(chainImage, x=(self._window.width/1.5/2),  y=0, batch=self._batch, group=self._foreground)

        titleImage = gui_resources.title_big
        title = pyglet.sprite.Sprite(titleImage, x=(self._window.width/1.5/2),  y=(self._window.height/1.5/2), batch=self._batch, group=self._foreground)


        print 'init all the buttons'
        layouter = PyLayouter()
        button_res = gui_resources.box
        button_res_active = gui_resources.box_selected
        point1 = PyPoint(50, 50)
        point2 = PyPoint(50, 180)
        point3 = PyPoint(50, 310)
        self.Player1VikingButton = PyButton('player1Viking', self, point1, self._batch, button_res, button_res_active, self._foreground,
                                'Credits')
        self.Player1SymbiontButton = PyButton('player1Symbiont', self, point2, self._batch, button_res, button_res_active,
                                  self._foreground, 'Settings')

        self.Player2VikingButton = PyButton('player2Viking', self, point3, self._batch, button_res, button_res_active, self._foreground,
                              'Fight')
        self.Player1VikingButton.setActive(True)
        layouter.addButton(self.Player1VikingButton)
        layouter.addButton(self.Player1SymbiontButton)
        layouter.addButton(self.Player2VikingButton)

        self._layouter = layouter

    def deleteScreen(self):
        self.Player1VikingButton.delete()
        self.Player1SymbiontButton.delete()
        self.Player2VikingButton.delete()

    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)