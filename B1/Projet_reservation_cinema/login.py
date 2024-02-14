from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox
from tistique import *
from choisir_placeBA12 import *
from choisir_placeBA20 import *
from choisir_placeTG12 import *
from choisir_placeTG20 import *


import matplotlib as plt
from matplotlib import pyplot




def login():

    
    #permet de faire pop les camemberts
    def statistique():

        #pie1 all class
        print("ok")
        pyplot.figure(figsize = (4, 4))
        x = [Aero1,Aero2,Aero3,Aero4,Aero5,bachelor1,bachelor2,bachelor3]
        pyplot.pie(x, labels = ['Aero1', 'Aero2', 'Aero3', 'Aero4', 'Aero5','B1',"B2","B3"], normalize = True,autopct='%1.1f%%')
        pyplot.show()
        colors = ['blue','red', 'yellow','green','orange','pink','purple','magenta']
        
        #pie2 bachelor/aero
        pyplot.figure(figsize = (4, 4))
        x = [aero,bachelor]
        pyplot.pie(x, labels = [ 'Aero' ,'Bachelor'], normalize = True,autopct='%1.1f%%')
        pyplot.show()
        colors = ['red','yellow']

    def Inscription_code() :

        #get login password and Promo
        global login
        login = Logininscription.get()
        password = mdplogin.get()
        Classe = Promo.get()

        #verif si qq chose inscrit sinon retest
        if login == "" or password == "" or Classe == "":
            messagebox.showerror("Erreur", "Veuillez remplir tout les champs ")
            print(login)
        


            #On passe maintenant a la verif de l'id et du mdp
        else :
            #ouverture du dossier
            File_inscription_name = os.listdir()
            #check file in dossier
            if str(login) + ".csv" in File_inscription_name : 
                print("Erreur 3 : Le nom d'utilisateur est déjà pris")

                messagebox.showwarning("Info", "Le nom d'utilisateur est déjà pris")
            else :

                #fichier de check de login
                File = open(str(login)+".csv", "w")
                File.write(str(password))
                File.close()
                messagebox.showinfo("Info", "Vous avez creer votre compte ")
                print("Message 2 : Votre comte a été crée avec succès !")

                #file pour db totale avec pie
                File3  = open("Database.csv", "a")
                File3.write(str(Classe)+";"+str(login)+";"+ str(password)+";"+"\n")
                File3.close()
            

    #def login verif connection 
    def Login_code() :
        #get data from window

        id_Login = Nomlogin_entry.get()
        mdp_Login = Passlogin_entry.get()


        #verif si qq chose inscrit sinon retest
        if mdp_Login =="" or id_Login == "":
            messagebox.showerror("Erreur", "Veuillez remplir tout les champs ")

        
        global connecte
        if connecte == 1: #check si deja co
            messagebox.showerror("Erreur", "vous etes deja connec")

        #On passe maintenant a la verif de l'id et du mdp
        else:
            #ouverture et def de quel fichier il faut verif 
            File_login_name = os.listdir()

            #check si le fichier exite 
            if str(id_Login) + ".csv" in File_login_name :
                #on ouvre le fichier coreespondant a l'id
                File1 = open(str(id_Login)+".csv", "r")
                liste_info_login = File1.read().split(":")
                File1.close()
                

                #on check si le mdp correspond dans le fichier du nom
                if mdp_Login == liste_info_login[0] :
                    print("Vous etes bien connecté.e")
                    messagebox.showinfo("Info", "Vous etes bien connecté.e ")
                    
                    connecte = 1
                    fenetre.destroy()
    
           #si mdp incorrect
                else :
                    print("Erreur : mdp incorrect ")
                    messagebox.showerror("Info", "Erreur : mdp incorrect ")

                    #si pas id
            else :
                print("Il n'existe pas d'identifiant a ce nom")
                messagebox.showerror("Info", "Identifiant incorrect")
                
        

    #fenetre  Creation account

    def inscription():
        Create = Tk()
        Create.iconbitmap(r'icone.ico')

        def findevie2():
            Create.destroy()

        SL0 = Label(Create, text = "Veuillez remplir") #SL = Sous label
        SL0.grid(row=0,column=0)
        SL01 = Label(Create, text = "  les champs si dessous ") 
        SL01.grid(row=0,column=1)
        SL02 = Label(Create, text = "  afin de creer votre compte ") 
        SL02.grid(row=0,column=2)


        SL3 = Label(Create, text = "Nom") 
        SL3.grid(row=1,column=0)


        global Logininscription
        Logininscription = Entry(Create)
        Logininscription.grid(row = 1 ,column= 1)

        
        
        SL5 = Label(Create, text = "Mots de passe") 
        SL5.grid(row=3,column=0)
        
        
        
        global mdplogin
        mdplogin = Entry(Create)
        mdplogin.grid(row = 3,column= 1)

        SL6 = Label(Create, text = "Promo") 
        SL6.grid(row=4,column=0)

        global Promo
        Promo =ttk.Combobox(Create, values=["B1","B2","B3","A1","A2","A3","A4","A5",])
        Promo.grid(row=4,column=1)

        '''SL6 = Label(Create, text = "Comfirmez mdp") 
        SL6.grid(row=5,column=0)
        Se6 = Entry(Create) 
        Se6.grid(row = 5 ,column= 1)'''

        
        Sb2 = Button(Create, text = 'Creer compte', command= Inscription_code) #lambda permet d'appeler 2 fct en mm tps
        Sb2.grid(row = 6 ,column= 1)

        Sb2 = Button(Create, text = 'Stats', command= statistique) #lambda permet d'appeler 2 fct en mm tps
        Sb2.grid(row = 6 ,column= 0)

        Sb2 = Button(Create, text = 'Annuler', command= findevie2) #lambda permet d'appeler 2 fct en mm tps
        Sb2.grid(row = 6 ,column= 2)
        

        Create.mainloop()

    
    #fenetre principale
    fenetre = Tk()
    fenetre.iconbitmap(r'icone.ico')

    def findevie():
        fenetre.destroy()
    #Création du bouton Login :

    L4 = Label(fenetre, text = " Connexion ") 
    L4.grid(row=0,column=1)

    Nom_LoginLabel = Label(fenetre, text = "Nom") 
    Nom_LoginLabel.grid(row=2,column=0)

    global Nomlogin_entry
    Nomlogin_entry= Entry(fenetre)
    Nomlogin_entry.grid(row = 2,column= 1)

    Pass_Login = Label(fenetre, text = "Mots de passe") 
    Pass_Login.grid(row=3,column=0)

    global Passlogin_entry
    Passlogin_entry = Entry(fenetre)
    Passlogin_entry.grid(row = 3 ,column= 1)

    b1 = Button(fenetre, text = 'Annuler', command= findevie) #cancel
    b1.grid (row = 5, column= 0)


    Login_bouton = Button(fenetre,text="Login",command=Login_code)
    Login_bouton.grid(row=5,column=2)

    #Création du bouton Inscription :
    Inscription_bouton = Button(fenetre,text="Inscription",command=inscription)
    Inscription_bouton.grid(row=5,column=1)

    fenetre.title("Cine'psa")

    fenetre.mainloop()



