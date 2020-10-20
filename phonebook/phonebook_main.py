# Python Version 3.7.2
# Author: Brian Brown
# Phonebook tutorial featuring OOP,
# Tkinter GUI and using Tkinter Parent/Child

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# my other modules
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define the master frame configuration
        self.master = master
        self.master.minsize(500, 300)  # height/width
        self.master.maxsize(500, 300)

        # Center window method will center the app on the users screen
        phonebook_func.center_window(self, 500, 300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is as tkinter built-in method to catch if
        # the user clicks the upper corner "X" in Windows
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        phonebook_gui.load_gui(self)


"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
