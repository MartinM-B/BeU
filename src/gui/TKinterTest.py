__author__ = 'florian'

from Tkinter import *
from src.timer.PyTimer import *
from src.Messenger.PyMessenger import *
from src.states.StateMachine import *
from src.Messenger.PyMessage import *
from src.states.StateEnum import *


class App:

    type = "Receiver"
    #start the timer on start of the program


    timer = PyTimer()
    timer.startTimer()

    #initialize messenger
    messenger = PyMessenger()

    #initialize Statemachine with a certain type
    stateMachine = StateMachine(type)

    #subscribe to the messenges of the type
    messenger.subscribe(type, stateMachine)

    gameMessage = PyMessage(type, States.Game)

    messenger.send(gameMessage)

    def __init__(self, master):

        frame = Frame(width=1000, height=1000, bg="red", colormap="new")
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.sayHi)
        self.hi_there.pack(side=LEFT)

        self.execute_button = Button(frame, text="Execute", command=self.execute)
        self.execute_button.pack(side=LEFT)

    def sayHi(self):
        print "hi there, everyone!"

    def execute(self):
        print "execute"
        self.messenger.execute()

root = Tk()

app = App(root)

root.mainloop()

root.destroy() # optional; see description below