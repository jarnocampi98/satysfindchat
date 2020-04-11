import os.path
import tkinter
from tkinter import *
from ftplib import FTP
import time
server='ftp.satysfind.altervista.org'
user='satysfind'
passwd='Satysfind18'
def col():
	try:
		global ftp
		ftp=FTP(server)
		ftp.login(user, passwd)
		print ('COLLEGAMENTO RIUSCITO\nPIENO CONTROLLO DEL SERVER\n')
		#ftp.retrlines('LIST')
		#ftp.cwd('/sc')
	except:
		print ('Errore nel contattare il server\nControlla di essere connesso ad internet')
		time.sleep(3)
		exit()
#col()
def on_closing():
	os.remove("log.txt")
	win.destroy()
def agg():
	col()
	try:
		dirr=os.getcwd()
		print (dirr)
		try:
			print(os.getcwd())
			fff=open("log.txt", 'r')
			logg=fff.readline()
			fff.close()
		except:
			print ("Impossibile trovare log.txt")
		print ("ok")
		print(logg)
		print(ftp.pwd())
		ftp.cwd("/sc/u/"+logg+"/messaggi_r")
		print ("OK")
		l=ftp.nlst()
		tuno.delete(1.0, END)
		lenn=len(l)
		for i in range(lenn):
			tuno.insert(END, '\n'+str(i+1)+") "+l[i])
		tuno.pack()
		ftp.close()
	except:
		print("ERROR")
		ftp.close()
		return 0

def leg():
	col()
	try:
		dirr=os.getcwd()
		print (dirr)
		try:
			print(os.getcwd())
			fff=open("log.txt", 'r')
			logg=fff.readline()
			fff.close()
		except:
			print ("Impossibile trovare log.txt")
		print ("ok")
		ftp.cwd("/sc/u/"+logg+"/messaggi_r")
		l=ftp.nlst()
        #tuno.delete(1.0, END)
		lenn=len(l)
		ii=tdue.get()
		ii=int(ii)-1
		if (((ii)>=lenn) or (ii+1)==0):
			print ("ERROR - file sovrastimato")
			l4.configure(text="NUMERO TROPPO GRANDE O UGUALE A ZERO")
			l4.pack()
			l5.configure(text="")
			l5.pack()
			ttre.delete(1.0, END)
			ttre.pack()
			return 0
		try:
			file=l[ii]
			ftp.retrbinary('RETR '+l[ii], open(l[ii], 'wb').write)
			filel=open(l[ii], "r")
			testo=filel.readlines()
			filel.close()
			print(testo)
			ttre.delete(1.0, END)
			lentesto=len(testo)
			for cont in range (lentesto):
				ttre.insert(END, testo[cont])
			#ttre.insert(END, testo)
			ttre.pack()
			os.remove(l[ii])
			l4.configure(text="")
			l4.pack()
			l5.configure(text="ECCO IL MESSAGGIO: "+l[ii])
			l5.pack()
			ftp.close()
		except:
			print ("Errore nel trovare il file o nel leggerlo")
			l4.configure(text="File non trovato")
			l4.pack()
			l5.configure(text="")
			l5.pack()
			ttre.delete(1.0, END)
			ttre.pack()
			ftp.close()
			return 0
	except:
		print("ERROR")
		l4.configure(text="ERRORE - INSERISCI UN NUMERO E NON UN CARATTERE")
		l4.pack()
		l5.configure(text="")
		l5.pack()
		ttre.delete(1.0, END)
		ttre.pack()
		ftp.close()
		return 0

