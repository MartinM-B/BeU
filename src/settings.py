__author__ = 'SARAH'

class Settings(object):
    """ A python singleton """

    class __impl:
        """ Implementation of the singleton interface """

        def spam(self):
            """ Test method, return singleton id """
            return id(self)

    # storage for the instance reference
    __instance = None
    _player1 = 0
    _player2 = 0
    _volume = 100
    _time = 99

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Settings.__instance is None:
            # Create and remember instance
            Settings.__instance = Settings.__impl()

        # Store instance reference as the only member in the handle
        self.__dict__['_Singleton__instance'] = Settings.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

    def setPlayer1Viking(self):
        Settings._player1 = 0

    def setPlayer1Symbiont(self):
        Settings._player1 = 1

    def setPlayer2Viking(self):
        Settings._player2 = 0

    def setPlayer2Symbiont(self):
        Settings._player2 = 1

    def setVolume(self, volume):
        Settings._volume = volume

    def setTime(self, time):
        Settings._time = time

# Test it
s1 = Settings()
print id(s1), s1.spam()
print Settings._player1
s1.setPlayer1Symbiont()
print Settings._player1

s2 = Settings()
print id(s2), s2.spam()
print Settings._player1

# Sample output, the second (inner) id is constant:
# 33560400 33568048
# 33560400 33568048