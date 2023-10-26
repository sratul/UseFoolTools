#Import the required Libraries
from tkinter import *
from tkinter import ttk

import time
# import sys
# import os

import pyperclip

recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if tmp_value != recent_value:
        recent_value = tmp_value
        print("Value Copied: %s" % str(recent_value)[:40])
        
        #Create an instance of tkinter frame
        win = Tk()

        #Set the geometry of tkinter frame
        win.geometry("270x170")

        #Initialize a Label widget
        Label(win, text= "Value \n Copied",
        font=('Helvetica 40 bold')).pack(pady=20)

        #Automatically close the window after 3 seconds
        win.after(1500,lambda:win.destroy())

        win.mainloop()


    time.sleep(0.1)


