import tkinter as tk
import pandas as pd
from tkinter import messagebox
import os
import webbrowser
df = pd.read_json("yelp_academic_dataset_business.json", lines=True)





def login_windows():

    def back_main():
        login_window.destroy()  
    fenetre.destroy()


    global login_window
    login_window = tk.Tk()
    login_window.geometry("400x200") 

    Nom_LoginLabel = tk.Label(login_window, text="Nom d'utilisateur :", font=("Arial", 14), bg='#F0F0F0')
    Nom_LoginLabel.pack()
    
    global  Nomlogin_entry       
    Nomlogin_entry = tk.Entry(login_window, font=("Arial", 14))
    Nomlogin_entry.pack()

    Pass_Login = tk.Label(login_window, text="Mots de passe", font=("Arial", 14), bg='#F0F0F0')
    Pass_Login.pack()
    global Passlogin_entry
    Passlogin_entry = tk.Entry(login_window, font=("Arial", 14))
    Passlogin_entry.pack()

    b1 = tk.Button(login_window, text='Back', font=("Arial", 14), bg="#4CAF50", fg="white",
                command=lambda:[back_main(),def_fenetre()])
    b1.pack(side=tk.LEFT, padx=5, pady=5)

    Login_bouton = tk.Button(login_window,text="Login", font=("Arial", 14), bg="#4CAF50", fg="white",
                            command=Login_code)
    
    '''lambda:[back_main(),''' '''()])'''
    Login_bouton.pack(side=tk.RIGHT, padx=5, pady=5)

    Inscription_bouton = tk.Button(login_window,text="Inscription", font=("Arial", 14) , bg="#4CAF50", fg="white",
                                command=lambda:[back_main(),windows()])
    Inscription_bouton.pack(side=tk.RIGHT, padx=5, pady=5)
    
    login_window.title("Login")
    login_window.mainloop()

def Login_code() :
    
    print("good")
    print(type(Nomlogin_entry))
    id_Login = Nomlogin_entry.get()
    print("good2")
    print(id_Login)
    global name
    name = id_Login
    mdp_Login = Passlogin_entry.get()
    print(id_Login)
    print(mdp_Login)
    

    #verif si qq chose inscrit sinon retest
    if mdp_Login =="" or id_Login == "":
        messagebox.showerror("Erreur", "Veuillez remplir tout les champs ")
        messageboxcounter = 1


    global connecte
    if connecte == 1: #check si deja co
        messagebox.showerror("Erreur", "vous etes deja connecte")

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
                messagebox.showinfo("Info", "Vous etes bien connecté.e")
                connecte == 1
                login_window.destroy()
                def_fenetre2()
    

            else:
                print("Il n'existe pas d'identifiant a ce nom")
                messagebox.showerror("Info", "Identifiant incorrect")
            
        


        

