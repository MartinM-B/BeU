#!/usr/bin/env python

import pyglet

from src.Healthbar import healthbar


window = pyglet.window.Window()

batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)

test_healthbar = healthbar.HealthBar(batch, window)

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.app.run()

