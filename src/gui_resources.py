__author__ = 'florian'
import pyglet
pyglet.resource.path = ['../resources/Background', '../resources/ScreenElements', '../resources/Screens']
pyglet.resource.reindex()

background = pyglet.resource.image("background.png")
box = pyglet.resource.image("box.png")
box_selected = pyglet.resource.image("box_selected.png")
chain = pyglet.resource.image("chain.png")
character_background = pyglet.resource.image("character_background.png")
character_big = pyglet.resource.image("character_big.png")
character_small = pyglet.resource.image("character_small.png")
character_small_selected1 = pyglet.resource.image("character_small_selected1.png")
character_small_selected2 = pyglet.resource.image("character_small_selected2.png")
credits = pyglet.resource.image("credits.png")
life = pyglet.resource.image("life.png")
life_background = pyglet.resource.image("life_background.png")
main = pyglet.resource.image("main.png")
main_broken = pyglet.resource.image("main_broken.png")
setting_big = pyglet.resource.image("setting_big.png")
setting_big_selected = pyglet.resource.image("setting_big_selected.png")
setting_small = pyglet.resource.image("setting_small.png")
setting_small_selected = pyglet.resource.image("setting_small_selected.png")
slider = pyglet.resource.image("slider.png")
timer = pyglet.resource.image("timer.png")
title_big = pyglet.resource.image("title_big.png")
title_small = pyglet.resource.image("title_small.png")
win = pyglet.resource.image("win.png")

creditScreen = pyglet.resource.image("CreditScreen.png")
creditBackground = pyglet.resource.image("CreditBack.png")
startScreen = pyglet.resource.image("MainScreen.png")

vikingBig = pyglet.resource.image("Viking.png")
vikingSmall = pyglet.resource.image("Viking_small.png")

symbiontBig = pyglet.resource.image("Symbiont.png")
symbiontSmall = pyglet.resource.image("Symbiont_small.png")

#backgrounds
bg_assembly = pyglet.resource.image("assembly.jpg")
bg_beach = pyglet.resource.image("beach.png")
bg_underground = pyglet.resource.image("beach.png")
