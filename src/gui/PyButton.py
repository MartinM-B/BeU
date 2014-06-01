__author__ = 'florian'

#class which works with a label and rectangle, reacts if called from the layouter


class PyButton(object):

    def __init__(self, rectangle, text= 0):
        self.rectangle = rectangle
        self.text = text

    def onPressed(self):
        print 'button pressed'

    def drawButton(self):
        print 'draw this button'