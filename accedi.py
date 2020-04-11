import os.path
import tkinter
from tkinter import *
from ftplib import FTP
import time
import hashlib
server='ftp.satysfind.altervista.org'
user='satysfind'
passwd='Satysfind18'

try:
	ftp=FTP(server)
	ftp.login(user, passwd)
	print ('COLLEGAMENTO RIUSCITO\nPIENO CONTROLLO DEL SERVER\n')
	#ftp.retrlines('LIST')
    #ftp.cwd('/sc')

except:
        print ('Errore nel contattare il server\nControlla di essere connesso ad internet')
        time.sleep(3)
        exit()

def acc():
    #print ("a")
    try:
    	ftp=FTP(server)
    	ftp.login(user, passwd)
    	print ('COLLEGAMENTO RISTABILITO\nPIENO CONTROLLO DEL SERVER\n')
    	#ftp.retrlines('LIST')
        #ftp.cwd('/sc')

    except:
            print ("SERVER GIA' COLLEGATO")
    global nu
    global pa
    nu=""
    pa=""
    nu = tuno.get()
    pa = tdue.get()
    pa=str(pa)
    pah = hashlib.md5(pa.encode())
    pah=pah.hexdigest()
    pah=str(pah)
    ftp.cwd("/sc/u")
    if (nu=="" or pa==""):
        l6.configure(text="Riempire i campi")
        l6.pack()
        return 0
    #print(dir)
    try:
        #print ("ok")
        dirr=os.getcwd()
        os.chdir(dirr+"/u")
        print ("OK, siamo nella cartella: "+os.getcwd())
    except:
        print("Errore nel trovare la cartella utenti u in locale")
        print ("!!!!!siamo nella cartella: "+os.getcwd())

    try:
        ftp.cwd("/sc/u/"+nu)
    except:
        l6.configure(text="Impossibile trovare l'utente: "+nu+ " (DIRECTORY ERROR)")
        l6.pack()
        return 0
    try:
        ftp.retrbinary('RETR '+nu+'.txt', open(nu+'.txt', 'wb').write)
        f=open(nu+".txt", 'r')
        #f.seek(0)
        passg=f.readline()
        f.close()
        if (passg==pah):
            print ("Password corretta\n")
            print("Elimino il file di log in locale")
            os.remove(nu+'.txt')
            l7.configure(text="PASSWORD CORRETTA...COLLEGAMENTO AL SERVER")
            l7.pack()
            win.destroy()
            fff=open("log.txt", 'w')
            fff.write(nu)
            fff.close()
            import main.py
        else:
            print ("Password errata")
            os.remove(nu+'.txt')
            l6.configure(text="PASSWORD ERRATA!")
            l6.pack()
            return 0

    except:
        print("Errore nel trovare l'utente sul server")
        l6.configure(text="Impossibile trovare l'utente: "+nu+ " (FILE ERROR)")
        l6.pack()
win=Tk()
win.title("Satysfind chat-accedi")
win.rowconfigure(0, weight=2, minsize=800)
win.columnconfigure(0, weight=2, minsize=800)
f1=Frame(master=win, width=400, height=50)
l1=Label(master=f1, text="SATYSFIND CHAT")
l2=Label(master=f1, text="ACCEDI")
f2=Frame(master=win, width=200, height=25)
l3=Label(master=f2, text="Nome utente:")
tuno=Entry(master=f2, width=25)
l4=Label(master=f2, text="Password:")
tdue=Entry(master=f2, width=25)
f3=Frame(master=win, width=200, height=25)
b1=Button(master=f3, text="ACCEDI", command=acc)
f4=Frame(master=win, width=200, height=25)
l6=Label(master=f4, text="", fg="red")
l7=Label(master=f4, text="", fg="green")


f1.pack()
l1.pack()
l2.pack()
f2.pack()
l3.pack()
tuno.pack()
l4.pack()
tdue.pack()
f3.pack()
b1.pack()
f4.pack()
l6.pack()
l7.pack()
win.mainloop()
