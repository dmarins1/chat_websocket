import tkinter as tk


root = tk.Tk() # create a Tk root window

w = 500 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/4)
y = (hs/2) - (h/5)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, 750, 100))

root.mainloop() # starts the mainloop