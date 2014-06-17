__author__ = 'florian'

from Queue import *
from PyMessage import *
from src.timer.PyTimer import *


class PyMessenger(object):

    __myqueue = Queue()
    __receivers = {}

    def __init__(self):
        self.__receivers = {}

    def send(self, type, time, msg):
        pymsg = PyMessage(type, time, msg)
        self.__myqueue.put(pymsg)

    def send(self, type, msg):
        pymsg = PyMessage(type, msg)
        self.__myqueue.put(pymsg)

    def send(self, message):
        self.__myqueue.put(message)

    def subscribe(self, atype, receiver):
        self.__receivers.setdefault(atype, []).append(receiver)

    def unsubscribe(self, atype, receiver):
        self.__receivers[atype].remove(receiver)

    def cleanUp(self):
        self.__myqueue.empty()
        self.__receivers.clear()

    def execute(self):
        #acces all the receivers inside the queue with a certain key
        #timestamp needs to take action here

        __timer = PyTimer()
        __deltatime = __timer.getDeltaTime()

        for msg in self.__myqueue.queue:
            if msg.timestamp < __deltatime:
                length = len(self.__receivers.get(msg.type))
                temp = 0
                while temp < length:
                    #call the receiver
                    self.__receivers[msg.type][temp].onReceive(msg)
                    temp += 1
                self.__myqueue.queue.remove(msg)
                break


    def printReceivers(self):
        print self.__receivers

    def printQueue(self):
        print self.__myqueue