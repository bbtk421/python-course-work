import webbrowser
from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
      def __init__(self, master):
            Frame.__init__(self)

            self.master = master
            self.master.resizable(width = False, height = False)
            #self.master.resizable(width = True, height = True)
            self.master.geometry('{}x{}'.format(450,250))
            self.master.title('Web Page Generator')
            self.master.config(bg='lightgrey')

            self.textBox = Text(self.master, width=52, height=10)
            self.textBox.grid(column = 1, row = 2, rowspan = 6, padx=(10), pady=(10))

            self.btnClose = tk.Button(self.master,text ="Close Program", width=12, height=2, command=quit)
            self.btnClose.grid(column = 1, row=15, padx=(10,10), pady=(20,10), sticky=SE)

            self.btnSave = tk.Button(self.master,text ="Save", width=12, height=2, command=lambda:page_gen(self))
            self.btnSave.grid(column = 1, row=15, padx=(10,10), pady=(20,10), sticky=SW)

            

            def page_gen(self):
                  customText = self.textBox.get('1.0', END)
                  f = open("webpagegen.html", "w")
                  f.write("<html>\n<body>\n<p>" + customText + "</p>\n</body>\n</html>")
                  f.close()
                  webbrowser.open_new_tab("webpagegen.html")

if __name__ =="__main__":
      root = Tk()
      App = ParentWindow(root)
      root.mainloop()