def windows():
    def back_main():
        window_login.destroy()
    def ajouter_utilisateur():
        global identifiant
        
        identifiant = identifiant_entry.get()
        global nom_utilisateur
        nom_utilisateur = nom_utilisateur_entry.get()
        global mot_de_passe
        mot_de_passe = mot_de_passe_entry.get()
        global prenom
        prenom = prenom_entry.get()
        global nom_entry_login
        nom_entry_login = nom_entry.get()

        

        if identifiant == "" or nom_utilisateur == "" or mot_de_passe == "" or prenom_entry == ""or nom_entry_login == "":
                messagebox.showerror("Erreur", "Veuillez remplir tout les champs ")
                print(identifiant)
            
            #On passe maintenant a la verif de l'id et du mdp
        else :
            #ouverture du dossier
            File_inscription_name = os.listdir()
            if str(nom_utilisateur) + ".csv" in File_inscription_name : 
                print("Erreur 3 : Le nom d'utilisateur est déjà pris")

                messagebox.showwarning("Info", "Le nom d'utilisateur est déjà pris")
            else :

                #fichier de check de login
                File = open(str(nom_utilisateur)+".csv", "w")
                File.write(str(mot_de_passe))
                File.close()
                messagebox.showinfo("Info", "Vous avez creer votre compte ")
                print("Message 2 : Votre comte a été crée avec succès !")
                print(str(prenom))
                #file pour db totale avec pie
                File3 = open("Database.csv", "a")
                File3.write(str(mot_de_passe) + ";" + str(identifiant) + ";" + str(nom_utilisateur) + ";" + str(nom_entry_login) + ";" + str(prenom) + "\n")
                File3.close()
                identifiant_entry.delete(0, tk.END)
                nom_utilisateur_entry.delete(0, tk.END)
                mot_de_passe_entry.delete(0, tk.END)
                prenom_entry.delete(0, tk.END)
                nom_entry.delete(0, tk.END)

            

    global window_login
    window_login = tk.Tk()
    window_login.title("Ajouter un utilisateur")
    window_login.geometry("300x600")

    identifiant_label = tk.Label(window_login, text="ID :", font=("Arial", 14))
    identifiant_label.pack(pady=10)
    identifiant_entry = tk.Entry(window_login, font=("Arial", 14))  
    identifiant_entry.pack(pady=5)

    nom_utilisateur_label = tk.Label(window_login, text="Nom d'utilisateur :", font=("Arial", 14))
    nom_utilisateur_label.pack(pady=10)
    nom_utilisateur_entry = tk.Entry(window_login, font=("Arial", 14))
    nom_utilisateur_entry.pack(pady=5)

    mot_de_passe_label = tk.Label(window_login, text="Mot de passe :", font=("Arial", 14))
    mot_de_passe_label.pack(pady=10)
    mot_de_passe_entry = tk.Entry(window_login, show="*", font=("Arial", 14))
    mot_de_passe_entry.pack(pady=5)

    prenom_label = tk.Label(window_login, text="Prénom :", font=("Arial", 14))
    prenom_label.pack(pady=10)
    prenom_entry = tk.Entry(window_login, font=("Arial", 14))
    prenom_entry.pack(pady=5)

    nom_label = tk.Label(window_login, text="Nom :", font=("Arial", 14))
    nom_label.pack(pady=10)
    nom_entry = tk.Entry(window_login, font=("Arial", 14))
    nom_entry.pack(pady=5)

    bouton_ajouter = tk.Button(window_login, text="Add", font=("Arial", 14), bg="#4CAF50", fg="white", command=ajouter_utilisateur)
    bouton_ajouter.pack(pady=20)
    
    retour_button = tk.Button(window_login, text="back", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda:[back_main(),def_fenetre()])
    retour_button.pack(pady=20)

    message = tk.Label(window_login, font=("Arial", 14))
    message.pack()
    message.config(text="Utilisateur ajouté avec succès.", fg="green")
    window_login.mainloop()



