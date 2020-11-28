from tkinter import *

"""win = Tk() #part 4
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

b1.configure(text="Uno")

def butt1():
      print("Button one was pushed")

b1.configure(command=butt1)

win = Tk() #part 5
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

v.get()
'This is a test'

v.set("this is set by the program")"""

win = Tk() #part 6
lb = Listbox(win, height = 3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fouth entry")
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection()
