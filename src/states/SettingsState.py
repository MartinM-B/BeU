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

class SettingsState(State, PyClickListener):

    def onClick(self, anID):
        s1 = Settings()
        if anID == 'music_louder':
            print 'louder'
            vol = s1._volume
            if(vol < 100):
                s1.setVolume(vol+1)

        elif anID == 'music_quieter':
            print 'quieter'
            vol = s1._volume
            if(vol > 0):
                s1.setVolume(vol-1)

        elif anID == 'timeUp':
            print 'change player2 to viking in singleton'
            time = s1._time
            if(time < 100):
                s1.setTime(time+1)

        elif anID == 'timeDown':
            print 'change player2 to symbiont in singleton'
            time = s1._time
            if(time > 0):
                s1.setTime(time-1)


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
        background1 = pyglet.sprite.Sprite(backgroundImage, x=0,  y=0, batch=self._batch, group=self._background)

        titleImage = gui_resources.title_big
        title = pyglet.sprite.Sprite(titleImage, x=(self._window.width/1.5/2),  y=(self._window.height/1.5/2),
                                     batch=self._batch, group=self._foreground)

        button_res = gui_resources.setting_small
        button_res_active = gui_resources.setting_small_selected

        print 'init all the buttons'
        layouter = PyLayouter()

        point1 = PyPoint(100, 200)
        point2 = PyPoint(400, 200)
        point3 = PyPoint(100, 400)
        point4 = PyPoint(400, 400)

        self.louderButton = PyButton('music_louder', self, point1, self._batch, button_res,
                                     button_res_active, self._foreground,'louder')
        self.quieterButton = PyButton('music_quieter', self, point2, self._batch, button_res,
                                      button_res_active, self._foreground, 'quieter')
        self.timeUpButton = PyButton('timeUp', self, point3, self._batch, button_res,
                                     button_res_active, self._foreground, 'up')
        self.timeDownButton = PyButton('timeDown', self, point4, self._batch, button_res,
                                        button_res_active, self._foreground, 'down')

        self.quieterButton.setActive(True)

        layouter.addButton(self.louderButton)
        layouter.addButton(self.quieterButton)
        layouter.addButton(self.timeUpButton)
        layouter.addButton(self.timeDownButton)

        self._layouter = layouter

    def deleteScreen(self):
        self.louderButton.delete()
        self.quieterButton.delete()
        self.timeUpButton.delete()
        self.timeDownButton.delete()

    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)