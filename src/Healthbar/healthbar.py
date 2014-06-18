# this is improved version of animatedsprite which can be found here:
# http://swiftcoder.wordpress.com/2009/04/17/enhanced-animation-code-for-pyglet/

import pyglet
from pyglet.gl import *
from pyglet.text import *

from pyglet import gl
from pyglet import graphics
from src.gui.PyColor import *
from src.states.StartState import *


from .. import gui_resources

class HealthBar(object):
    ''' Sprite subclass providing advanced
            playback controls for animated sprites '''

    def __init__(self, batch, window, player1, player2, messenger):
        #self._blend_src = pyglet.gl.GL_SRC_ALPHA
        #self._blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA

        self._player1 = player1
        self._player2 = player2
        self._messenger = messenger

        self._color = (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)
        self._batch = batch

        self._winWidth = window.width/1.5
        self._winHeight = window.height/1.5

        self._vertex_list1 = self._batch.add(4, gl.GL_QUADS, pyglet.graphics.OrderedGroup(1), ('v2f', (0, 0, 0, 0, 0, 0, 0, 0)),
                      ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)))
        self._vertex_list2 = self._batch.add(4, gl.GL_QUADS, pyglet.graphics.OrderedGroup(1), ('v2f', (0, 0, 0, 0, 0, 0, 0, 0)),
                      ('c3B', (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)))

        self._rounds_to_win = 3
        self._rounds1 = 0
        self._rounds2 = 0

        self.background(batch)
        self.timerPic(batch)
        self.set_bar1()
        self.set_bar2()
        self.init_lifes()


    def update(self):
        #self._vertex_list1.delete()
        self.background(self._batch)
        self.timerPic(self._batch)
        self.set_bar1()
        self.set_bar2()

        if self._player1.health <= 0:
            self._rounds2 += 1
            self.reset_players()

        if self._player2.health <= 0:
            self._rounds1 += 1
            self.reset_players()

        if(self._rounds1 >= self._rounds_to_win):
            self._game_over = 1
        elif(self._rounds2 >= self._rounds_to_win):
            self._game_over = 2

        if(self._rounds1 == 1):
            self._star1_3.opacity = 128
        elif(self._rounds1 == 2):
            self._star1_2.opacity = 128
        elif(self._rounds1 == 3):
            self._star1_1.opacity = 128

        if(self._rounds2 == 1):
            self._star2_3.opacity = 128
        elif(self._rounds2 == 2):
            self._star2_2.opacity = 128
        elif(self._rounds2 == 3):
            self._star2_1.opacity = 128

        if(self._rounds1 == 3):
            #orig_img = gui_resources.win1
           # scaling_factor = (self._winWidth*0.4)/orig_img.width
            #self._background1 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.45, self._winHeight*0.45, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
            #self._background1.scale = scaling_factor
            self.goBack()
        elif (self._rounds2 == 3):
            #orig_img = gui_resources.win2
            #scaling_factor = (self._winWidth*0.4)/orig_img.width
            #self._background1 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.45, self._winHeight*0.45, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
           # self._background1.scale = scaling_factor
            self.goBack()


    def goBack(self):
        gameMessage = PyMessage('receiver', States.Start)
        self._messenger.send(gameMessage)

    def reset_players(self):
        self._player1.health = 100
        self._player2.health = 100
        self._player1.x = 30
        self._player2.x = 300


    def background(self, batch):
        orig_img = gui_resources.life_background
        scaling_factor = (self._winWidth*0.4)/orig_img.width
        self._background1 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.05, self._winHeight*0.88, batch=batch, group=pyglet.graphics.OrderedGroup(0))
        self._background1.scale = scaling_factor
        self._background2 = pyglet.sprite.Sprite(orig_img, self._winWidth*0.55, self._winHeight*0.88, batch=batch, group=pyglet.graphics.OrderedGroup(0))
        self._background2.scale = scaling_factor


    def timerPic(self, batch):
        img = gui_resources.timer
        scaling_factor = (self._winWidth*0.175)/img.width
        self._timer = pyglet.sprite.Sprite(img, self._winWidth*0.415, (self._winHeight*0.775), batch=batch, group=pyglet.graphics.OrderedGroup(1))
        self._timer.scale = scaling_factor


    def set_bar1(self):
        bar_width = (self._background1.width*0.9) * (float(self._player1.health)/float(100))
        bar_height = self._background1.height*0.8

        if self._player1.health > 50:
            bar_color = (0, 205, 0, 0, 205, 0, 0, 205, 0, 0, 205, 0)
        elif self._player1.health > 25:
            bar_color = (255, 185, 15, 255, 185, 15, 255, 185, 15, 255, 185, 15)
        else:
            bar_color = (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)

        x1 = self._background1.x + self._background1.width*0.05
        y1 = self._background1.y + self._background1.height*0.2
        x2 = self._background1.x + bar_width
        y2 = self._background1.y + bar_height

        self._vertex_list1.delete()
        self._vertex_list1 = self._batch.add(4, gl.GL_QUADS, pyglet.graphics.OrderedGroup(1),('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
                      ('c3B', bar_color))



        #glPushMatrix()
        #pyglet.graphics.draw(4, gl.GL_QUADS, ('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
        #              ('c3B', bar_color))
        #glPopMatrix()


    def set_bar2(self):
        bar_width = (self._background1.width*0.85) * (float(self._player2.health)/float(100))
        bar_height = self._background1.height*0.8

        if self._player2.health > 50:
            bar_color = (0, 205, 0, 0, 205, 0, 0, 205, 0, 0, 205, 0)
        elif self._player2.health > 25:
            bar_color = (255, 185, 15, 255, 185, 15, 255, 185, 15, 255, 185, 15)
        else:
            bar_color = (255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0)

        x2 = (self._winWidth*0.5) + self._background1.x + self._background1.width*0.95
        y2 = self._background1.y + self._background1.height*0.2
        x1 = (self._winWidth*0.5)+ self._background1.x + self._background1.width*0.95 - bar_width
        y1 = self._background1.y + bar_height

        self._vertex_list2.delete()
        self._vertex_list2 = self._batch.add(4, gl.GL_QUADS, pyglet.graphics.OrderedGroup(1),('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
          ('c3B', bar_color))


    def draw(self):
        self.set_bar1()
        self.set_bar2()


    def init_lifes(self):
        star_img = gui_resources.win
        scaling = (self._winWidth*0.15)/star_img.width
        self._star1_1 = pyglet.sprite.Sprite(star_img, self._winWidth*0.05, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
        self._star1_2 = pyglet.sprite.Sprite(star_img, self._winWidth*0.10, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
        self._star1_3 = pyglet.sprite.Sprite(star_img, self._winWidth*0.15, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))

        self._star2_1 = pyglet.sprite.Sprite(star_img, self._winWidth*0.81, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
        self._star2_2 = pyglet.sprite.Sprite(star_img, self._winWidth*0.86, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))
        self._star2_3 = pyglet.sprite.Sprite(star_img, self._winWidth*0.91, self._winHeight*0.8, batch=self._batch, group=pyglet.graphics.OrderedGroup(1))

    def delete(self):
        self._star1_1.delete()
        self._star1_2.delete()
        self._star1_3.delete()
        self._star2_1.delete()
        self._star2_2.delete()
        self._star2_3.delete()
        self._background1.delete()
        self._background2.delete()
        self._vertex_list2.delete()
        self._vertex_list1.delete()
        self._timer.delete()