def search_resto():
    def research():
        name_research_resto = nom_restaurant.get()
        resto_nom_results = []
        for index, row in df.iterrows():
            if row['name'].lower() == name_research_resto.lower():
                resto_nom_results.append(row)
        if len(resto_nom_results) == 0:
            messagebox.showerror("showwarning","Aucun restaurant trouvé avec ce nom.")
            print("Aucun restaurant trouvé avec ce nom.")
        else:
            root.destroy()
            result = tk.Tk()
            result.title("Search responce ***") 
            result.geometry("1920x1080")
            
            
            for resto in resto_nom_results:
                
                info_resto2 = f"Adresse : {resto['address']}, {resto['city']}, {resto['state']} {resto['postal_code']}"
                info_resto3 = f"Categorie : {resto['categories']}"
                info_resto4 = f"Note : {resto['stars']}"
                info_resto6 = f"Horaires : {resto['hours']}"

            def get_adress():
                id = resto['name']
                for i in range(0,len(df)):
                    if id == df['name'][i]: 
                        a = df['latitude'][i]
                        b = df['longitude'][i]  
                        
                        google_maps_link = f"https://www.google.com/maps/search/?api=1&query={a},{b}"
                        webbrowser.open(google_maps_link)
            

            label_nom_entree_restaurant = tk.Label(result, text="Search: " + name_research_resto, font=("Arial", 14), bg='#F0F0F0')
            label_nom_entree_restaurant.grid(row=0, column=1, pady=20)

            label_nbr_resto = tk.Label(result, text="Total Number: " + str(len(resto_nom_results)), font=("Arial", 14), bg='#F0F0F0')
            label_nbr_resto.grid(row=1, column=1, pady=10)

            label3 = tk.Label(result, text= info_resto2, font=("Arial", 12))
            label4 = tk.Label(result, text= info_resto3, font=("Arial", 12))
            label5 = tk.Label(result, text= info_resto4, font=("Arial", 12))
            label7 = tk.Label(result, text= info_resto6, font=("Arial", 12))
            label_recom = tk.Label(result, text="Recommandation : ",font=("Arial", 12))
            label_resultat = tk.Label(result, text="")
            label_maps = tk.Button(result, text= "Maps", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda:[get_adress()])
            

            label3.grid(row=2, column=0, pady=10, padx=10)
            label4.grid(row=3, column=0, pady=10, padx=10)
            label5.grid(row=5, column=1, pady=10, padx=10)
            label7.grid(row=4, column=0, pady=10, padx=10,columnspan=3)
            label_recom.grid(row=6, column=1, columnspan=2)
            label_resultat.grid(row=7, column=1, columnspan=2)
            label_maps.grid(row=6, column=0, columnspan=2)
            """Hellobis = "Hello"
            label12 = tk.Label(fenetre2, text=   Hellobis +"  "+name +"  "+ family, font=("Arial", 14), bg='#F0F0F0')
            label12.grid(row=15, column=0, columnspan=2)"""

            result.configure(bg="#FFFFFF")
            label3.configure(bg="#FFFFFF")
            label4.configure(bg="#FFFFFF")
            label5.configure(bg="#FFFFFF")
            label7.configure(bg="#FFFFFF")

            def afficher_resultat(result):
                result_str = "\n\n".join(result)
                label_resultat.config(text=result_str)

            entry_categori = resto['categories']

            df_restaurants = df[(df['categories'].str.contains('Restaurants')) & (df['categories'].str.contains(entry_categori))]
            df_restaurants_tries = df_restaurants.sort_values('stars', ascending=False).iloc[:3]
            if df_restaurants_tries.empty:
                afficher_resultat(["Aucun résultat trouvé pour cette catégorie.\n"])
            else:
                restaurant_strs = []
                for _, row in df_restaurants_tries.iterrows():
                    restaurant_str = f"Nom: {row['name']}\nAdresse: {row['address']}\nVille: {row['city']}\n\n"
                    restaurant_strs.append(restaurant_str)
                afficher_resultat(restaurant_strs)
            



    fenetre2.destroy()
    def afficher_nom_restaurant():
        nom = nom_restaurant.get() 
        label_resultat.config(text="Le nom du restaurant est : " + nom)

    def back_main():
        root.destroy()
        
    root = tk.Tk()
    root.title("Saisie du nom d'un restaurant")
    root.geometry("400x300") 
    root.configure(bg='#F0F0F0') 


    label_nom_restaurant = tk.Label(root, text="Nom du restaurant :", font=("Arial", 14), bg='#F0F0F0')
    label_nom_restaurant.pack(pady=10)

    nom_restaurant = tk.Entry(root, font=("Arial", 14))
    nom_restaurant.pack()


    bouton_afficher_nom_restaurant = tk.Button(root, text="Afficher", font=("Arial", 14), bg="#4CAF50", fg="white", command=lambda:[afficher_nom_restaurant(),research()])
    bouton_afficher_nom_restaurant.pack(pady=10)

    Back_Button = tk.Button(root,text="Back" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=lambda: [back_main(), def_fenetre2()])
    Back_Button.pack()

    label_resultat = tk.Label(root, font=("Arial", 14), bg='#F0F0F0')
    label_resultat.pack()

    Hellobis = "Hello"
    label = tk.Label(root, text=   Hellobis +"  "+name +"  "+ family, font=("Arial", 14), bg='#F0F0F0')
    label.pack()

    root.mainloop()
   

