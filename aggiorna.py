import os.path
import tkinter
from tkinter import *
from ftplib import FTP
import time
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

ftp.cwd("/e")

try:
    dir=os.getcwd()
    print(dir)
    try:
        ftp.retrbinary('RETR r.py', open('r.py', 'wb').write)
    except:
        print ("ERRORE r.py")
    try:
        ftp.storbinary('STOR '+'accedi.py', file)
    except:
        print ("ERRORE accedi.py")
    try:
        ftp.storbinary('STOR '+'main.py', file)
    except:
        print ("ERRORE main.py")
    try:
        ftp.storbinary('STOR '+'sc.py', file)
    except:
        print ("ERRORE sc.py")
    try:
        ftp.storbinary('STOR '+'rc.py', file)
    except:
        print ("ERRORE rc.p")
    file.close()
except:
    print ("Errore")
