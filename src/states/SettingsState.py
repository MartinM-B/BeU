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
        s1 = self.settings
        if anID == 'music_louder':
            vol = s1._volume
            if(vol < 100):
                s1.setVolume(vol+1)
                self.labelVolume.text = str(vol+1)

        elif anID == 'music_quieter':
            vol = s1._volume
            if(vol > 0):
                s1.setVolume(vol-1)
                self.labelVolume.text = str(vol-1)

        elif anID == 'time_Up':
            time = s1._time
            if(time < 100):
                s1.setTime(time+1)
                self.labelTime.text = str(time+1)

        elif anID == 'time_Down':
            time = s1._time
            if(time > 0):
                s1.setTime(time-1)
                self.labelTime.text = str(time-1)


    def onExit(self):
        print 'onExit'
        if self.isActive:
            self.deleteScreen()
            self._active = False

    def onEnter(self):
        if not self.isActive:
            self._active = True
        self.initalizeState()

    def initalizeState(self):
        self.settings = Settings()
        #add background sprites
        backgroundImage = gui_resources.background
        background1 = pyglet.sprite.Sprite(backgroundImage, x=0,  y=0, batch=self._batch, group=self._background)

        titleImage = gui_resources.title_big
        title = pyglet.sprite.Sprite(titleImage, x=(self._window.width/1.5/2),  y=(self._window.height/1.5/2),
                                     batch=self._batch, group=self._foreground)

        button_res = gui_resources.setting_small
        button_res_active = gui_resources.setting_small_selected

        layouter = PyLayouter()
        point1 = PyPoint(300, 200)
        point2 = PyPoint(600, 200)
        x1 = 500
        y1 = 100

        point3 = PyPoint(300, 400)
        point4 = PyPoint(600, 400)
        x2 = 500
        y2 = 450

        self.labelTime = pyglet.text.Label(text=str(self.settings._time), font_name='Times New Roman', font_size=24, x=x2, y=y2,
                                       width=30, height=30, anchor_x='left',
                                       anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')

        self.labelVolume = pyglet.text.Label(text=str(self.settings._volume), font_name='Times New Roman', font_size=24, x=x1, y=y1,
                                       width=100, height=300, anchor_x='left',
                                       anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')


        self.louderButton = PyButton('music_louder', self, point1, self._batch, button_res,
                                     button_res_active, self._foreground,'louder', 0.75)
        self.quieterButton = PyButton('music_quieter', self, point2, self._batch, button_res,
                                      button_res_active, self._foreground, 'quieter', 0.75)
        self.timeUpButton = PyButton('time_Up', self, point3, self._batch, button_res,
                                     button_res_active, self._foreground, 'up', 0.75)
        self.timeDownButton = PyButton('time_Down', self, point4, self._batch, button_res,
                                        button_res_active, self._foreground, 'down', 0.75)

        self.timeUpButton.setActive(True)
        layouter.addButton(self.quieterButton)
        layouter.addButton(self.louderButton)
        layouter.addButton(self.timeDownButton)
        layouter.addButton(self.timeUpButton)

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