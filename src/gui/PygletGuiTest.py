import pyglet
from pyglet_gui.theme import Theme
from pyglet_gui.gui import Label
from pyglet_gui.manager import Manager
from pyglet_gui.buttons import Button

window = pyglet.window.Window(640, 480, resizable=True, vsync=True)
batch = pyglet.graphics.Batch()

theme = Theme({"font": "Lucida Grande",
               "font_size": 12,
               "text_color": [255, 255, 255, 255],
               "gui_color": [255, 0, 0, 255],
               "button": {
                   "down": {
                       "image": {
                           "source": "button-down.png",
                           "frame": [8, 6, 2, 2],
                           "padding": [18, 18, 8, 6]
                       },
                       "text_color": [0, 0, 0, 255]
                   },
                   "up": {
                       "image": {
                           "source": "button.png",
                           "frame": [6, 5, 6, 3],
                           "padding": [18, 18, 8, 6]
                       }
                   }
               }
              }, resources_path='../../resources/theme')

label = Label('Hello world')

@window.event
def on_draw():
    window.clear()
    batch.draw()

def callback(is_pressed):
    print('Button was pressed to state', is_pressed)

button = Button('Hello world', on_press=callback)

#Manager(label, window=window, theme=theme, batch=batch)
Manager(button, window=window, theme=theme, batch=batch)

pyglet.app.run()