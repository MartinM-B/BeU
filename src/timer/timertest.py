__author__ = 'florian'

from PyTimer import *

_timer = PyTimer()

_timer.startTimer()

_deltaTime = _timer.getDeltaTime()

print "time"
print time.asctime(time.localtime(_deltaTime))

