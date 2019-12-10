from tkinter import *
from tkinter.constants import *

import cs101events
from cs101events import cs101events

myEvents = cs101events()

root = Tk()

def displayNextEvent():
    
    eventText = Label(root, text="Next Event: " + str(myEvents.getNextEvent()))
    eventText.grid(row=4)

def addEvent():
    myEvents.addNewEvent(eventEntry.get(),dayEntry.get(),monthEntry.get(),yearEntry.get())
    eventTexty = Label(root, text="New Event Added Successfully!")
    
    eventTexty.grid(row=3)

        
topFrame = Frame(root)
topFrame.grid(row=2, column=3)


buttonAdd = Button(topFrame, text="Add New Event", command=addEvent)
buttonAdd.grid(row=2)
buttonNext = Button(topFrame, text="Next Event", command=displayNextEvent)
buttonNext.grid(row=2, column=4)

eventLabel = Label(root, text="Event Name:", )
dayLabel = Label(root, text="Day: ")
monthLabel = Label(root, text="Month: ")
yearLabel = Label(root, text="Year: ")
addEventLabel = Label(root, text="Add New Event")


addEventLabel.grid(row=0,column=0)
eventLabel.grid(row=0,column=1)
dayLabel.grid(row=1, column=0)
monthLabel.grid(row=1, column=2)
yearLabel.grid(row=1, column=4)


eventEntry = Entry(root)
dayEntry = Entry(root)
monthEntry = Entry(root)
yearEntry = Entry(root)
eventEntry.grid(row=0, column=1)
dayEntry.grid(row=1, column=1)
monthEntry.grid(row=1, column=3)
yearEntry.grid(row=1, column=5)
#continously display the window
root.mainloop()