def tri_resto():
    fenetre2.destroy()
    global fenetre3
    fenetre3 = tk.Tk()
    fenetre3.title("find")
    fenetre3.geometry("400x300") 
    
    def back_main():
        fenetre3.destroy()


    def tri():
        window = tk.Tk()
        window.title("Recherche des restaurants")
        window.title("tri")
        window.geometry("400x200")

        def back_main_win():
            window.destroy()

        label_critere = tk.Label(window, text="Critère de comparaison :", font=("Arial", 14), bg='#F0F0F0')
        entry_critere = tk.Entry(window)
        label_operateur = tk.Label(window, text="Opérateur :", font=("Arial", 14), bg='#F0F0F0')
        entry_operateur = tk.Entry(window)
        label_valeur = tk.Label(window, text="Valeur :", font=("Arial", 14), bg='#F0F0F0')
        entry_valeur = tk.Entry(window)
        button_rechercher = tk.Button(window, text="Rechercher",font=("Arial", 14),bg="#4CAF50", fg="white")
        label_resultats = tk.Label(window, text="")

        def afficher_resultats(results):
            label_resultats.config(text=results)

        def effectuer_recherche():
            resultats = []
            insert = []
            attribut = entry_critere.get()
            operateur = entry_operateur.get()
            valeur = entry_valeur.get()
            for i in range(0,len(df)):
                if operateur == ">":
                    if float(df[attribut][i]) > float(valeur):
                        insert.append(df['business_id'][i])
                        resultats.append(df['name'][i])
                if operateur == "<":
                    if float(df[attribut][i]) < float(valeur):
                        insert.append(df['business_id'][i])
                        resultats.append(df['name'][i])
                elif operateur == "=": 
                    try :
                        if (df[attribut][i]) == float(valeur):
                            print('aaaa')
                            insert.append(df['business_id'][i])
                            resultats.append(df['name'][i])
                    except:
                        if (df[attribut][i]) == (valeur):
                            print('eeee')
                            insert.append(df['business_id'][i])
                            resultats.append(df['name'][i])

            df_meta = pd.DataFrame({'business_id': insert, 'name': resultats})
            df_meta = df_meta[['business_id', 'name']]
            if len(df_meta) == 0:
                afficher_resultats("Aucun résultat trouvé pour les critères donnés.\n")
            else:
                afficher_resultats(df_meta.to_string(index=False))

        button_rechercher.config(command=effectuer_recherche)

        label_critere.grid(row=0, column=0)
        entry_critere.grid(row=0, column=1)
        label_operateur.grid(row=1, column=0)
        entry_operateur.grid(row=1, column=1)
        label_valeur.grid(row=2, column=0)
        entry_valeur.grid(row=2, column=1)
        button_rechercher.grid(row=3, column=0, columnspan=2)
        label_resultats.grid(row=4, column=0, columnspan=2)

        Back_Button_win = tk.Button(window,text="Back" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=lambda: [back_main_win()])
        Back_Button_win.grid(row=3, column=1, columnspan=2)

        window.mainloop()
    


    def top_5_restaurants():
        window2 = tk.Tk()
        window2.title("Recherche par categories")
        window2.title("tri")
        window2.geometry("400x200")

        def back_main_win2():
            window2.destroy()

        label_categorie = tk.Label(window2, text="Enter une categorie :", font=("Arial", 14), bg='#F0F0F0')
        entry_categorie = tk.Entry(window2)
        button_rechercher = tk.Button(window2, text="Rechercher",font=("Arial", 14),bg="#4CAF50", fg="white")
        label_resultats = tk.Label(window2, text="")

        label_categorie.grid(row=0, column=0)
        entry_categorie.grid(row=0, column=1)
        button_rechercher.grid(row=1, column=0, columnspan=2)
        label_resultats.grid(row=2, column=0, columnspan=2)

        

        def afficher_resultats(results):
            results_str = "\n\n".join(results)
            label_resultats.config(text=results_str)
        
        def top_5_restaurants_par_categorie(entry_categorie):
            if entry_categorie == "":
                messagebox.showerror("Erreur","veuillez remplir le champ")
            else:
            
                df_restaurants = df[df['categories'].str.contains('Restaurants') & df['categories'].str.contains(entry_categorie)]
                top_5_restaurants = df_restaurants.nlargest(5, 'stars')
                if len(top_5_restaurants) == 0:
                    afficher_resultats(["Aucun résultat trouvé pour les critères donnés.\n"])
                else:
                    restaurant_strs = []
                    for _, row in top_5_restaurants.iterrows():
                        restaurant_str = f"Nom: {row['name']}\nAdresse: {row['address']}\nVille: {row['city']}\n\n"
                        restaurant_strs.append(restaurant_str)
                    afficher_resultats(restaurant_strs)
        button_rechercher.config(command=lambda: top_5_restaurants_par_categorie(entry_categorie.get()))
        Back_Button_win = tk.Button(window2,text="Back" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=lambda: [back_main_win2()])
        Back_Button_win.grid(row=1, column=1, columnspan=2)

        
        window2.mainloop()



    label = tk.Label(fenetre3, text="Cliquez pour continuer :", font=("Arial", 14), bg='#F0F0F0')
    label.pack(pady=25)

    Login_Button = tk.Button(fenetre3,text="trier :" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=tri)
    Login_Button.pack(pady=10)
    Search_Button = tk.Button(fenetre3,text="top 5 par categories :" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=top_5_restaurants)
    Search_Button.pack()

    Back_Button = tk.Button(fenetre3,text="Back" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=lambda: [back_main(), def_fenetre2()])
    Back_Button.pack()

    Hellobis = "Hello"
    label = tk.Label(fenetre3, text=   Hellobis +"  "+name +"  "+ family, font=("Arial", 14), bg='#F0F0F0')
    label.pack()

    fenetre3.mainloop()





