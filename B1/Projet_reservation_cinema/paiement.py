from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import ssl
import smtplib


def paiment():
    #________________________________________________
    #________________________________________________
    #________________________________________________
    def enregistrer():
        n=e1.get()
        m=cb1.get()
        a=cb2.get()
        c=e3.get()
        ma=e4.get()
        if n =="" or m == "" or a== "" or c == "" or ma== "" :      #verif si qq chose inscrit sinon retest
            messagebox.showerror("Erreur", "Veuillez remplir tout les champs ")
        else :

            F=open("paiement.csv","a")
            F.write(n+";"+m+";"+a+";"+c+";"+ma+"\n")

            F.close()
            
            #-------envoie de mail-------
    
    
            email_sender = '81anonyme81@gmail.com'
            email_password = 'tgrvamctwinpqqmj'
            email_receiver = ma
            subject = 'Votre réservation Ciné-psa'
    
            nom_fichier = 'BA12'+pl+'.png'

    
            em = MIMEMultipart()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.attach(MIMEText('Bonjour voici votre reservation :',"plain"))

            context = ssl.create_default_context()

            with open(nom_fichier, 'rb') as fp:
                img = MIMEImage(fp.read())
                img.add_header('Content-ID', '<{}>'.format(nom_fichier))
                em.attach(img)


            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver, em.as_string())
            
            print("votre place a bien ete enregistrer")
            print("vous allez recevoir un mail avec votre e-billet")

    #----------------------------------------
    fenetre1 = Tk()
    fenetre1.title("Paiement par carte bancaire")
    fenetre1.geometry("300x225")

    def findevie():
       fenetre1.destroy()

    l0=Label(fenetre1,text="Paiement 100% sécurisé")
    l0.grid(row=2,column=0)

    l1=Label(fenetre1,text="Numéro de carte")
    l1.grid(row=3,column=0)
    e1=Entry(fenetre1)
    e1.grid(row=4,column=0)

    l2=Label(fenetre1,text="Date d'expiration")
    l2.grid(row=5,column=0)
    mois=['01','02','03','04','05','06','07','08','09','10','11','12']
    cb1=ttk.Combobox(fenetre1,values=mois)#combobox
    cb1.grid(row=6,column=0)
    cb1.set('01') # option par defaut
    annees=['2022','2023','2024','2025','2026','2027','2028','2029','2030','2031','2032','2033']
    cb2=ttk.Combobox(fenetre1,values=annees)#combobox
    cb2.grid(row=6,column=1)
    cb2.set('2022') # option par defaut


    l3=Label(fenetre1,text="Cryptogramme")
    l3.grid(row=7,column=0)
    e3=Entry(fenetre1)
    e3.grid(row=8,column=0)

    l4=Label(fenetre1,text="Adresse Mail")
    l4.grid(row=0,column=0)
    e4=Entry(fenetre1)
    e4.grid(row=1,column=0)

    #----------------------------------------
    b1=Button(fenetre1,text="Annuler",command=findevie)
    b1.grid(row=9,column=0)

    b2=Button(fenetre1,text="Confirmer",command=enregistrer)
    b2.grid(row=9,column=1)

    #________________________________________________
    #________________________________________________
    #________________________________________________




