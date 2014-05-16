__author__ = 'florian'
from abc import ABCMeta, abstractmethod


class Receiver(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def onReceive(self, msg):
        pass

