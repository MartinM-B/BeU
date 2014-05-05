__author__ = 'florian'

from pyglet import clock
from Queue import *
from PyMessage import *


class PyMessenger(object):

    myqueue = Queue()
    receivers = {}

    def __init__(self):
        self.myclock.set_fps_limit(60)
        self.receivers = {}

    def send(self, amsg, atimestamp):
        pymsg = PyMessage(amsg, atimestamp)
        self.myqueue.put(pymsg)

    def subscribe(self, atype, receiver):
        self.receivers.setdefault(atype, []).append(receiver)

    def unsubscribe(self, atype, receiver):
        self.receivers[atype].remove(receiver)

    def cleanup(self):
        self.myqueue.empty()
        self.receivers.clear()

    def execute(self):
        #acces all the receivers inside the queue with a certain key
        #timestamp needs to take action here
        for msg in self.myqueue.queue:
            if msg.type in self.receivers:
                length = len(self.receivers.get(msg.type))
                temp = 0
                while temp < length:
                    print self.receivers[msg.type][temp]
                    temp += 1

    def printreceivers(self):
        print self.receivers

    def printqueue(self):
        print self.myqueue