def sen():
	col()
	print ("Funzia sen")
	des=tquattro.get()
	ogg=tcinque.get()
	if(des=="" and ogg==""):
		l9.configure(text="RIEMPIRE I CAMPI")
		l9.pack()
		l10.configure(text="")
		l10.pack()
		ftp.close()
	else:
		try:
			ftp.cwd("/sc/u/"+des)
			try:
				print (des)
				print (ogg)
				ftp.cwd("/sc/u/"+des+"/messaggi_r")
				print ("OK, siamo nella caretlla dele destinatario")
				testoo=ttre.get('1.0', END)
				print (testoo)
				ogg=ogg+"_ da "+loggg+" _.txt"
				save=open(ogg, "w")
				save.write(testoo)
				save.close()
				print(ogg)
				ftp.storbinary('STOR '+ogg, open(ogg, "rb"))
				os.remove(ogg)
				l10.configure(text="OK, MESSAGGIO INVIATO")
				l10.pack()
				l9.configure(text="")
				l9.pack()
				ftp.close()
			except:
				l9.configure(text="IMPOSSIBILE RECAPITARE IL MESSAGGIO AL DESTINATARIO")
				l9.pack()
				l10.configure(text="")
				l10.pack()
				ftp.close()
				return 0

		except:
			l9.configure(text="NOME UTENTE DEL DESTINATARIO NON TROVATO")
			l9.pack()
			l10.configure(text="")
			l10.pack()
			ftp.close()
			return 0
win=Tk()
win.geometry('800x800')
win.title("Satysfind chat")
win.rowconfigure(0, weight=2, minsize=800)
win.columnconfigure(0, weight=2, minsize=800)
f1=Frame(master=win, width=400, height=50)
l1=Label(master=f1, text="SATYSFIND CHAT")
try:
	#print(os.getcwd())
	ffff=open("log.txt", 'r')
	global loggg
	loggg=ffff.readline()
	ffff.close()
except:
	print ("Impossibile trovare log.txt per utente")
l01=Label(master=f1, text="Login come: "+loggg, fg="green")
l2=Label(master=f1, text="MESSAGGI")
#l2=tk.Label(win, text="ACCEDI").pack()
f2=Frame(master=win, width=200, height=25)
#l3=Label(master=f2, text="Nome utente:")
tuno= Text(master=f2,width=100,height=10)
tuno.insert('1.0', '')
#l4=Label(master=f2, text="(ATTENZIONE! Il nome utente identificherà univocamente il tuo account)")
#l5=Label(master=f2, text="Password:")
#tdue=Entry(master=f2, width=25)
f3=Frame(master=win, width=200, height=25)
b1=Button(master=f3, text="AGGIORNA", command=agg)
f4=Frame(master=win, width=200, height=25)
l3=Label(master=f4, text="Indica il numero del messaggio che desideri leggere:")
tdue=Entry(master=f4, width=5)
l4=Label(master=f4, text="", fg="red")
l5=Label(master=f4, text="", fg="green")
b2 = Button(master=f4, text="LEGGI", command=leg)
#f4=Frame(master=win, width=200, height=25)
#l6=Label(master=f4, text="", fg="red")
f5 = Frame(master=win, width=200, height=25)
ttre= Text(master=f5,width=100,height=10)
ttre.insert('1.0', '')

f6=Frame(master=win, width=20, height=25)
l6=Label(master=f5, text="(^testo qui sopra^)\nOPPURE INVIA UN UN MESSAGGIO", fg="green")
l7=Label(master=f5, text="Destinatario (nome utente):")
tquattro=Entry(master=f5, width=15)
l8=Label(master=f5, text="Oggetto:")
tcinque=Entry(master=f5, width=30)
b3=Button(master=f5, text="INVIA MESSAGGIO", command=sen)
l9=Label(master=f5, text="", fg="red")
l10=Label(master=f5, text="", fg="green")

agg()

f1.pack()
l1.pack()
l01.pack()
l2.pack()
f2.pack()
#l3.pack()
tuno.pack()
#l4.pack()
#l5.pack()
#tdue.pack()
f3.pack()
b1.pack()
#f4.pack()
#l6.pack()
f4.pack()
l3.pack()
tdue.pack()
b2.pack()
l4.pack()
l5.pack()
f5.pack()
ttre.pack()
l6.pack()
l7.pack()
tquattro.pack()
l8.pack()
tcinque.pack()
b3.pack()
l9.pack()
l10.pack()
win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()
