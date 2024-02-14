from tkinter import *
from tkinter import ttk
import matplotlib 
from matplotlib import pyplot
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


    #---------------------------------------------------
    #---------------------------------------------------
    #---------------------------------------------------

def info_1():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "1" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break
               

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A1"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A1"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 1
   
   

def info_2():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "2" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A2"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A2"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 2
   
   

def info_3():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "3" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A3"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A3"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 3

def info_4():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "4" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A4"+"\n")
      F.close()
      print("tortue")
      paiment()
      F=open("places.csv","a")
      F.write("A4"+"\n")
      F.close()
   csv_file.close()
   global pl
   pl = 4

def info_5():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "5" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A5"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A5"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 5

def info_6():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "6" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A6"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A6"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 6

def info_7():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "7" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A7"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A8"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 7

def info_8():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "8" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A8"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A8"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 8

def info_9():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "A":
               print("row 1 correct")
               if row[1] == "9" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("A9"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("A9"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 9

def info_10():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "0" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B0"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B0"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 10

def info_11():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "1" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B1"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B1"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 11

def info_12():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "2" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B2"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B2"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 12

def info_13():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "3" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B3"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B3"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 13

def info_14():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "4" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B4"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B4"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 14

def info_15():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "5" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B5"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B5"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 15

def info_16():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "6" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B6"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B6"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 16

def info_17():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "7" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B7"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B7"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 17

def info_18():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "8" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B8"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B8"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 18

def info_19():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "B":
               print("row 1 correct")
               if row[1] == "9" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("B9"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("B9"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 19

def info_20():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "0" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C0"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C0"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 20

def info_21():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "1" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C1"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C1"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 21

def info_22():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "2" :
                  print("placesBA12 deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C2"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C2"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 22

def info_23():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "3" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C3"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C3"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 23

def info_24():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "4" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C4"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C4"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 24

def info_25():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "5" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C5"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C5"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 25

def info_26():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "6" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C6"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C6"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 26

def info_27():
   a = 0
   csv_file = open("placesBA12.csv")
   for row in csv_file:
            if row[0] == "C":
               print("row 1 correct")
               if row[1] == "7" :
                  print("place deja reserve ")
                  a = 1
                  messagebox.showerror("Erreur", "Place deja réserveé")
                  break

   if a == 0:
      F=open("placesBA12.csv","a")
      F.write("C7"+"\n")
      F.close()
      F=open("places.csv","a")
      F.write("C7"+"\n")
      F.close()
      print("tortue")
      paiment()
   csv_file.close()
   global pl
   pl = 27
    
        
    #---------------------------------------------------
    #---------------------------------------------------
    #---------------------------------------------------

def stats():
    csv_file = open('places.csv')
    A1=0
    A2=0
    A3=0
    A4=0
    A5=0
    A6=0
    A7=0
    A8=0
    A9=0
    B0=0
    B1=0
    B2=0
    B3=0
    B4=0
    B5=0
    B6=0
    B7=0
    B8=0
    B9=0
    C0=0
    C1=0
    C2=0
    C3=0
    C4=0
    C5=0
    C6=0
    C7=0
    
    
    for row in csv_file: #nous permet de loop le nombre de fois le nombre de ligne du fichier ouvert

        if row[0]== "A" :           #on obtient la rang de la place 
            

            if row[1] == "1": #systeme de trie entre les places
                A1 = A1 + 1
                

            if row[1] == "2":
                A2 = A2 + 1
                

            if row[1] == "3":
                A3 = A3 + 1
                

            if row[1] == "4":
                A4 = A4 + 1
                
                
            if row[1] == "5":
                A5 = A5 + 1
                

            if row[1] == "6":
                A6 = A6 + 1
                

            if row[1] == "7":
                A7 = A7 + 1
                

            if row[1] == "8":
                A8 = A8 + 1
                

            if row[1] == "9":
                A9 = A9 + 1
                

        elif row[0]== "B" :   #on obtient le rang de la place
            

            if row[1] == "0": #systeme de trie entre les places
                B0 = B0 + 1
                

            if row[1] == "1":
                B1 = B1 + 1
                

            if row[1] == "2":
                B2 = B2 + 1
                

            if row[1] == "3":
                B3 = B3 + 1
                

            if row[1] == "4":
                B4 = B4 + 1
                
                
            if row[1] == "5":
                B5 = B5 + 1
                

            if row[1] == "6":
                B6 = B6 + 1
                

            if row[1] == "7":
                B7 = B7 + 1
                

            if row[1] == "8":
                B8 = B8 + 1
                

            if row[1] == "9":
                B9 = B9 + 1
                

                
        elif row[0]== "C" :
           
            if row[1] == "0": #systeme de trie entre les places
                C0 = C0 + 1
                

            if row[1] == "1":
                C1 = C1 + 1
                

            if row[1] == "2":
                C2 = C2 + 1
                

            if row[1] == "3":
                C3 = C3 + 1
                

            if row[1] == "4":
                C4 = C4 + 1
                
                
            if row[1] == "5":
                C5 = C5 + 1
               

            if row[1] == "6":
                C6 = C6 + 1
                

            if row[1] == "7":
                C7 = C7 + 1  

    csv_file.close()

    pyplot.figure(figsize = (4, 4))
    x = [A1,A2,A3,A4,A5,A6,A7,A8,A9,B0,B1,B2,B3,B4,B5,B6,B7,B8,B9,C0,C1,C2,C3,C4,C5,C6,C7]
    pyplot.pie(x, labels = ['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26','P27'], normalize = True,autopct='%1.1f%%')
    pyplot.show()


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
            pla=str(pl)
    
    
            email_sender = '81anonyme81@gmail.com'
            email_password = 'tgrvamctwinpqqmj'
            email_receiver = ma
            subject = 'Votre réservation Ciné-psa'
    
            nom_fichier = 'BA12'+pla+'.png'

    
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
    fenetre1.iconbitmap(r'icone.ico')

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






def choisir2 ():
   reserver2 = Tk()
   reserver2.title('Choisir ma place')
   reserver2.iconbitmap(r'icone.ico')
   #---------------------------------------------------
   l1=Label(reserver2,text="Selectionnez vos places")
   l1.grid(row=0,column=0)

   l2=Label(reserver2,text="Salle 1  -  27 places")
   l2.grid(row=1,column=0)

   #---------------------------------------------------

   def findevie():
      reserver2.destroy()
      

     
   b1=Button(reserver2,text="Annuler",width=15, height=1,command=findevie)
   b1.grid(row=5,column=0)

   '''b2=Button(reserver2,text="stats",width=15, height=1,command=stats)
   b2.grid(row=3,column=0)'''

   p1=Button(reserver2,text="P1",command=info_1,bg='yellow')
   p1.grid(row=2,column=1)

   p2=Button(reserver2,text="P2",command=info_2,bg='yellow')
   p2.grid(row=2,column=2)

   p3=Button(reserver2,text="P3",command=info_3,bg='yellow')
   p3.grid(row=2,column=3)

   p4=Button(reserver2,text="P4",command=info_4,bg='yellow')
   p4.grid(row=2,column=4)

   p5=Button(reserver2,text="P5",command=info_5,bg='yellow')
   p5.grid(row=2,column=5)

   p6=Button(reserver2,text="P6",command=info_6,bg='yellow')
   p6.grid(row=2,column=6)

   p7=Button(reserver2,text="P7",command=info_7,bg='yellow')
   p7.grid(row=2,column=7)

   p8=Button(reserver2,text="P8",command=info_8,bg='yellow')
   p8.grid(row=2,column=8)

   p9=Button(reserver2,text="P9",command=info_9,bg='yellow')
   p9.grid(row=2,column=9)

   p10=Button(reserver2,text="P10",command=info_10,bg='yellow')
   p10.grid(row=3,column=1)

   p11=Button(reserver2,text="P11",command=info_11,bg='yellow')
   p11.grid(row=3,column=2)

   p12=Button(reserver2,text="P12",command=info_12,bg='yellow')
   p12.grid(row=3,column=3)

   p13=Button(reserver2,text="P13",command=info_13,bg='yellow')
   p13.grid(row=3,column=4)
            
   p14=Button(reserver2,text="P14",command=info_14,bg='yellow')
   p14.grid(row=3,column=5)

   p15=Button(reserver2,text="P15",command=info_15,bg='yellow')
   p15.grid(row=3,column=6)

   p16=Button(reserver2,text="P16",command=info_16,bg='yellow')
   p16.grid(row=3,column=7)

   p17=Button(reserver2,text="P17",command=info_17,bg='yellow')
   p17.grid(row=3,column=8)

   p18=Button(reserver2,text="P18",command=info_18,bg='yellow')
   p18.grid(row=3,column=9)

   p19=Button(reserver2,text="P19",command=info_19,bg='yellow')
   p19.grid(row=4,column=1)

   p20=Button(reserver2,text="P20",command=info_20,bg='yellow')
   p20.grid(row=4,column=2)

   p21=Button(reserver2,text="P21",command=info_21,bg='yellow')
   p21.grid(row=4,column=3)

   p22=Button(reserver2,text="P22",command=info_22,bg='yellow')
   p22.grid(row=4,column=4)

   p23=Button(reserver2,text="P23",command=info_23,bg='yellow')
   p23.grid(row=4,column=5)

   p24=Button(reserver2,text="P24",command=info_24,bg='yellow')
   p24.grid(row=4,column=6)

   p25=Button(reserver2,text="P25",command=info_25,bg='yellow')
   p25.grid(row=4,column=7)

   p26=Button(reserver2,text="P26",command=info_26,bg='yellow')
   p26.grid(row=4,column=8)

   p27=Button(reserver2,text="P27",command=info_27,bg='yellow')
   p27.grid(row=4,column=9)

   reserver2.mainloop
