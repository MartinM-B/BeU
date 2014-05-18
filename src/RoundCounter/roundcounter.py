# this is improved version of animatedsprite which can be found here:
# http://swiftcoder.wordpress.com/2009/04/17/enhanced-animation-code-for-pyglet/

import pyglet
from pyglet.gl import *
from pyglet.text import *

class RoundCounter(object):
    ''' Sprite subclass providing advanced
            playback controls for animated sprites '''

    def __init__(self, batch, player1, player2, x=0, y=0, rounds=3):
        self._blend_src = pyglet.gl.GL_SRC_ALPHA
        self._blend_dest=pyglet.gl.GL_ONE_MINUS_SRC_ALPHA

        self._color = (0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255)

        self._player1 = player1
        self._player2 = player2

        self._startX1 = player1.x
        self._startX2 = player2.x

        self._health = 0
        self._health2 = 0

        self._rounds_to_win = rounds
        self._rounds1 = 0
        self._rounds2 = 0

        self._width = 60
        self._height = 50

        self._framecounter = 0
        self._game_over = 0

        self._x = x
        self._y = y

        self._label = pyglet.text.Label("1:1", font_name='Times New Roman', font_size=36, x=60, y=60, anchor_x='center', anchor_y='center')
        self._label_game_over = pyglet.text.Label("1:1", font_name='Times New Roman', font_size=45, x=60, y=60, anchor_x='center', anchor_y='center')
        self._label_player_win = pyglet.text.Label("1:1", font_name='Times New Roman', font_size=45, x=60, y=60, anchor_x='center', anchor_y='center')

    def update(self):
        if self._player1.health == 0:
            self._rounds2 += 1
            self.reset_players()

        if self._player2.health == 0:
            self._rounds1 += 1
            self.reset_players()

        if(self._rounds1 >= self._rounds_to_win):
            self._game_over = 1
        elif(self._rounds2 >= self._rounds_to_win):
            self._game_over = 2


    def reset_players(self):
        self._player1.health = 100
        self._player2.health = 100
        self._player1.x = 30
        self._player2.x = 300

    def draw(self):
        self.draw_background()
        self.draw_label()

        if(self._framecounter > 200):
            self._game_over = 0
            self._framecounter = 0
            self._rounds1 = 0
            self._rounds2 = 0

        if(self._game_over == 1):
            self.draw_label_over()
            self.draw_label_win("1")
        elif(self._game_over == 2):
            self.draw_label_over()
            self.draw_label_win("2")

    def draw_label_over(self):
        self._framecounter += 1
        self._label_game_over.text = "GAME OVER"
        self._label_game_over._x = 200
        self._label_game_over._y = 200
        self._label_game_over.color = (41, 41, 41, 255)
        self._label_game_over.draw()

    def draw_label_win(self, no=""):
        self._label_player_win.text = "Player " + no + " wins!"
        self._label_player_win._x = 200
        self._label_player_win._y = 100
        self._label_player_win.color = (41, 41, 41, 255)
        self._label_player_win.draw()

    def draw_background(self):
        color = (200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200)
        self.draw_rect(self._x, self._y, self._width, self._height, color)

    def draw_label(self):
        self._label.text = str(self._rounds1) + " - " + str(self._rounds2)
        self._label._x = self._x + self._width - 30
        self._label._y = self._y + self._height - 22
        self._label.font_size = (self._height-25)/1.33333
        self._label.color = (41, 41, 41, 255)
        self._label.draw()

    def draw_rect(self, x, y, w, h, color=(0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 255)):
        glPushMatrix()
        x1 = x
        y1 = y
        y2 = y1 + h
        x2 = x1 + w
        pyglet.graphics.draw(4, pyglet.graphics.GL_QUADS,
                             ('v2f', (x1, y1, x1, y2, x2, y2, x2, y1)),
                             ('c3B', color))
        glPopMatrix()









