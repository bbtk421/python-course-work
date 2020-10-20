# Python Version 3.7.2
# Author: Brian Brown
# Student Tracker using Tkinter GUI and sqlite3

from tkinter import *
import tkinter as tk
from tkinter import messagebox

# my other modules
import tracker_gui
import tracker_func

# Frame is the Tkinter frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define the master frame configuration
        self.master = master
        self.master.minsize(500, 300)  # height/width
        self.master.maxsize(500, 300)

        # Center window method will center the app on the users screen
        tracker_func.center_window(self, 500, 300)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")

        # This protocol method is as tkinter built-in method to catch if
        # the user clicks the upper corner "X" in Windows
        self.master.protocol("WM_DELETE_WINDOW", lambda: tracker_func.ask_quit(self))
        arg = self.master

        # load in GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        tracker_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
