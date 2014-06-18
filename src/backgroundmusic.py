__author__ = 'Martin'

import pyglet
from pyglet.gl import *
import pyglet.media.avbin
import pyglet.media

class BackgroundMusic(object):

    def __init__(self):
        self._player = pyglet.media.Player()
        self._player.eos_action = 'loop'

    def add(self, recource):
        self._player.queue(recource)

    def add_filename(self, recource):
        self._player.queue(pyglet.media.load(recource))

    def play(self):
        self._player.play()
