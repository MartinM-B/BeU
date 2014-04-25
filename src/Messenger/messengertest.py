__author__ = 'florian'


from PyMessage import *
from PyMessenger import *


msger1 = PyMessenger()
msger2 = PyMessenger()
msger3 = PyMessenger()


# msger1.printfpslimit()
# msger2.printfpslimit()
# msger3.printfpslimit()
# msger1.myclock.set_fps_limit(30)
# print "changed"
#
# msger1.printfpslimit()
# msger2.printfpslimit()
#
# print "changed again"
# msger2.myclock.set_fps_limit(20)
# msger3.printfpslimit()

msger1.subscribe("msg1", "receiver1")
msger1.subscribe("msg2", "receiver2")
msger1.subscribe("msg1", "superreceiver")

msger1.send("msg1", 100)


# msger1.printreceivers()
# msger1.printqueue()
msger1.execute()