def def_fenetre():

    global fenetre
    fenetre = tk.Tk()
    fenetre.title("hello")
    fenetre.geometry("400x200") 
    

    label = tk.Label(fenetre, text="Cliquez pour continuer :", font=("Arial", 14), bg='#F0F0F0')
    label.pack(pady=25)
    if connecte == 0:
        Login_Button = tk.Button(fenetre,text="Login" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=login_windows)
        Login_Button.pack(pady=10)

    fenetre.mainloop()

def def_fenetre2():
    global fenetre2
    fenetre2 = tk.Tk()
    fenetre2.title("Welcome back")
    fenetre2.geometry("400x200")
    Hellobis = "Hello"
    label = tk.Label(fenetre2, text="Cliquez pour continuer :", font=("Arial", 14), bg='#F0F0F0')
    label.pack(pady=25)

    Search_Button = tk.Button(fenetre2,text="Search" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=search_resto)
    Search_Button.pack()
    tri_Button = tk.Button(fenetre2,text="find" ,font=("Arial", 14),bg="#4CAF50", fg="white", command=tri_resto)
    tri_Button.pack()

    label = tk.Label(fenetre2, text=   Hellobis +"  "+name +"  "+ family, font=("Arial", 14), bg='#F0F0F0')
    label.pack()
    fenetre2.mainloop()


global name
name = ""
global family
family = ""
global connecte
connecte = 0
global Hellobis
"""Hellobis = ""
Hellobis = "Hello"
label = tk.Label(fenetre2, text=   Hellobis +"  "+name +"  "+ family, font=("Arial", 14), bg='#F0F0F0')"""
"""label.pack()"""
def_fenetre()