def reserver_blackadam():
    if connecte == 1:
        
        reserver1 = Tk()
        reserver1.title('Reserver ma place')
        reserver1.iconbitmap(r'icone.ico')

        l1=Label(reserver1,text="25/12/2022")
        l1.grid(row=0,column=1)

        l2=Label(reserver1,text="20H00")
        l2.grid(row=1,column=1)

        l3=Label(reserver1,text="Black Adam")
        l3.grid(row=3,column=0)

        l4=Label(reserver1,text="Ciné-psa")
        l4.grid(row=4,column=0)

        l5=Label(reserver1,text="Salle 001")
        l5.grid(row=4,column=3)

        b1=Button(reserver1,text="Reserver ma place",command=choisir1)
        b1.grid(row=6,column=1)

        reserver1.mainloop


        F=open("Seance.csv","a")
        F.write("B1"+"\n") #blackadam 20h

        F.close()
    else :
        messagebox.showinfo("Erreur","Vous n'etes pas connecte")

        

def reserver_blackadam_12():
    if connecte == 1:
        reserver1 = Tk()
        reserver1.title('Reserver ma place')
        reserver1.iconbitmap(r'icone.ico')

        l1=Label(reserver1,text="25/12/2022")
        l1.grid(row=0,column=1)

        l2=Label(reserver1,text="12H00")
        l2.grid(row=1,column=1)

        l3=Label(reserver1,text="Black Adam")
        l3.grid(row=3,column=0)

        l4=Label(reserver1,text="Ciné-psa")
        l4.grid(row=4,column=0)

        l5=Label(reserver1,text="Salle 001")
        l5.grid(row=4,column=3)

        b1=Button(reserver1,text="Reserver ma place",command=choisir2)
        b1.grid(row=6,column=1)

        reserver1.mainloop

        F=open("Seance.csv","a")
        F.write("B0"+"\n") #blackadam 12h

        F.close()
    
    else :
        messagebox.showinfo("Erreur","Vous n'etes pas connecte")

def reserver_topgun():
    if connecte == 1:
        reserver1 = Tk()
        reserver1.title('Reserver ma place')
        reserver1.iconbitmap(r'icone.ico')

        l1=Label(reserver1,text="25/12/2022")
        l1.grid(row=0,column=1)

        l2=Label(reserver1,text="20H00")
        l2.grid(row=1,column=1)

        l3=Label(reserver1,text="Top Gun")
        l3.grid(row=3,column=0)

        l4=Label(reserver1,text="Ciné-psa")
        l4.grid(row=4,column=0)

        l5=Label(reserver1,text="Salle 002")
        l5.grid(row=4,column=3)

        b1=Button(reserver1,text="Reserver ma place",command=choisir3)
        b1.grid(row=6,column=1)

        reserver1.mainloop

        F=open("Seance.csv","a")
        F.write("T2"+"\n") #topgun 20h

        F.close()
    else :
        messagebox.showinfo("Erreur","Vous n'etes pas connecte")


def reserver_topgun_12():
    if connecte == 1:
        reserver1 = Tk()
        reserver1.title('Reserver ma place')
        reserver1.iconbitmap(r'icone.ico')

        l1=Label(reserver1,text="25/12/2022")
        l1.grid(row=0,column=1)

        l2=Label(reserver1,text="12H00")
        l2.grid(row=1,column=1)

        l3=Label(reserver1,text="Top Gun")
        l3.grid(row=3,column=0)

        l4=Label(reserver1,text="Ciné-psa")
        l4.grid(row=4,column=0)

        l5=Label(reserver1,text="Salle 002")
        l5.grid(row=4,column=3)

        b1=Button(reserver1,text="Reserver ma place",command=choisir4)
        b1.grid(row=6,column=1)

        reserver1.mainloop

        F=open("Seance.csv","a")
        F.write("T3"+"\n") #topgun 12h

        F.close()
    else :
        messagebox.showinfo("Erreur","Vous n'etes pas connecte")

        
global connecte
connecte = 0


