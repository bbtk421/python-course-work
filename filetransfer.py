import shutil
import os
import datetime
from tkinter import *
import tkinter as tk
from tkinter import filedialog

source = 'C:/Users/bbtk4/Documents/GitHub/python-course-work/file trasfer/A/'
dest = 'C:/Users/bbtk4/Documents/GitHub/python-course-work/file trasfer/B/'
files = os.listdir(source)

class ParentWindow(Frame): #brought all this over from the earlier assignment
      def __init__(self, master):
            Frame.__init__(self)

            self.master = master
            self.master.resizable(width = False, height = False)
            self.master.geometry('{}x{}'.format(450,175))
            self.master.title('Check files')
            self.master.config(bg='lightgrey')
            
            self.buttonBrowse1 = tk.Button(self.master, text = "Browse...", width=12, height=1, command = self.open_source)
            self.buttonBrowse1.grid(column = 1, row = 4, padx=(20,25), pady=(40,4))

            self.textBox1 = Entry(self.master, width=40)
            self.textBox1.grid(column = 2, row = 4, columnspan = 3, padx=(20,25), pady=(40,4))

            self.buttonBrowse2 = tk.Button(self.master, text = "Browse...", width=12, height=1, command = self.open_dest)
            self.buttonBrowse2.grid(column = 1, row = 5, padx=(20,25), pady=(10,4))
            
            self.textBox2 = Entry(self.master, width=40)
            self.textBox2.grid(column = 2, row = 5, columnspan = 3, padx=(20,25), pady=(10,4))

            self.btnCheck = tk.Button(self.master,text ="Check for files...", width=12, height=2, command=lambda:self.check_files)#should only run when pushing the button
            self.btnCheck.grid(row=11, column=1, padx=(20,25), pady=(4,4), sticky=SW)

            self.btnClose = tk.Button(self.master,text ="Close Program", width=12, height=2, command=quit)
            self.btnClose.grid(row=11, column=4, padx=(20,25), pady=(10,4), sticky=SE)
            

      def open_source(self): #should start you in the "file trasfer" directory
            source = filedialog.askdirectory(initialdir="/C:/Users/bbtk4/Documents/GitHub/python-course-work/file transfer/", title="Select a file")
            self.textBox1.delete(0, END)
            self.textBox1.insert(0, source)
     
      def open_dest(self): #should start you in the "file trasfer" directory
            dest = filedialog.askdirectory(initialdir="/C:/Users/bbtk4/Documents/GitHub/python-course-work/file transfer/", title="Select a file")   
            self.textBox2.delete(0, END)
            self.textBox2.insert(0, dest)

      def check_files(self): #should run when clicking the Check for files... button
            for i in files:
                  modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(source+i))
                  todaysDate = datetime.datetime.today()
                  modifyDateLimit = modifyDate + datetime.timedelta(days=1)
            if modifyDateLimit > todaysDate:                                             
                  shutil.copy(source+i, dest)


if __name__ =="__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()
