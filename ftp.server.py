from ftplib import FTP
import time
import os
#funzioni
def upload():
    #upload file
    nome=input('Nome file con estensione(0 per annullare):')
    if nome=='0':
        #exit()
        print ('\n\nAnnullamento....\n\n')
        time.sleep(1)
    else:
        try:
            file= open(nome, 'rb')
        except:
            print ('file non trovato')
            exit()
        ftp.storbinary('STOR '+nome, file)
        file.close()
    #ftp.quit()

def download():
    nome=input('Nome file da scaricare con estensione(0 per annullare):')
    if nome=='0':
        #exit()
        print ('\n\nAnnullamento....\n\n')
        time.sleep(1)
    else:
        try:
            ftp.retrbinary('RETR '+nome, open(nome, 'wb').write)
        except:
            print ('file non trovato sul server')
    #ftp.quit()

def comandi():
    print ("\n\n*************************************\n*************************************\n-0 per chiudere il programma\n-1 per upload\n-2 per download\n-3 per verificare i dati sul server\n-4 verificare i file nella directory locale\n-5 cambia directory di lavoro\n-6 visualizza directory di lavoro corrente\n*************************************\n*************************************\n\n")
#main
a=-1
aa=0
print( '*************************************\n*************************************')
print( '\tGestore di ftp.server\n*************************************\n*************************************\ninserire:\n-0 per annullare....\n-00 per offline\n-1 per collegarsi al server della lista spirit....\n-2 per collegarsi al server "satysfind"....\n')
server=input('server: ')
if server=='1':
    server='ftp.listaspirit16.altervista.org'
    user='listaspirit16'
    passwd='Spirit9moonlight'
elif server=='2':
    server='ftp.satysfind.altervista.org'
    user='satysfind'
    passwd='Satysfind18'
elif server=='0':
    print ("operazione annullata...")
    time.sleep(2)
    exit()
elif server=='00':
    aa=-1
else:
    user=input('user: ')
    passwd=input('password: ')

print ('\nCollegamento al server...')
print (server)
try:
	ftp=FTP(server)
	ftp.login(user, passwd)
	print ('COLLEGAMENTO RIUSCITO\nPIENO CONTROLLO DEL SERVER\n')
	#ftp.retrlines('LIST')
except:
        if aa==-1:
            print ('\n\nMODALITA* OFFLINE ATTIVATA CON SUCCESSO\n\n')
        else:
            print ('Errore nel contattare il server\nControlla di essere connesso ad internet')
            time.sleep(3)
            exit()

while a!=0:
    comandi()
    a=input(">>>")
    if a=='1':
        if aa==-1:
            print ('Impossibile in offline')
        else:
            upload()
    elif a=='0':
        if aa==-1:
            print ('\n\n\tCHIUSURA\n\n')
            a=0
        else:
            print ('\n\n\tCHIUSURA\n\n')
            ftp.quit()
            a=0
    elif a=='2':
        if aa==-1:
            print ('Impossibile in offline')
        else:
            download()
    elif a=='3':
        if aa==-1:
            print (Back.RED+'Impossibile in offline')
        else:
            ftp.retrlines('LIST')
    elif a=='4':
        print ('Files:\n')
        time.sleep(0.5)
        files=os.listdir('.')
        for file in files:
            print (file)
            time.sleep(0.1)
    elif a=='5':
        print ("Directory corrente:"+os.getcwd())
        dirr=input('\nCambia directory(0 per annullare):')
        try:
            os.chdir(dirr)
            print ('\n\nDirectory cambiata correttamente!\n Attuale directory corrente:'+os.getcwd()+'\n\n')
        except:
            print ('\n\nErrore nel cambiere directory\n\n')
    elif a=='6':
        print (os.getcwd())
