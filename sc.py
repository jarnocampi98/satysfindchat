import tkinter as tk
import os
def accedi():
    win.destroy()
    import accedi.py
def registrati():
    win.destroy()
    import r.py
def esci():
    win.destroy()
def u():
    dir=os.getcwd()
    try:
        os.mkdir(dir+'/u')
    except:
        print ("")
win=tk.Tk()
win.title("Satysfind chat")
win.rowconfigure(0, weight=2, minsize=800)
win.columnconfigure(0, weight=2, minsize=800)
f1=tk.Frame(master=win, width=400, height=50).pack()
l1=tk.Label(master=f1, text="SATYSFIND CHAT").pack()
#l2=tk.Label(win, text="ACCEDI").pack()
b1=tk.Button(master=f1, text="ACCEDI",fg="green", command=accedi).pack()
b2=tk.Button(master=f1, text="REGISTRATI", bg="blue",fg="orange",command=registrati).pack()
b3=tk.Button(master=f1, text="ESCI",bg="blue",fg="red", command=esci).pack()
win.mainloop()
