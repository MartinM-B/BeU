__author__ = 'florian'
from abc import ABCMeta, abstractmethod


"""abstract receiver class"""


class Receiver(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def onReceive(self):
        pass