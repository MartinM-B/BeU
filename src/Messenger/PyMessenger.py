__author__ = 'florian'

from Queue import *
from PyMessage import *
from src.timer.PyTimer import *


class PyMessenger(object):

    myqueue = Queue()
    receivers = {}

    def __init__(self):
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

        timer = PyTimer()
        deltatime = timer.getDeltaTime()

        for msg in self.myqueue.queue:
            if msg.timestamp < deltatime:
                length = len(self.receivers.get(msg.type))
                temp = 0
                while temp < length:
                    #call the receiver
                    print self.receivers[msg.type][temp]
                    temp += 1

    def printreceivers(self):
        print self.receivers

    def printqueue(self):
        print self.myqueue