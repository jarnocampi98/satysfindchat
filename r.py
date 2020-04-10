import os.path
import tkinter
from tkinter import *
from ftplib import FTP
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

def esci():
    win.destroy()
def reg():
    #print ("a")
    global nu
    global pa
    nu=""
    pa=""
    nu = tuno.get()
    pa = tdue.get()
    if (nu=="" or pa==""):
        l6.configure(text="Riempire i campi")
        l6.pack()
        return 0
    dir=os.getcwd()
    #print(dir)
    try:
        os.chdir(dir+"/u")
    except:
        ok=0
    try:
        print ("ok")
        if (os.path.exists(nu+".txt")):
            l6.configure(text="Questo nome utente è già in uso")
            l6.pack()
            return 0

        else:
            ftp.cwd("/sc/u")
            f=open(nu+".txt", 'w')
            f.write(pa)
            f.close()
            #print ("ciao")
            ftp.storbinary('STOR '+nu+'.txt', open(nu+'.txt', 'rb'))
            #os.remove(nome+'.txt')
            print ("UTENTE CREATO")
            """ftp.retrbinary('RETR log.txt', open('log.txt', 'wb').write)
            ff=open('log.txt', 'a')
            ff.write('1'+nome+'\n2'+eta+'\n3'+sex+'\n40\n50\n')
            ff.close()
            ftp.storbinary('STOR log.txt', open('log.txt', 'rb'))"""
            ftp.quit()
            #print ("funia")
            win.destroy()
            import accedi.py
    		#padre.destroy()
    		#import saty.py
    except:
        print("ERRORE CARTELLA\n")
        print (os.getcwd())
        return 0

win=Tk()
win.title("Satysfind chat-registrati")
win.rowconfigure(0, weight=2, minsize=800)
win.columnconfigure(0, weight=2, minsize=800)
f1=Frame(master=win, width=400, height=50)
l1=Label(master=f1, text="SATYSFIND CHAT")
l2=Label(master=f1, text="REGISTRATI")
#l2=tk.Label(win, text="ACCEDI").pack()
f2=Frame(master=win, width=200, height=25)
l3=Label(master=f2, text="Nome utente:")
tuno=Entry(master=f2, width=25)
l4=Label(master=f2, text="(ATTENZIONE! Il nome utente identificherà univocamente il tuo account)")
l5=Label(master=f2, text="Password:")
tdue=Entry(master=f2, width=25)
f3=Frame(master=win, width=200, height=25)
b1=Button(master=f3, text="REGISTRATI", command=reg)

f4=Frame(master=win, width=200, height=25)
l6=Label(master=f4, text="", fg="red")


f1.pack()
l1.pack()
l2.pack()
f2.pack()
l3.pack()
tuno.pack()
l4.pack()
l5.pack()
tdue.pack()
f3.pack()
b1.pack()
f4.pack()
l6.pack()
win.mainloop()
