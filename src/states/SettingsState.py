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

        elif anID == 'back':
            startMessage = PyMessage(self._type, States.Start)
            self._messenger.send(startMessage)

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

        self.background_sprite = pyglet.sprite.Sprite(gui_resources.background, 0, 0, batch=self._batch, group=self._background)
        scaleY = (self._window.height / (self.background_sprite.height * 1.0))/1.5
        #chains
        self.chain_sprite1 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 2.0/10.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite2 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 4.0/10.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite3 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 6.0/10.0)-(gui_resources.chain.width/2.0), 0, batch=self._batch, group=self._background)
        self.chain_sprite4 =  pyglet.sprite.Sprite(gui_resources.chain, (self._window.width/1.5 * 8.0/10.0)-(gui_resources.chain.width/2.0), 0, batch=self._batch, group=self._background)

        self.chain_sprite1.scale = scaleY
        self.chain_sprite2.scale = scaleY
        self.chain_sprite3.scale = scaleY
        self.chain_sprite4.scale = scaleY

        spritePosX = ((self._window.width / 1.5 / 2.0) - (gui_resources.title_big.width) * scaleY / 2.0)
        spritePosY = ((self._window.height / 1.5 / 2.0) - (gui_resources.title_big.height) / 2.0) * 2.1

        self.title_sprite =  pyglet.sprite.Sprite(gui_resources.title_big, spritePosX, spritePosY, batch=self._batch, group=self._background)
        self.title_sprite.scale = scaleY
        self.title_label = pyglet.text.Label(text="Settings", font_name='Times New Roman', font_size=24,
                                       x=spritePosX + self.title_sprite.width/2,y=spritePosY + 18,
                                       width=self.title_sprite.width, height=self.title_sprite.height,
                                       anchor_x='center', anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')

        self.back_sprite = pyglet.sprite.Sprite(gui_resources.credits, self._window.width*0.125, self._window.height*0.07, group=self._background, batch=self._batch)
        self.back_sprite.scale = scaleY

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

        point_back = PyPoint(20, 50)


        self.labelTime = pyglet.text.Label(text=str(self.settings._time), font_name='Times New Roman', font_size=24, x=x2, y=y2,
                                       width=30, height=30, anchor_x='left',
                                       anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')

        self.labelVolume = pyglet.text.Label(text=str(self.settings._volume), font_name='Times New Roman', font_size=24, x=x1, y=y1,
                                       width=100, height=300, anchor_x='left',
                                       anchor_y='center', color=(0, 0, 0, 255), batch=self._batch, halign='right')


        self.louderButton = PyButton('music_louder', self, point1, self._batch, button_res,
                                     button_res_active, self._foreground,'louder', 0.8)
        self.quieterButton = PyButton('music_quieter', self, point2, self._batch, button_res,
                                      button_res_active, self._foreground, 'quieter', 0.8)
        self.timeUpButton = PyButton('time_Up', self, point3, self._batch, button_res,
                                     button_res_active, self._foreground, 'up', 0.8)
        self.timeDownButton = PyButton('time_Down', self, point4, self._batch, button_res,
                                        button_res_active, self._foreground, 'down', 0.8)
        self.backButton = PyButton('back', self, point_back, self._batch, button_res,
                                button_res_active, self._foreground, 'Back', 1)


        self.timeUpButton.setActive(True)
        layouter.addButton(self.backButton)
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
        self.labelVolume.delete()
        self.labelTime.delete()
        self.title_sprite.delete()
        self.title_label.delete()
        self.chain_sprite4.delete()
        self.chain_sprite3.delete()
        self.chain_sprite2.delete()
        self.chain_sprite1.delete()
        self.background_sprite.delete()
        self.backButton.delete()
        self.back_sprite.delete()


    def handleKeyPress(self, symbol, modifiers):
        print 'startState press'
        self._layouter.handleKeyPress(symbol, modifiers)

    def handleKeyRelease(self, symbol, modifiers):
        print 'startState release'
        self._layouter.handleKeyRelease(symbol, modifiers)