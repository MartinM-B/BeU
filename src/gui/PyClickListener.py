__author__ = 'florian'
from abc import ABCMeta, abstractmethod


class PyClickListener(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def onClick(self, anID):
        pass