__author__ = 'florian'

import time


class PyTimer(object):

    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None
    _time = time.time()

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if PyTimer.__instance is None:
            # Create and remember instance
            PyTimer.__instance = PyTimer.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = PyTimer.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

    def startTimer(self):
        self._time = time.time()

    def getDeltaTime(self):
        self._deltaTime = time.time() - self._time
        return self._deltaTime