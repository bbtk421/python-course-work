from tkinter import *
import tkinter as tk
from tkinter import filedialog

class ParentWindow(Frame):
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

            self.btnCheck = tk.Button(self.master,text ="Check for files...", width=12, height=2)#, command=self.cancel)
            self.btnCheck.grid(row=11, column=1, padx=(20,25), pady=(4,4), sticky=SW)

            self.btnClose = tk.Button(self.master,text ="Close Program", width=12, height=2, command=quit)
            self.btnClose.grid(row=11, column=4, padx=(20,25), pady=(10,4), sticky=SE)
            

      def open_source(self):
           source = filedialog.askdirectory(initialdir="/", title="Select a file")
           self.textBox1.delete(0, END)
           self.textBox1.insert(0, source)
     
      def open_dest(self):
            dest = filedialog.askdirectory(initialdir="/", title="Select a file")   
            self.textBox2.delete(0, END)
            self.textBox2.insert(0, dest)
      
if __name__ =="__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()
      
      
