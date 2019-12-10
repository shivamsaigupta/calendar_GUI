#---------------------------------------------------------------------------
# This file gives you a basic GUI application with which you can build your
# GUI.

# In tkinter, we use the "grid" Layout Manager to arrange the different 
# widgets (i.e. Frames, Labels, Buttons, etc) on the screen as we like.
# The grid layout manager treats UI.

# In tkinter, we use the "grid" Layout Manager to arrange the different 
# widgets (i.e. Frames, Labels, Buttons, etc) on the screen as we like.
# We should first create a Frame, and use that to hold other widgets in it.
# A Frame can contain other Frames within it, which can contain widgets.
# "grid" treats each Frame as a rectangle having rows and columns, but it 
# has two problems or peculiarities:
# 1. if a row or a column has no widgets in any of its "cells", then grid
#    layout will not show that row or column at all!
# 2. unless we use special instructions in our code, grid layout automatically
#    reduces the width of a column or the height of a row to that of the
#    largest widget in any of the cells of that column or row.
# Because of the above two points, you see strange and difficult behaviour
# when trying to organize the windows in your GUI.
#
# To solve the above problems, this code creates a Frame for your GUI window
# and splits that into multiple subframes organized as a grid, into "numrows"
# rows and "numcols" columns. You can set numrows and numcols below to have
# as many rows and columns as you want, thus getting numrows*numcols cells. 
# After creating the cells, the width of each column and the height of each
# row is fixed in the code so that the grid layout doesn't make things 
# reduce in size.
#
# Once all this is done, you can place any of your widgets in any of the cells,
# as shown with the Label example widget at the end of this code. You can also
# make your widget span multiple cells. Altogether 4 examples are shown at the
# end of this code.
#
# So, feel free to use this code as the base version of your GUI and then
# add to it your own Buttons, Labels, Frames, etc etc.
#
#-------------------- start of GUI code: ----------------------------------
#
#
# mandatory GUI preamble code:
import tkinter
from tkinter.constants import *
## create the root GUI window
rootFrame = tkinter.Tk()

# now create the overall GUI window:
# set it to a fixed size irrespective of its contents; otherwise, 
# tknter/TclTk shrink this window to the size of its contents 
# (by my preference, that is not a very desirable default behavior)
GUIwidth  = 1024 # change this to suit your monitor size
GUIheight = 600  # change this to suit your monitor size

# fix number of rows and columns for GUIwindow
numrows = 8
numcols = 8

# create the GUI window now:
GUIwindow = tkinter.Frame(rootFrame, width=GUIwidth, height=GUIheight)
# set the title of your app window:
GUIwindow.master.title("GUI Grid")  
##  register the window with the geometry manager, so that is displayed
## in the GUI, else it will not be displayed:
GUIwindow.grid(padx=1, pady=1)
# to fix the window's size, the following is also needed:
GUIwindow.grid_propagate(0) 


# now create a 2-D array of (numrows*numcols) Frames as a nested list:
cellFrame = [[[] for j in range(0,numcols)] for i in range(0,numrows)]

for i in range(0,numrows):
  for j in range(0,numcols):
    # create a cell Frame, make its parent the GUI window:
    cellFrame[i][j] = tkinter.Frame(GUIwindow, borderwidth=2, relief=RIDGE,
                                        width=GUIwidth//numcols, 
                                        height=GUIheight//numrows)
    # make the cell frames appear in their respective positions in the
    # GUI grid:
    cellFrame[i][j].grid(in_=GUIwindow, row=i, column=j, padx=1, pady=1)
    # fix the size of the cell Frame:
    cellFrame[i][j].grid_propagate(0)


# now the GUI has all its row and column Frames;
# fix the row and column widths of the GUI window itself now:
for i in range(0,numrows):
  GUIwindow.grid_rowconfigure(i, weight=1, minsize=GUIheight//numrows)
for j in range(0,numcols):
  GUIwindow.grid_columnconfigure(j, weight=1, minsize=GUIwidth//numcols)

# status message printout:
print(GUIwindow.grid_size())

#-----------------------------------------------------------------------
# now you can add whatever Widget you want to whichever cell frame
#-----------------------------------------------------------------------
# example 1: here we add a label to one cell 
#-----------------------------------------------------------------------

## first create a generic text holder
defaultText = tkinter.StringVar()
defaultText.set("label in a \n cell frame")

# now create the label as a member of cell[1][1]
defaultlabel = tkinter.Label(cellFrame[1][1],
                             relief=RIDGE, borderwidth=4, text="default") 
# set the label's text:
defaultlabel['textvariable'] = defaultText
# make the label appear in its cell Frame:
defaultlabel.grid(in_=cellFrame[1][1])
                  
# fix the label's size:
defaultlabel.grid_propagate(0)



#-----------------------------------------------------------------------
# example 2: here we add a label to the GUIwindow itself
#-----------------------------------------------------------------------

## first create a generic text holder
defaultText = tkinter.StringVar()
defaultText.set("label in \n GUIwindow cell")

# now create the label as a member of GUIwindow
defaultlabel = tkinter.Label(GUIwindow, relief=RIDGE, borderwidth=4, 
                             text="default") 
# set the label's text:
defaultlabel['textvariable'] = defaultText
# make the label appear in its cell Frame:
defaultlabel.grid(in_=GUIwindow, row=3, column=3, 
                  sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W)
# fix the label's size:
defaultlabel.grid_propagate(0)



#-----------------------------------------------------------------------
# example 3: here we add a label that spans multiple cells of the GUIwindow
#-----------------------------------------------------------------------

## first create a generic text holder
defaultText = tkinter.StringVar()
defaultText.set("label spanning multiple GUIwindow cells")

# now create the label as a member of GUIwindow
defaultlabel = tkinter.Label(GUIwindow, relief=RIDGE, borderwidth=4, 
                             text="default") 
# set the label's text:
defaultlabel['textvariable'] = defaultText
# make the label appear in its cell Frame:
defaultlabel.grid(in_=GUIwindow, row=numrows-4, column=numcols-4, columnspan=3, rowspan=2,
                  sticky=tkinter.N+tkinter.E+tkinter.S+tkinter.W)
# fix the label's size:
defaultlabel.grid_propagate(0)



#-----------------------------------------------------------------------
# example 4: here we add two labels to one cell 
#-----------------------------------------------------------------------

## first create a generic text holder
defaultText = tkinter.StringVar()
defaultText.set("label in a \n cell frame")

# now create the label as a member of cell[numrows-1][numcols-1]
defaultlabel1 = tkinter.Label(cellFrame[numrows-1][numcols-1],
                             relief=RIDGE, borderwidth=4, text="label1") 
defaultlabel2 = tkinter.Label(cellFrame[numrows-1][numcols-1],
                             relief=RIDGE, borderwidth=4, text="label2") 

# make the labels appear in its cell Frame:
# NOTE that the grid layout manager now treats the row number and column
#      number as being within a grid inside the PARENT widget of the 
#      labels, i.e., within cellFrame[numrows-1][numcols-1] and NOT within
#      GUIwindow
#      So, the grid layout manager builds a grid within each widget that 
#      can hold other widgets; such widgets are typically Frames.
defaultlabel1.grid(in_=cellFrame[numrows-1][numcols-1], row=0, column=0)
defaultlabel2.grid(in_=cellFrame[numrows-1][numcols-1], row=1, column=2)
                  
# fix the label's size:
defaultlabel.grid_propagate(0)


#-----------------------------------------------------------------------
# now start the GUI main loop
tkinter.mainloop()
