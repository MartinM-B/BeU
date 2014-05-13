
class PyMessage(object):

    type = "msg"
    timestamp = 0

    def __init__(self, atype, atime):
        self.type = atype
        self.timestamp = atime

    def getType(self):
        return self.type
