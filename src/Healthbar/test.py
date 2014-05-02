#!/usr/bin/env python

import pyglet

from src.Healthbar import healthbar


window = pyglet.window.Window()

sprite = healthbar.HealthBar(200, 200, 200, 50)
sprite.set_health(100)
@window.event
def on_draw():
    window.clear()
    sprite.draw()
@window.event
def on_key_press(symbol, mod):
    if symbol == 49:
        sprite.set_active_lookup(1)
    if symbol == 50:
        sprite.set_active_lookup(2)

pyglet.app.run()

