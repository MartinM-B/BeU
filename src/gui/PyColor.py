__author__ = 'florian'

#container for rgb values


class PyColor(object):

    def __init__(self, r, g, b):
        self.r = self.checkColor(r)
        self.g = self.checkColor(g)
        self.b = self.checkColor(b)

    def checkColor(self, c):
        if c < 0:
            c = 0
        if c > 255:
            c = 255
        return c