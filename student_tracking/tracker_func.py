# Python Version 3.7.2
# Author: Brian Brown
# Student Tracker using Tkinter GUI and sqlite3

import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

# my other modules
import tracker_gui
import tracker_main


def center_window(
    self, w, h
):  # pass in the tkinter frame(master) reference and the w + h
    # get users screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width / 2) - (w / 2))
    y = int((screen_height / 2) - (h / 2))
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the window upper right "X" to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # this closes app
        self.master.destroy()
        os._exit(0)


def create_db(self):
    conn = sqlite3.connect("tracker.db")
    with conn:
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE if not exists tbl_tracker( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_course TEXT \
            );"
        )
        # you must commit() to save and close the database connection
        conn.commit()
    conn.close()
    first_run(self)
