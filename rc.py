import tkinter
from tkinter import *
def aa():
    win.destroy()
    import accedi.py
win=Tk()
win.title("Satysfind chat-registrati")
win.rowconfigure(0, weight=2, minsize=800)
win.columnconfigure(0, weight=2, minsize=800)
f1=Frame(master=win, width=400, height=50)
l1=Label(master=f1, text="REGISTRAZIONE AVVENUTA CON SUCCESSO!")
f2=Frame(master=win, width=400, height=50)
b1=Button(master=f2, text="ACCEDI", fg="green", command=aa)

f1.pack()
l1.pack()
f2.pack()
b1.pack()
win.mainloop()
