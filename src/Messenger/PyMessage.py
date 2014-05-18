
class PyMessage(object):

    type = "type"
    timestamp = 0
    msg = "msg"

    def __init__(self, atype, atime, amsg):
        self.type = atype
        self.timestamp = atime
        self.msg = amsg

    def __init__(self, atype, amsg):
        self.type = atype
        self.timestamp = 0
        self.msg = amsg

    def getType(self):
        return self.type
